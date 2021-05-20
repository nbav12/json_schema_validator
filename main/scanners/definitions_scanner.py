from main.exceptions.array_type_exception import ArrayTypeException
from main.exceptions.number_type_exception import NumberTypeException
from main.exceptions.string_type_exception import StringTypeException
from main.utils.check_keywords import check_keyword
from main.utils.definitions_utils import find_definition_line
from main.utils.log_utiles import write_to_temp_file


def definitions_scanner(definitions, schema_path):
    for definition in definitions:
        try:
            check_keyword(definitions[definition], schema_path)
        except NumberTypeException as e:
            if schema_path is not None:
                definition_line = find_definition_line(definition, schema_path)
                write_to_temp_file(f'Line[{definition_line}]:\t"{definition}" Definition: {e}')
        except StringTypeException as e:
            if schema_path is not None:
                definition_line = find_definition_line(definition, schema_path)
                write_to_temp_file(f'Line[{definition_line}]:\t"{definition}" Definition: {e}')
        except ArrayTypeException as e:
            if schema_path is not None:
                definition_line = find_definition_line(definition, schema_path)
                write_to_temp_file(f'Line[{definition_line}]:\t"{definition}" Definition: {e}')
