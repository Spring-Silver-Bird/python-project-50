from gendiff.parser import get_data_of_file as parse


def generate_diff(file_path1, file_path2):
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    results = '{\n'
    for key, value in sorted(file1.items()):
        if key in file2 and value == file2[key]:
            results += f"    {key}: {value}\n"
        elif key not in file2 or value != file2[key]:
            results += f"  - {key}: {value}\n"
    for key, value in sorted(file2.items()):
        if key not in file1 or value != file1[key]:
            results += f"  + {key}: {value}\n"
    results += '}\n'
    return results
