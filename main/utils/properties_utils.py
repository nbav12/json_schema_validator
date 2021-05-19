def find_prop_line(prop, schema_path):
    with open(schema_path, 'r') as f:
        schema = f.read().split('\n')

    for line_index in range(len(schema)):
        if f'"{prop}"' in schema[line_index]:
            print(f'Line[{line_index + 1}]', end=':\t')
            break
