from gendiff.parser import get_data_of_file as parse
import json

def generate_diff(file_path1, file_path2):
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    #print(file1)
    #print(file2)
    results = '{\n'
    results_dict = {}
    for key, value in sorted(file1.items()):
        if key in file2 and value == file2[key]:
            k = '    '+key
            results_dict[k] = value
            results += f"    {key}: {value}\n"
        elif key not in file2 or value != file2[key]:
            k = '  - ' + key
            results_dict[k] = value
            results += f"  - {key}: {value}\n"
    for key, value in sorted(file2.items()):
        if key not in file1 or value != file1[key]:
            k = '  + ' + key
            results_dict[k] = value
            results += f"  + {key}: {value}\n"
    results += '}\n'
    #print(json.dumps(results_dict))
    return results.lower()
