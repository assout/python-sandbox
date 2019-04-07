#!/usr/bin/env python3

# vim: set fileencoding=utf-8 :

from unittest import TestCase
import unittest
import asspy


class TestFoo(TestCase):

    def test_say(self):
        self.assertEqual(asspy, '2')


if __name__ == "__main__":
    unittest.main()
