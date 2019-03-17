#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import mlbcolors


class MlbColorsTest(unittest.TestCase):

    def test_get(self):
        mlbcolors.get("CHC")
        with self.assertRaises(KeyError):
            mlbcolors.get("FOOBAR")


if __name__ == '__main__':
    unittest.main()
