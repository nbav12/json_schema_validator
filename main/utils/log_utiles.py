import os
import tempfile
from datetime import datetime

TEMP_FILE = tempfile.TemporaryFile(mode='a+t', delete=False, suffix='.txt')


def write_to_temp_file(logs):
    TEMP_FILE.write(logs + '\n')


def read_from_temp_file():
    TEMP_FILE.seek(0)

    return TEMP_FILE.read()


def get_temp_file_name():
    return TEMP_FILE.name


def close_temp_file():
    TEMP_FILE.close()


def write_to_log_file(logs, schema_path):
    timestamp = get_timestamp()
    user_dir = os.environ.get('USERPROFILE')
    schema_name = extract_schema_name_from_path(schema_path)
    log_path = f'{user_dir}/Desktop/{schema_name}_{timestamp}_log.txt'

    with open(log_path, 'a') as f:
        f.write(logs + '\n')


def get_timestamp():
    return datetime.now().strftime('%a__%d_%m_%y__%H_%M_%S')


def extract_schema_name_from_path(schema_path):
    schema_name_index = schema_path.rfind('/') + 1

    return schema_path[schema_name_index:]
