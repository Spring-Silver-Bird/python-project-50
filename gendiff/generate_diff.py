import argparse
import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file_1, open(file_path2, 'r') as file_2:
        file1 = json.load(file_1)
        file2 = json.load(file_2)
        results = '{\n'
        for key, value in sorted(file1.items()):
            if key in file2 and value == file2[key]:
                results += f"    {key}: {value}\n"
            elif key not in file2 or value != file2[key]:
                results += f"  - {key}: {value}\n"
        for key, value in sorted(file2.items()):
            if key not in file1 or value != file1[key]:
                results += f"  + {key}: {value}\n"
        results += '}'
        return results



