#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Contains functions used in test cases"""
    def test_negative(self):
        """Tests a list with negative values"""
        self.assertEqual(max_integer([-2, -40, 0, -1]), 0)

    def test_strings(self):
        """Tests error raise if a list has none integers"""
        new_list = [4, "holberton", [3, 3, 4], 7]
        self.assertRaises(TypeError, max_integer, new_list)

    def test_floats(self):
        """Test for floats"""
        self.assertEqual(max_integer([5.98, 4.32, 2, 5.99]), 5.99)

    def test_empty_list(self):
        """Test for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_no_arguments(self):
        """Test with no argumest passed to function"""
        self.assertEqual(max_integer(), None)
