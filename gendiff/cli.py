import argparse


def get_parser_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('path_file1',
                        type=str,
                        help='Path to the first (old) file.')
    parser.add_argument('path_file2',
                        type=str,
                        help='Path to the second (new) file.')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        choices=['stylish', 'plain', 'json'],
        default='stylish', type=str
    )
    return parser.parse_args()
