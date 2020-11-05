#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from pathlib import Path
from data_parser import parser

here = Path(__file__).parent.resolve()


class ParserTest(unittest.TestCase):
    def test_michigan(self):
        expected = {
            "date": "2020-10-21",
            "returned": 1790561,
            "rejected": 1268,
            "requested": 2985473,
            "locality": "",
        }
        result = parser(here / "fixtures/MI.html")
        self.assertDictEqual(result, expected)

    def test_south_carolina(self):
        expected = {
            "date": "2020-11-03",
            "returned": 1309598,
            "requested": 1347886,
            "locality": "",
        }
        result = parser(here / "fixtures/SC.html")
        self.assertDictEqual(result, expected)

    def test_georgia(self):
        expected = {
            "date": "2020-11-02",
            "total": 3912819,
            "in-person": 2689696,
            "returned": 1782653,
            "rejected": 1574,
            "requested": 1782621,
            "locality": "",
            "turnout-rate": 56.5,
        }
        result = parser(here / "fixtures/GA.html")
        self.assertDictEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
