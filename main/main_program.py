import json
import os
import time

from main.scanners.definitions_scanner import definitions_scanner
from main.scanners.properties_scanner import properties_scanner

from main.utils.log_utiles import write_to_temp_file, get_temp_file_name, close_temp_file


def greeting():
    print('''\t\tJSON Schema Validator''')


def load_schema_dialog():
    default_path = '.'
    user_path = input(f'Where the schema is stored? [{default_path}] ')

    if user_path.strip() == '':
        user_path = default_path

    return user_path


def handle_schema(schema_path):
    with open(schema_path, 'r') as f:
        schema = json.loads(f.read())

    properties = schema.get('properties')

    if properties:
        properties_scanner(properties, schema_path)

    definitions = schema.get('definitions') if schema.get('definitions') else schema.get('$defs')

    if definitions:
        definitions_scanner(definitions, schema_path)


def display_results():
    close_temp_file()  # Let access to the temp file
    os.system(f'start {get_temp_file_name()}')
    time.sleep(0.1)  # Let to default text editor open the file before deleting it
    os.unlink(get_temp_file_name())


def exiting():
    print('DONE')


def main():
    greeting()
    user_path = load_schema_dialog()

    for file in os.listdir(user_path):
        if file.endswith('.json'):
            write_to_temp_file('\t' + file)
            handle_schema(user_path + file)

    display_results()
    exiting()


if __name__ == '__main__':
    main()
