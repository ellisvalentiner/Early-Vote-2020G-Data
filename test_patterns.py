#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from patterns import REPORT_DATE, BALLOTS_RETURNED, BALLOTS_REQUESTED, BIG_NUMBER, DATE


class DatePatternTest(unittest.TestCase):
    def setUp(self) -> None:
        self.examples = [
            ("10/23/2020", ["10/23/2020"]),
            ("Last Report: 10/23/2020", ["10/23/2020"]),
            ("Last Report: 9/2/2020", ["9/2/2020"]),
        ]

    def test_examples(self):
        for example in self.examples:
            matches = DATE.findall(example[0])
            self.assertListEqual(matches, example[1])


class NumberPatternTest(unittest.TestCase):
    def setUp(self) -> None:
        self.examples = [
            ("123", ["123"]),
            ("Ballots Requested: 3,032,987", ["3,032,987"]),
            ("Ballots Returned: 1,985,687", ["1,985,687"]),
        ]

    def test_examples(self):
        for example in self.examples:
            matches = BIG_NUMBER.findall(example[0])
            self.assertListEqual(matches, example[1])


class ReportDatePatternTest(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_examples = [
            "Last Report: 9/29/2020",
            "Last Report: 10/2/2020",
            "Last Report: 10/21/2020" "Last Report: 10/22/2020",
            "Last Report: 10/23/2020",
        ]
        self.invalid_examples = [
            "Alaska voters have cast 73,843 mail ballots.",
            "Ballots Returned: 145,574",
            "Mail Ballots Returned: 81,665",
            "Returned Mail Ballots",
            "Source: Arizona state and county election offices",
            "Arizona does not distinguish between mail ballots returned and in-person votes.",
            "(Requests are missing for Maricopa County at this time.)",
            "Alaska voters have requested 143,519 mail ballots.",
            "Ballots Requested: 217,427",
            "Mail Ballots Requested: 123,057",
            "California voters have requested 21,879,949 mail ballots.",
            "Ballots Requested: 3,032,987",
        ]

    def test_valid_examples(self):
        for example in self.valid_examples:
            matches = REPORT_DATE.findall(example)
            self.assertTrue(matches)

    def test_invalid_examples(self):
        for example in self.invalid_examples:
            matches = REPORT_DATE.findall(example)
            self.assertFalse(matches)


class BallotsReturnedPatternTest(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_examples = [
            "Alaska voters have cast 73,843 mail ballots.",
            "Ballots Returned: 145,574",
            "Mail Ballots Returned: 81,665",
        ]
        self.invalid_examples = [
            "Last Report: 10/23/2020",
            "Returned Mail Ballots",
            "Source: Arizona state and county election offices",
            "Arizona does not distinguish between mail ballots returned and in-person votes.",
            "(Requests are missing for Maricopa County at this time.)",
            "Alaska voters have requested 143,519 mail ballots.",
            "Ballots Requested: 217,427",
            "Mail Ballots Requested: 123,057",
            "California voters have requested 21,879,949 mail ballots.",
            "Ballots Requested: 3,032,987",
        ]

    def test_valid_examples(self):
        for example in self.valid_examples:
            matches = BALLOTS_RETURNED.findall(example)
            self.assertTrue(matches)

    def test_invalid_examples(self):
        for example in self.invalid_examples:
            matches = BALLOTS_RETURNED.findall(example)
            self.assertFalse(matches)


class BallotsRequestedPatternTest(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_examples = [
            "Alaska voters have requested 143,519 mail ballots.",
            "Ballots Requested: 217,427",
            "Mail Ballots Requested: 123,057",
            "California voters have requested 21,879,949 mail ballots.",
            "Ballots Requested: 3,032,987",
        ]
        self.invalid_examples = [
            "Alaska voters have cast 73,843 mail ballots.",
            "Ballots Returned: 145,574",
            "Mail Ballots Returned: 81,665",
            "Last Report: 10/23/2020",
            "Returned Mail Ballots",
            "Source: Arizona state and county election offices",
            "Arizona does not distinguish between mail ballots returned and in-person votes.",
            "(Requests are missing for Maricopa County at this time.)",
        ]

    def test_valid_examples(self):
        for example in self.valid_examples:
            matches = BALLOTS_REQUESTED.findall(example)
            self.assertTrue(matches)

    def test_invalid_examples(self):
        for example in self.invalid_examples:
            matches = BALLOTS_REQUESTED.findall(example)
            self.assertFalse(matches)


if __name__ == "__main__":
    unittest.main()
