#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import json
import numpy as np
from data_parser import to_serializable


class JsonSerializerTest(unittest.TestCase):
    def test_np_int64(self):
        self.assertEqual(json.dumps(np.int64(1), default=to_serializable), "1")

    def test_np_float(self):
        self.assertEqual(json.dumps(np.float(1), default=to_serializable), "1.0")


if __name__ == "__main__":
    unittest.main()
