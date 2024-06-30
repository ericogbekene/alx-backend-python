#!/usr/bin/env python3
"""
creating a Unit test module
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """
    Using Unit test module
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test class
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

