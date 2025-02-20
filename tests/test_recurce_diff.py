import pytest

from gendiff.diff_generator import generate_diff


@pytest.mark.parametrize(
    'path_to_file1, path_to_file2, formatter, expected_result',
    [
        (
            './tests/test_data/file_1.json',
            './tests/test_data/file_2.json',
            'stylish',
            './tests/test_data/tru_stylish_result.txt'
        ),
        (
            './tests/test_data/file_1.yaml',
            './tests/test_data/file_2.yaml',
            'stylish',
            './tests/test_data/tru_stylish_result.txt'
        ),
        (
            './tests/test_data/file_1.json',
            './tests/test_data/file_2.json',
            'plain',
            './tests/test_data/tru_plain_result.txt'
        ),
        (
            './tests/test_data/file_1.yaml',
            './tests/test_data/file_2.yaml',
            'plain',
            './tests/test_data/tru_plain_result.txt'
        ),
        (
            './tests/test_data/file_1.json',
            './tests/test_data/file_2.json',
            'json',
            './tests/test_data/tru_json_result.txt'
        ),
        (
            './tests/test_data/file_1.yaml',
            './tests/test_data/file_2.yaml',
            'json',
            './tests/test_data/tru_json_result.txt'
        )
    ]
)
def test_gendiff(path_to_file1, path_to_file2, formatter, expected_result):
    diff = generate_diff(path_to_file1, path_to_file2, formatter)
    with open(expected_result, 'r', encoding='utf8') as file:
        result = file.read().strip('\n')
        assert diff == result


def test_exception():
    with pytest.raises(ValueError):
        generate_diff('./tests/test_data/file_1.json',
            './tests/test_data/file_2.txt',)
