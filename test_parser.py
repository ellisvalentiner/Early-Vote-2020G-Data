#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from pathlib import Path
from parser import parser

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


if __name__ == "__main__":
    unittest.main()
