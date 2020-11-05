#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import (
    List,
    Dict,
    Union,
)
from urllib.request import urlopen
from functools import singledispatch

import html2text
import pandas as pd
import numpy as np

from patterns import (
    REPORT_DATE,
    REQUESTED,
    RETURNED,
    BIG_NUMBER,
    DATE,
    REJECTED,
    IN_PERSON,
    TOTAL,
    TURNOUT,
    PERCENT,
)
from unmark import unmark

here = Path(__file__).parent.resolve()

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


@singledispatch
def to_serializable(val):
    """Used by default."""
    return str(val)


@to_serializable.register(np.int64)
def np_int64(val):
    return int(val)


@to_serializable.register(np.float)
def np_float(val):
    return "" if np.isnan(val) else float(val)


def resolve_filepath(path: Path) -> str:
    return path.resolve().as_uri()


def convert_html_to_plain_text(doc: str) -> List[str]:
    return [
        unmark(line.strip().lower()) for line in html2text.html2text(doc).splitlines()
    ]


def find_tables(doc: str) -> List[pd.DataFrame]:
    try:
        return [df for df in pd.read_html(doc) if not df.empty]
    except ValueError:
        return []


def extract_total_row(df: pd.DataFrame) -> Dict:
    record = {}
    for k, v in df.iloc[-1, :].to_dict().items():
        column_name = k.lower()
        if RETURNED.findall(column_name):
            record["returned"] = v
        elif REQUESTED.findall(column_name):
            record["requested"] = v
        elif REJECTED.findall(column_name):
            record["rejected"] = v
        elif IN_PERSON.findall(column_name):
            record["in-person"] = v
        elif TOTAL.findall(column_name):
            record["total"] = v
        elif TURNOUT.findall(column_name):
            record["turnout-rate"] = v
    return record


def parser(path: Union[str, Path] = here.resolve() / "tmp.html") -> Dict:
    log.info(f"Processing state: {os.getenv('STATE', '')}")
    file_uri = resolve_filepath(path=path)
    doc = urlopen(url=file_uri).read().decode()  # nosec
    if not doc:
        log.warning("Empty doc!")
        exit(0)
    tables = find_tables(doc)
    record = {}
    for table in tables:
        try:
            record.update(**extract_total_row(table))
        except IndexError:
            log.warning("IndexError processing a table")
            print(table)
            exit(1)
    for line in convert_html_to_plain_text(doc=doc):
        if REPORT_DATE.findall(line):
            for match in DATE.findall(line):
                try:
                    record["date"] = (
                        datetime.strptime(match, "%m/%d/%Y").date().isoformat()
                    )
                except ValueError:
                    record["date"] = match
        elif RETURNED.findall(line):
            for match in BIG_NUMBER.findall(line):
                record["returned"] = int(match.replace(",", ""))
        elif REQUESTED.findall(line):
            for match in BIG_NUMBER.findall(line):
                record["requested"] = int(match.replace(",", ""))
        elif REJECTED.findall(line):
            for match in BIG_NUMBER.findall(line):
                record["rejected"] = int(match.replace(",", ""))
        elif IN_PERSON.findall(line):
            for match in BIG_NUMBER.findall(line):
                record["in-person"] = int(match.replace(",", ""))
        elif TOTAL.findall(line):
            for match in BIG_NUMBER.findall(line):
                record["total"] = int(match.replace(",", ""))
        elif TURNOUT.findall(line):
            for match in PERCENT.findall(line):
                record["turnout-rate"] = float(match)
    if record:
        if not any(
            map(
                lambda x: x
                in [
                    "returned",
                    "requested",
                    "rejected",
                    "in-person",
                    "total",
                    "turnout-rate",
                ],
                record.keys(),
            )
        ):
            return {}
        locality = os.getenv("STATE", "")
        if locality == "index":
            locality = "US"
        record["locality"] = locality
    return record


def main():
    data = parser()
    if data:
        with open(here / "tmp.jsonl", "a") as fh:
            json.dump(data, fh, default=to_serializable, allow_nan=False)
            fh.write("\n")


if __name__ == "__main__":
    main()
