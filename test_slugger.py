#!/usr/bin/env python3
"""test_slugger.py"""

import unittest
import slugger

s = slugger.slugger


class TestSlugger(unittest.TestCase):
    def test_min_word_len(self):
        self.assertEqual(
            s('this is a test'),
            'this-test'
        )
        self.assertEqual(
            s('this is 12 test'),
            'this-12-test'
        )

    def test_pullwords(self):
        self.assertEqual(
            s('test XXXtestXXX'),
            'test'
        )
        self.assertEqual(
            s('test XXXkeepXXX'),
            'test-xxxkeepxxx'
        )

    def test_year_expansion(self):
        self.assertEqual(
            s("bob's '66 Chevy"),
            'bobs-1966-chevy'
        )
        self.assertEqual(
            s("tom's '06 Camaro"),
            'toms-2006-camaro'
        )
        self.assertEqual(
            s('I got 99 problems'),
            'got-99-problems'
        )
        self.assertEqual(
            s("a '49 '50 '51 '52"),
            '1949-1950-1951-1952'
        )

    def test_hypenation(self):
        self.assertEqual(
            s('  -- test ~- string      	'),
            'test-string'
        )
        self.assertEqual(
            s('test-string'),
            'test-string'
        )


if __name__ == "__main__":
    unittest.main()
