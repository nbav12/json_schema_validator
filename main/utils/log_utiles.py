import os


def write_to_log_file(logs, schema_path):
    from main.main_program import get_timestamp

    timestamp = get_timestamp()
    user_dir = os.environ.get('USERPROFILE')
    schema_name = extract_schema_name_from_path(schema_path)
    log_path = f'{user_dir}/Desktop/{schema_name}_{timestamp}_log.txt'

    with open(log_path, 'a') as f:
        f.write(logs + '\n')


def extract_schema_name_from_path(schema_path):
    schema_name_index = schema_path.rfind('/') + 1

    return schema_path[schema_name_index:]
