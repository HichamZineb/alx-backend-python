#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "a not found"),
        ({"a": 1}, ("a", "b"), "b not found"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_error):
        """Test access_nested_map function with exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_error)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function"""
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

    def test_memoize(self):
        """Test memoize decorator"""
        test_instance = self.TestClass()
        with patch.object(test_instance, 'a_method') as mock_method:
            test_instance.a_property()
            test_instance.a_property()
            mock_method.assert_called_once()

    class TestClass:
        """TestClass class for memoize testing"""

        def a_method(self):
            """Test method"""
            return 42

        @memoize
        def a_property(self):
            """Test property"""
            return self.a_method()


if __name__ == "__main__":
    unittest.main()
