import json
import os

from main.scanners.definition_scanner import definition_scanner
from main.scanners.properties_scanner import properties_scanner


def greeting():
    print('''\t\tJSON Schema Validator''')


def load_schema_dialog():
    default_path = '.'
    user_path = input(f'Where the schema is stored? [{default_path}] ')

    if user_path.strip() == '':
        user_path = default_path

    load_schema(user_path)


def load_schema(path):
    for file in os.listdir(path):
        if file.endswith('.json'):
            handle_schema(path + file)


def handle_schema(schema_path):
    with open(schema_path, 'r') as f:
        schema = json.loads(f.read())

    properties = schema.get('properties')

    if properties:
        properties_scanner(properties, schema_path)

    definition = schema.get('definition') if schema.get('definition') else schema.get('$defs')

    if definition:
        definition_scanner(definition, schema_path)


def main():
    greeting()
    load_schema_dialog()


if __name__ == '__main__':
    main()
