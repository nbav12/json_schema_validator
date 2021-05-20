from main.exceptions.array_type_exception import ArrayTypeException
from main.exceptions.number_type_exception import NumberTypeException
from main.exceptions.string_type_exception import StringTypeException


def check_array_keyword(keyword):
    # Without explicit type of items
    if keyword.get('items') is None:
        raise ArrayTypeException('(array) without explicit type of items')
    # Without correct definition of items
    if type(keyword.get('items')) != dict:
        raise ArrayTypeException('(array) without correct definition of items')
    if keyword.get('items').get('type') == 'string':
        return check_string_keyword(keyword.get('items'))
    elif keyword.get('items').get('type') == 'number':
        return check_number_keyword(keyword.get('items'))


def check_min_length(value):
    return value >= 0


def check_max_length(value):
    return value <= 100


def check_string_keyword(keyword):
    if keyword.get('enum') is not None:
        return True

    is_min_length_valid = False if not keyword.get('minLength') else check_min_length(keyword.get('minLength'))
    is_max_length_valid = False if not keyword.get('maxLength') else check_max_length(keyword.get('maxLength'))
    is_pattern_valid = False if not keyword.get('pattern') else check_pattern(keyword.get('pattern'))

    if not (is_min_length_valid and is_max_length_valid and is_pattern_valid):
        raise StringTypeException('(string) missing minLength|maxLength|pattern keyword')

    return True


def check_number_minimum(value):
    return value is not None


def check_number_maximum(value):
    return value is not None


def check_number_keyword(keyword):
    is_minimum_valid = False if not check_number_minimum(keyword.get('minimum')) else True
    is_maximum_valid = False if not check_number_maximum(keyword.get('maximum')) else True

    if not (is_minimum_valid and is_maximum_valid):
        raise NumberTypeException('(integer|number) missing minimum|maximum keyword')

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


def check_keyword(keyword, schema_path=None):
    # If keyword doesn't contain type (e.g. $ref to some definition|property)
    if keyword.get('type') is None:
        return
    if 'array' in keyword.get('type'):
        check_array_keyword(keyword)
    elif 'string' in keyword.get('type'):
        check_string_keyword(keyword)
    elif ('number' in keyword.get('type')) or ('integer' in keyword.get('type')):
        check_number_keyword(keyword)
    elif 'object' in keyword.get('type'):
        from main.scanners.definitions_scanner import definitions_scanner
        from main.scanners.properties_scanner import properties_scanner

        try:
            properties_scanner(keyword.get('properties'), schema_path)
        # In case the object references to additionalProperties
        except TypeError:
            pass

        try:
            definitions_scanner(keyword.get('definitions'), schema_path)
        # In case the object without definitions keyword
        except TypeError:
            pass
