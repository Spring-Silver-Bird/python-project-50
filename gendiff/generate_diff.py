from gendiff.parser import parse_data_from_file as make_data
from gendiff.generate import generate
from gendiff.format.stylish import format_diff_stylish as format


def generate_diff(file_path1, file_path2):
#    print(f'Make data from first file {file_path1}...')
#    print()
    old_data = make_data(file_path1)
#    print(f'Make data from second file {file_path2}...')
#    print()
    new_data = make_data(file_path2)
    diff = generate(old_data, new_data)
#    print(f'Generate different {diff}')
#    print()
    return format(diff)
