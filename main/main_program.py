import json
import os

from main.scanners.definitions_scanner import definitions_scanner
from main.scanners.properties_scanner import properties_scanner
from datetime import datetime


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


def get_timestamp():
    return datetime.now().strftime('%a__%d_%m_%y__%H_%M_%S')


def exiting():
    print('DONE')


def main():
    greeting()
    user_path = load_schema_dialog()

    for file in os.listdir(user_path):
        if file.endswith('.json'):
            handle_schema(user_path + file)

    exiting()


if __name__ == '__main__':
    main()
