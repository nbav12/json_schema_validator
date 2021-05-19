def check_array_property(prop):
    if prop.get('items').get('type') == 'string':
        return check_string_property(prop.get('items'))
    elif prop.get('items').get('type') == 'number':
        return check_number_property(prop.get('items'))


def check_min_length(value):
    return value >= 0


def check_max_length(value):
    return value <= 100


def check_pattern(pattern):
    special_symbols = ['.', '*']

    for index in range(len(pattern)):
        if pattern[index] in special_symbols:
            if pattern[index - 1] != '\\':
                return False

    return True


def check_string_property(prop):
    if prop.get('enum') is not None:
        return True

    is_min_length_valid = False if not prop.get('minLength') else check_min_length(prop.get('minLength'))
    is_max_length_valid = False if not prop.get('maxLength') else check_max_length(prop.get('maxLength'))
    is_pattern_valid = False if not prop.get('pattern') else check_pattern(prop.get('pattern'))

    return is_min_length_valid and is_max_length_valid and is_pattern_valid


def check_number_minimum(value):
    return value is not None


def check_number_maximum(value):
    return value is not None


def check_number_property(prop):
    is_minimum_valid = False if not check_number_minimum(prop.get('minimum')) else True
    is_maximum_valid = False if not check_number_maximum(prop.get('maximum')) else True

    return is_minimum_valid and is_maximum_valid


def check_property(prop):
    if prop.get('type') == 'array':
        return check_array_property(prop)
    elif prop.get('type') == 'string':
        return check_string_property(prop)
    elif prop.get('type') in ['number', 'integer']:
        return check_number_property(prop)
    return True


def properties_scanner(properties):
    for prop in properties:
        if check_property(properties[prop]):
            print('Valid Prop:', prop)
        else:
            print('Invalid Prop:', prop)
