#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unmark import unmark


class UnmarkTest(unittest.TestCase):
    def test_remove_italics(self):
        examples = [
            ("*This text will be italic*", "This text will be italic"),
            ("_This will also be italic_", "This will also be italic"),
        ]
        for example in examples:
            plain = unmark(example[0])
            self.assertEqual(plain, example[1])

    def test_remove_bold(self):
        examples = [
            ("**This text will be bold**", "This text will be bold"),
            ("__This will also be bold__", "This will also be bold"),
        ]
        for example in examples:
            plain = unmark(example[0])
            self.assertEqual(plain, example[1])

    def test_remove_emphasis(self):
        examples = [
            ("_You **can** combine them_", "You can combine them"),
        ]
        for example in examples:
            plain = unmark(example[0])
            self.assertEqual(plain, example[1])


if __name__ == "__main__":
    unittest.main()
