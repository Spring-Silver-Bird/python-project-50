from gendiff.generate_diff import generate_diff

def test_generate_flat_diff_json():
    first_file = 'tests/fixtures/file1.json'
    second_file = 'tests/fixtures/file2.json'
    true_diff = open('tests/fixtures/res.txt', 'r', encoding='utf-8')
    diff = generate_diff(first_file, second_file)
    assert diff == true_diff.read()
    true_diff.close()

def test_generate_flat_diff_yml():
    first_file = 'tests/fixtures/file1.yaml'
    second_file = 'tests/fixtures/file2.yaml'
    true_diff = open('tests/fixtures/res.txt', 'r', encoding='utf-8')
    diff = generate_diff(first_file, second_file)
    assert diff == true_diff.read()
    true_diff.close()