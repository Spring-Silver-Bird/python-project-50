import json


def format_diff_json(diff):
    return json.dumps(diff, sort_keys=True, indent=4, separators=(',', ': '))
