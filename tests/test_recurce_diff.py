from gendiff.generate_diff import generate_diff

def test_generate_diff_json():
    first_file = 'tests/fixtures/file_1.json'
    second_file = 'tests/fixtures/file_2.json'
    true_diff = open('tests/fixtures/result_json_depth.txt', 'r', encoding='utf-8')
    diff = generate_diff(first_file, second_file)
    assert diff == true_diff.read()
    true_diff.close()

def test_generate_diff_yml():
    first_file = 'tests/fixtures/file_1.yaml'
    second_file = 'tests/fixtures/file_2.yaml'
    true_diff = open('tests/fixtures/result.txt', 'r', encoding='utf-8')
    diff = generate_diff(first_file, second_file)
    assert diff == true_diff.read()
    true_diff.close()


def test_generate_plain_diff_json():
    first_file = 'tests/fixtures/file_1.json'
    second_file = 'tests/fixtures/file_2.json'
    formatter = 'plain'
    true_diff = open('tests/fixtures/result_json_plain_depth.txt', 'r', encoding='utf-8')
    diff = generate_diff(first_file, second_file, formatter)
    assert diff == true_diff.read()
    true_diff.close()