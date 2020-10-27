#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
from pathlib import Path
from typing import List, Dict, Union
from urllib.request import urlopen
from datetime import datetime

import html2text

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


def convert_html_to_plain_text(filepath: Union[str, Path]) -> List[str]:
    uri = filepath.as_uri()
    doc = urlopen(url=uri).read().decode()  # nosec
    return [unmark(line.strip()) for line in html2text.html2text(doc).splitlines()]


def parser(path: Union[str, Path] = here.resolve() / "tmp.html") -> Dict:
    record = {}
    for line in convert_html_to_plain_text(path):
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
                record["turnout-rate"] = int(match.replace(",", ""))
    if record:
        locality = os.getenv("STATE", "")
        if locality == "index":
            locality = "US"
        record["locality"] = locality
    return record


def main():
    data = parser()
    if data:
        with open(here / "data.jsonl", "a") as fh:
            json.dump(data, fh)
            fh.write("\n")


if __name__ == "__main__":
    main()
