import os
import json

THIS_DIR = os.path.dirname(__file__)
LOOKUP = json.load(open(os.path.join(THIS_DIR, 'data.json'), 'r'))


def get(value):
    """
    Accepts abbreviation of a MLB team and returns a list of official colors.
    """
    try:
        return LOOKUP[value]
    except KeyError:
        raise KeyError("The team you requested does not exist")
