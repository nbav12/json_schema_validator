from main.exceptions.array_type_exception import ArrayTypeException
from main.exceptions.number_type_exception import NumberTypeException
from main.exceptions.string_type_exception import StringTypeException
from main.utils.check_keywords import check_keyword
from main.utils.definitions_utils import find_definition_line


def definitions_scanner(definitions, schema_path):
    for definition in definitions:
        try:
            check_keyword(definitions[definition], schema_path)
        except NumberTypeException:
            if schema_path is not None:
                definition_line = find_definition_line(definition, schema_path)
                print(f'Line[{definition_line}]:\t"{definition}" '
                      f'definition (integer|number) missing minimum or maximum keyword')
        except StringTypeException:
            if schema_path is not None:
                definition_line = find_definition_line(definition, schema_path)
                print(f'Line[{definition_line}]:\t"{definition}"'
                      f' definition (string) missing minLength, maxLength or pattern keyword')
        except ArrayTypeException:
            if schema_path is not None:
                definition_line = find_definition_line(definition, schema_path)
                print(f'Line[{definition_line}]:\t"{definition}" definition (array) missing explicit type of items')
