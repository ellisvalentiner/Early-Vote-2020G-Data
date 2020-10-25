#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

DATE = re.compile("[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}")

_number = "[0-9]{1,3}(?:,[0-9]{3})*"
BIG_NUMBER = re.compile(_number)

REPORT_DATE = re.compile(".*[0-9]{1,2}/[0-9]{1,2}/2020")

BALLOTS_RETURNED = re.compile(
    "("
    f".*voters have cast {_number} mail ballots."
    f"|Ballots Returned: {_number}"
    ")"
)

BALLOTS_REQUESTED = re.compile(
    "("
    f".* voters have requested {_number} mail ballots."
    f"|Ballots Requested: {_number}"
    ")"
)
