import pytest
from gendiff.diff_generator import generate_diff


@pytest.mark.parametrize(
    'path_to_file1, path_to_file2, formatter, expected_result',
    [
        (
            './tests/fixtures/file_1.json',
            './tests/fixtures/file_2.json',
            'stylish',
            './tests/fixtures/tru_stylish_result.txt'
        ),
        (
            './tests/fixtures/file_1.yaml',
            './tests/fixtures/file_2.yaml',
            'stylish',
            './tests/fixtures/tru_stylish_result.txt'
        ),
        (
            './tests/fixtures/file_1.json',
            './tests/fixtures/file_2.json',
            'plain',
            './tests/fixtures/tru_plain_result.txt'
        ),
        (
            './tests/fixtures/file_1.yaml',
            './tests/fixtures/file_2.yaml',
            'plain',
            './tests/fixtures/tru_plain_result.txt'
        ),
        (
            './tests/fixtures/file_1.json',
            './tests/fixtures/file_2.json',
            'json',
            './tests/fixtures/tru_json_result.txt'
        ),
        (
            './tests/fixtures/file_1.yaml',
            './tests/fixtures/file_2.yaml',
            'json',
            './tests/fixtures/tru_json_result.txt'
        )
    ]
)
def test_gendiff(path_to_file1, path_to_file2, formatter, expected_result):
    diff = generate_diff(path_to_file1, path_to_file2, formatter)
    with open(expected_result, 'r', encoding='utf8') as file:
        result = file.read().strip('\n')
        assert diff == result
