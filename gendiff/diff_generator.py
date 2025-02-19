from gendiff.format.choice_formatter import format_diff
from gendiff.generate import generate
from gendiff.parser import parse_data_from_file as make_data


def generate_diff(file_path1, file_path2, formatter='stylish'):
    old_data = make_data(file_path1)
    new_data = make_data(file_path2)
    diff = generate(old_data, new_data)
    return format_diff(diff, formatter)
