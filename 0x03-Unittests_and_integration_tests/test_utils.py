#!/usr/bin/env python3
"""
creating a Unit test module
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence

class TestAccessNestedMap(unittest.TestCase):
    """
    Using Unit test module
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected):
        """
        test class
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence):
        """
        test that the method raises an Error
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), str(path[-1]))
