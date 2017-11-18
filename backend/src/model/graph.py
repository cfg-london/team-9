import json


class Graph:
    def __init__(self):
        pass

    def to_json(self):
        return json.loads(json.dumps({}))