from unittest import TestCase

from main.scanners.properties_scanner import *


class TestPropertiesScanner(TestCase):
    def test_check_array_property__invalid_string_items(self):
        prop = {'type': 'array', 'items': {'type': 'string'}}

        with self.assertRaises(StringTypeException):
            check_array_property(prop)

    def test_check_array_property__valid_string_items(self):
        prop = {'type': 'array', 'items': {'type': 'string', 'minLength': 1, 'maxLength': 99, 'pattern': 'foo'}}
        result = check_array_property(prop)

        self.assertTrue(result)

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

    def test_check_pattern(self):
        self.fail()

    def test_check_string_property__missing_min_length(self):
        prop = {'type': 'string', 'maxLength': 99, 'pattern': 'foo'}
        with self.assertRaises(StringTypeException):
            check_string_property(prop)

    def test_check_string_property__missing_max_length(self):
        prop = {'type': 'string', 'mixLength': 1, 'pattern': 'foo'}

        with self.assertRaises(StringTypeException):
            check_string_property(prop)

    def test_check_string_property__missing_pattern(self):
        prop = {'type': 'string', 'mixLength': 1, 'maxLength': 99}

        with self.assertRaises(StringTypeException):
            check_string_property(prop)

    def test_check_string_property__valid(self):
        prop = {'type': 'string', 'minLength': 1, 'maxLength': 99, 'pattern': 'foo'}
        result = check_string_property(prop)

        self.assertTrue(result)

    def test_check_string_property__with_enum(self):
        prop = {'type': 'string', 'enum': []}
        result = check_string_property(prop)

        self.assertTrue(result)

    def test_check_number_property__valid(self):
        prop = {'type': 'number', 'minimum': 1, 'maximum': 55}
        result = check_number_property(prop)

        self.assertTrue(result)

    def test_check_property__invalid_integer_property(self):
        prop = {'type': 'integer', 'maximum': 55}

        with self.assertRaises(NumberTypeException):
            check_property(prop)

    def test_check_property__invalid_number_property(self):
        prop = {'type': 'number', 'minimum': 1}

        with self.assertRaises(NumberTypeException):
            check_property(prop)

    def test_check_property__invalid_string_property(self):
        prop = {'type': 'string', 'minLength': 1}

        with self.assertRaises(StringTypeException):
            check_property(prop)

    def test_check_property__invalid_array_property(self):
        prop = {'type': 'array', 'items': {'type': 'string'}}

        with self.assertRaises(StringTypeException):
            check_property(prop)

    def test_check_property__unchecked_type(self):
        prop = {'type': 'enum'}
        result = check_property(prop)

        self.assertTrue(result)

    def test_check_property__property_with_valid_object(self):
        prop = {'type': 'object', 'properties': {'veggieName': {'type': 'number', 'minimum': 1, 'maximum': 10}}}
        result = check_property(prop)

        self.assertTrue(result)

    def test_check_property__property_with_invalid_object(self):
        prop = {'type': 'object', 'properties': {'veggieName': {'type': 'number', 'maximum': 10}}}
        result = check_property(prop)

        self.assertFalse(result)
