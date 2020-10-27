#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

DATE = re.compile("[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}")

_number = "[0-9]{1,3}(?:,[0-9]{3})*"
BIG_NUMBER = re.compile(_number)

REPORT_DATE = re.compile(".*[0-9]{1,2}/[0-9]{1,2}/2020")

RETURNED = re.compile(
    "("
    f".*voters have cast {_number} mail ballots."
    f"|Ballots Returned: {_number}"
    ")"
)

REQUESTED = re.compile(
    "("
    f".* voters have requested {_number} mail ballots."
    f"|Ballots Requested: {_number}"
    ")"
)

REJECTED = re.compile(
    "("
    f".* election officials have rejected {_number} mail ballots."
    f"|Ballots Rejected: {_number}"
    ")"
)

IN_PERSON = re.compile(
    "("
    f".* voters have cast {_number} in-person early votes."
    f"|In-Person Votes: {_number}"
    ")"
)

TOTAL = re.compile("(" f"Total Voted: {_number}" ")")

TURNOUT = re.compile(
    "("
    "Total Vote as Percentage of 2016 Total Turnout: [0-9]{1,2}\\.[0-9]%"
    "|Total Voted as Percentage of Registered Voters: [0-9]{1,2}\\.[0-9]%"
    "|Total Early Vote as Percentage of 2016 Total Turnout: [0-9]{1,2}\\.[0-9]%"
    "|Turnout Rate \\(of Registered Voters\\): [0-9]{1,2}\\.[0-9]%"
    ")"
)

PERCENT = re.compile("[0-9]{1,2}\\.[0-9]")
