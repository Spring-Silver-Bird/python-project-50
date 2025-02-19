import json
import os

import yaml


def get_format_file(file_path):
    """
    Parses a file based on its extension ('yaml', 'yml', 'json').

    Supports YAML and JSON formats. Raises an error for unsupported formats.
    """
    _, extension = os.path.splitext(file_path)
    return extension[1:]


def parse_data(file, format):
    if format == 'json':
        return json.load(file)
    if format == 'yaml' or format == 'yml':
        return yaml.safe_load(file)
    raise ValueError('Unsupported format.'
                     'Next formats are supported: .json .yaml .yml')


def parse_data_from_file(file_path):
    format = get_format_file(file_path)
    with open(file_path) as content:
        return parse_data(content, format)
