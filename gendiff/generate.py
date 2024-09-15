def to_unchanged(key, value):
    return {
        'status': 'unchanged',
        'name': key,
        'value': value
    }


def to_add(key, value):
    return {
        'status': 'added',
        'name': key,
        'new_value': value
    }


def to_delete(key, value):
    return {
        'status': 'deleted',
        'name': key,
        'old_value': value
    }


def to_changed(key, value1, value2):

    return {
        'status': 'changed',
        'name': key,
        'old_value': value1,
        'new_value': value2
    }


def to_nested(key, value1, value2):
    return {
        'status': 'nested',
        'name': key,
        'children': generate(value1, value2)
    }


def generate(data1, data2):
    all_keys = data1.keys() | data2.keys()
    added = data2.keys() - data1.keys()
    deleted = data1.keys() - data2.keys()
    diff = []
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(to_nested(key, value1, value2))
        elif key in added:
            diff.append(to_add(key, value2))
        elif key in deleted:
            diff.append(to_delete(key, value1))
        elif value1 != value2:
            diff.append(to_changed(key, value1, value2))
        else:
            diff.append(to_unchanged(key, value1))
    return sorted(diff, key=lambda x: x['name'])
