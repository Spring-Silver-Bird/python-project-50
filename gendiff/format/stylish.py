SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '
DEFAULT_INDENT = 4


def format_string(value, depth=1):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int) or isinstance(value, float):
        return str(value)
    if isinstance(value, dict):
        indent = SEPARATOR * ((depth * DEFAULT_INDENT - 2) + DEFAULT_INDENT)
        lines = []
        for key, inner_value in value.items():
            formatted_value = format_string(inner_value, depth + 1)
            lines.append(f'{indent}{NONE}{key}: {formatted_value}')
        formatted_string = '\n'.join(lines)
        end_indent = SEPARATOR * depth * DEFAULT_INDENT
        return f'{{\n{formatted_string}\n{end_indent}}}'
    return f'{value}'


def make_stylish(diff, depth=1):
    indent = SEPARATOR * (depth * DEFAULT_INDENT - 2)
    lines = []
    for item in diff:
        key_name = item['name']
        old_value = format_string(item.get('old_value'), depth)
        new_value = format_string(item.get('new_value'), depth)
        action = item['status']
        if action == 'unchanged':
            current_value = format_string(item.get('value'), depth)
            lines.append(f'{indent}{NONE}{key_name}: {current_value}')
        elif action == 'changed':
            lines.append(f'{indent}{DELETE}{key_name}: {old_value}')
            lines.append(f'{indent}{ADD}{key_name}: {new_value}')
        elif action == 'deleted':
            lines.append(f'{indent}{DELETE}{key_name}: {old_value}')
        elif action == 'added':
            lines.append(f'{indent}{ADD}{key_name}: {new_value}')
        else:
            children = make_stylish(item.get('children'), depth + 1)
            lines.append(f'{indent}{NONE}{key_name}: {children}')
    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (depth * DEFAULT_INDENT - 4)

    return f'{{\n{formatted_string}\n{end_indent}}}'


def format_diff_stylish(data):
    return make_stylish(data)
