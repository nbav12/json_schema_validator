from main.exceptions.number_type_exception import NumberTypeException
from main.exceptions.string_type_exception import StringTypeException
from main.utils.properties_utils import find_prop_line


def check_array_property(prop):
    if prop.get('items').get('type') == 'string':
        return check_string_property(prop.get('items'))
    elif prop.get('items').get('type') == 'number':
        return check_number_property(prop.get('items'))


def check_min_length(value):
    return value >= 0


def check_max_length(value):
    return value <= 100


def check_string_property(prop):
    if prop.get('enum') is not None:
        return True

    is_min_length_valid = False if not prop.get('minLength') else check_min_length(prop.get('minLength'))
    is_max_length_valid = False if not prop.get('maxLength') else check_max_length(prop.get('maxLength'))
    is_pattern_valid = False if not prop.get('pattern') else check_pattern(prop.get('pattern'))

    if not (is_min_length_valid and is_max_length_valid and is_pattern_valid):
        raise StringTypeException()

    return True


def check_number_minimum(value):
    return value is not None


def check_number_maximum(value):
    return value is not None


def check_number_property(prop):
    is_minimum_valid = False if not check_number_minimum(prop.get('minimum')) else True
    is_maximum_valid = False if not check_number_maximum(prop.get('maximum')) else True

    if not (is_minimum_valid and is_maximum_valid):
        raise NumberTypeException()

    return True


def check_pattern(pattern):
    special_symbols = ['.', '*', '?', '+']

    if pattern[0] in special_symbols:
        return False

    for index in range(1, len(pattern)):
        if pattern[index] in special_symbols:
            if pattern[index - 1] != '\\':
                return False

    return True


def check_property(prop, schema_path=None):
    if prop.get('type') == 'array':
        return check_array_property(prop)
    elif prop.get('type') == 'string':
        return check_string_property(prop)
    elif prop.get('type') in ['number', 'integer']:
        return check_number_property(prop)
    elif prop.get('type') == 'object':
        return properties_scanner(prop.get('properties'), schema_path)
    else:
        return True


def properties_scanner(properties, schema_path):
    for prop in properties:
        try:
            return check_property(properties[prop], schema_path)
        except NumberTypeException:
            if schema_path is not None:
                find_prop_line(prop, schema_path)
                print(f'"{prop}" property missing minimum or maximum keyword')

            return False
        except StringTypeException:
            if schema_path is not None:
                find_prop_line(prop, schema_path)
                print(f'"{prop}" property missing minLength, maxLength or pattern keyword')

            return False
