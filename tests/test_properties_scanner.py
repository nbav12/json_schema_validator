from unittest import TestCase

from main.scanners.properties_scanner import *
from main.utils.check_keywords import check_number_keyword, check_string_keyword, check_max_length, check_min_length, \
    check_array_keyword, check_pattern


class TestPropertiesScanner(TestCase):
    def test_check_array_keyword__invalid_string_items(self):
        prop = {'type': 'array', 'items': {'type': 'string'}}

        with self.assertRaises(StringTypeException):
            check_array_keyword(prop)

    def test_check_array_keyword__valid_string_items(self):
        prop = {'type': 'array', 'items': {'type': 'string', 'minLength': 1, 'maxLength': 99, 'pattern': 'foo'}}
        result = check_array_keyword(prop)

        self.assertTrue(result)

    def test_check_array_keyword__array_without_type_of_items(self):
        prop = {'type': 'array'}

        with self.assertRaises(ArrayTypeException):
            check_array_keyword(prop)

    def test_check_array_keyword__incorrect_definition_of_items(self):
        prop = {'type': 'array', 'items': True}

        with self.assertRaises(ArrayTypeException):
            check_array_keyword(prop)

    def test_check_min_length__negative_length(self):
        result = check_min_length(-1)

        self.assertFalse(result)

    def test_check_min_length__zero_length(self):
        result = check_min_length(0)

        self.assertTrue(result)

    def test_check_min_length__positive_length(self):
        result = check_min_length(1)

        self.assertTrue(result)

    def test_check_max_length__under_valid_length(self):
        result = check_max_length(99)

        self.assertTrue(result)

    def test_check_max_length__exact_valid_length(self):
        result = check_max_length(100)

        self.assertTrue(result)

    def test_check_max_length__more_than_valid_length(self):
        result = check_max_length(101)

        self.assertFalse(result)

    def test_check_string_keyword__missing_min_length(self):
        prop = {'type': 'string', 'maxLength': 99, 'pattern': 'foo'}
        with self.assertRaises(StringTypeException):
            check_string_keyword(prop)

    def test_check_string_keyword__missing_max_length(self):
        prop = {'type': 'string', 'mixLength': 1, 'pattern': 'foo'}

        with self.assertRaises(StringTypeException):
            check_string_keyword(prop)

    def test_check_string_keyword__missing_pattern(self):
        prop = {'type': 'string', 'mixLength': 1, 'maxLength': 99}

        with self.assertRaises(StringTypeException):
            check_string_keyword(prop)

    def test_check_string_keyword__valid(self):
        prop = {'type': 'string', 'minLength': 1, 'maxLength': 99, 'pattern': 'foo'}
        result = check_string_keyword(prop)

        self.assertTrue(result)

    def test_check_string_keyword__with_enum(self):
        prop = {'type': 'string', 'enum': []}
        result = check_string_keyword(prop)

        self.assertTrue(result)

    def test_check_number_keyword__valid(self):
        prop = {'type': 'number', 'minimum': 1, 'maximum': 55}
        result = check_number_keyword(prop)

        self.assertTrue(result)

    def test_check_keyword__invalid_integer_keyword(self):
        prop = {'type': 'integer', 'maximum': 55}

        with self.assertRaises(NumberTypeException):
            check_keyword(prop)

    def test_check_keyword__invalid_number_keyword(self):
        prop = {'type': 'number', 'minimum': 1}

        with self.assertRaises(NumberTypeException):
            check_keyword(prop)

    def test_check_keyword__invalid_string_keyword(self):
        prop = {'type': 'string', 'minLength': 1}

        with self.assertRaises(StringTypeException):
            check_keyword(prop)

    def test_check_keyword__invalid_array_keyword(self):
        prop = {'type': 'array', 'items': {'type': 'string'}}

        with self.assertRaises(StringTypeException):
            check_keyword(prop)

    def test_check_keyword__unchecked_type(self):
        prop = {'type': 'enum'}
        result = check_keyword(prop)

        self.assertIsNone(result)

    def test_check_keyword__keyword_with_valid_object(self):
        prop = {'type': 'object', 'properties': {'veggieName': {'type': 'number', 'minimum': 1, 'maximum': 10}}}
        result = check_keyword(prop)

        self.assertIsNone(result)

    def test_check_keyword__keyword_with_invalid_object(self):
        prop = {'type': 'object', 'properties': {'veggieName': {'type': 'number', 'maximum': 10}}}
        result = check_keyword(prop)

        self.assertFalse(result)

    def test_check_pattern__special_symbol_without_backslash(self):
        pattern = '[abc?]'
        result = check_pattern(pattern)

        self.assertFalse(result)

    def test_check_pattern__special_symbol_with_backslash(self):
        pattern = '[abc\?]'
        result = check_pattern(pattern)

        self.assertTrue(result)

    def test_check_pattern__special_symbol_without_backslash_at_beginning(self):
        pattern = '?[abc]'
        result = check_pattern(pattern)

        self.assertFalse(result)

    def test_check_pattern__special_symbol_with_backslash_at_beginning(self):
        pattern = '\?[abc]'
        result = check_pattern(pattern)

        self.assertTrue(result)
