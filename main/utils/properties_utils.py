def find_prop_line(prop, schema_path):
    with open(schema_path, 'r') as f:
        schema = f.read().split('\n')

    for line_index in range(len(schema)):
        if f'"properties"' in schema[line_index]:
            properties_line = line_index + 1
            break

    for line_index in range(properties_line, len(schema)):
        if f'"{prop}"' in schema[line_index]:
            return line_index + 1
