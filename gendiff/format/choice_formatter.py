from gendiff.format.json import format_diff_json
from gendiff.format.plain import format_diff_plain
from gendiff.format.stylish import format_diff_stylish


def format_diff(diff, formatter):
    if formatter == "stylish":
        return format_diff_stylish(diff)
    elif formatter == "plain":
        return format_diff_plain(diff)
    elif formatter == "json":
        return format_diff_json(diff)
    else:
        return f"Invalid format: {formatter}"
