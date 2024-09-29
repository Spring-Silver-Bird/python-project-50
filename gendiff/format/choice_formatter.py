from gendiff.format.stylish import format_diff_stylish
from gendiff.format.plain import format_diff_plain


def format_diff(diff, formatter):
    if formatter == "stylish":
        return format_diff_stylish(diff)
    elif formatter == "plain":
        return format_diff_plain(diff)
    else:
        return f"Формат введен неверно: {formatter}"
