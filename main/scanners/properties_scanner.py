from main.exceptions.array_type_exception import ArrayTypeException
from main.exceptions.number_type_exception import NumberTypeException
from main.exceptions.string_type_exception import StringTypeException
from main.utils.check_keywords import check_keyword
from main.utils.properties_utils import find_prop_line


def properties_scanner(properties, schema_path):
    for prop in properties:
        try:
            check_keyword(properties[prop], schema_path)
        except NumberTypeException:
            if schema_path is not None:
                prop_line = find_prop_line(prop, schema_path)
                print(f'Line[{prop_line}]:\t"{prop}" property (integer|number) missing minimum or maximum keyword')

        except StringTypeException:
            if schema_path is not None:
                prop_line = find_prop_line(prop, schema_path)
                print(f'Line[{prop_line}]:\t"{prop}" property (string) missing minLength, maxLength or pattern keyword')
        except ArrayTypeException:
            if schema_path is not None:
                prop_line = find_prop_line(prop, schema_path)
                print(f'Line[{prop_line}]:\t"{prop}" property (array) missing explicit type of items')
