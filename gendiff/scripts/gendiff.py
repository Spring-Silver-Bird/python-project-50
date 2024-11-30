from gendiff.diff_generator import generate_diff
from gendiff.cli import get_parser_args


def main():
    args = get_parser_args()
    diff = generate_diff(args.path_file1, args.path_file2, args.format)
    print(diff)


if __name__ == '__main__':
    main()
