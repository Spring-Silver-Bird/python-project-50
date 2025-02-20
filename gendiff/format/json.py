import json

IND = 4


def format_diff_json(diff):
    return json.dumps(diff, sort_keys=True, indent=IND, separators=(',', ': '))
