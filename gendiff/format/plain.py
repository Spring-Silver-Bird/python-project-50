def format_string(value):
    if isinstance(value, (list, dict)):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def make_plain_result_item(item, path=''):
    current_key = item['name']
    current_path = f"{path}.{current_key}" if path else current_key
    action = item['status']

    match action:
        case 'added':
            new_value = format_string(item['new_value'])
            return f"Property '{current_path}' was added with value: {new_value}"
        case 'deleted':
            return f"Property '{current_path}' was removed"
        case 'changed':
            old_value = format_string(item['old_value'])
            new_value = format_string(item['new_value'])
            return f"Property '{current_path}' was updated. From {old_value} to {new_value}"
        case 'nested':
            return make_plain_result(item['children'], current_path)


def make_plain_result(diff, path=''):
    result = []
    for item in diff:
        formatted_item = make_plain_result_item(item, path)
        if formatted_item is not None:
            result.append(formatted_item)

    return '\n'.join(result)


def format_diff_plain(data):
    return make_plain_result(data)
