import json
import yaml
import os

def get_data_of_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    with open(file_path) as file:
        return parse_data(file, file_extension[1:])


def parse_data(file, extension):
    if extension == 'json':
        return json.load(file)
    if extension == 'yaml' or extension == 'yml':
        return yaml.safe_load(file)
    raise ValueError('Unsupported format. Next formats are supported: .json .yaml .yml')

