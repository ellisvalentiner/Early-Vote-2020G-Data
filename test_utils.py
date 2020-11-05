#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import pandas as pd
from data_parser import find_tables


class FindTablesTest(unittest.TestCase):
    def test_find_tables(self):
        doc = """
            <table class="table table-striped" style="width: auto !important; ">
            <thead>
            <tr>
            <th style="text-align:left;">
            Column
            </th>
            </tr>
            </thead>
            <tbody>
            <tr>
            <td style="text-align:left;">
            Row
            </td>
            </tr>
            </tbody>
            </table>
        """
        tables = find_tables(doc)
        df = tables[0]
        expected_df = pd.DataFrame.from_dict({0: {"Column": "Row"}}, orient="index")
        pd.testing.assert_frame_equal(df, expected_df)

    def test_no_tables(self):
        doc = "<head></head>"
        tables = find_tables(doc)
        self.assertListEqual(tables, [])


if __name__ == "__main__":
    unittest.main()
