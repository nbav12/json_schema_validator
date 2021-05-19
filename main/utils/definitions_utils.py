def find_definition_line(prop, schema_path):
    with open(schema_path, 'r') as f:
        schema = f.read().split('\n')

    for line_index in range(len(schema)):
        if f'"definitions"' in schema[line_index]:
            definitions_line = line_index + 1
            break

    for line_index in range(definitions_line, len(schema)):
        if f'"{prop}"' in schema[line_index]:
            return line_index + 1
