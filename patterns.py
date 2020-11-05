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
    f"|ballots returned: {_number}"
    f"|mail ballots {_number}"
    f"|returned ballots"
    ")"
)

REQUESTED = re.compile(
    "("
    f".* voters have requested {_number} mail ballots."
    f"|ballots requested: {_number}"
    f"|mail ballot requests {_number}"
    "|requested ballots"
    ")"
)

REJECTED = re.compile(
    "("
    f".* election officials have rejected {_number} mail ballots."
    f"|ballots rejected: {_number}"
    ")"
)

IN_PERSON = re.compile(
    "("
    f".* voters have cast {_number} in-person early votes."
    f"|in-person votes: {_number}"
    f"|in-person early votes: {_number}"
    ")"
)

TOTAL = re.compile("(" f"total voted: {_number}" ")")

TURNOUT = re.compile(
    "("
    "total vote as percentage of 2016 total turnout: [0-9]{1,2}\\.[0-9]%"
    "|total voted as percentage of registered voters: [0-9]{1,2}\\.[0-9]%"
    "|total early vote as percentage of 2016 total turnout: [0-9]{1,2}\\.[0-9]%"
    "|turnout rate \\(of registered voters\\): [0-9]{1,2}\\.[0-9]%"
    ")"
)

PERCENT = re.compile("[0-9]{1,2}\\.[0-9]")
