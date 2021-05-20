from main.exceptions.array_type_exception import ArrayTypeException
from main.exceptions.number_type_exception import NumberTypeException
from main.exceptions.string_type_exception import StringTypeException
from main.utils.check_keywords import check_keyword
from main.utils.log_utiles import write_to_temp_file
from main.utils.properties_utils import find_prop_line


def properties_scanner(properties, schema_path):
    for prop in properties:
        try:
            check_keyword(properties[prop], schema_path)
        except NumberTypeException as e:
            if schema_path is not None:
                prop_line = find_prop_line(prop, schema_path)
                write_to_temp_file(f'Line[{prop_line}]:\t"{prop}" Property: {e}')
        except StringTypeException as e:
            if schema_path is not None:
                prop_line = find_prop_line(prop, schema_path)
                write_to_temp_file(f'Line[{prop_line}]:\t"{prop}" Property: {e}')
        except ArrayTypeException as e:
            if schema_path is not None:
                prop_line = find_prop_line(prop, schema_path)
                write_to_temp_file(f'Line[{prop_line}]:\t"{prop}" Property: {e}')
