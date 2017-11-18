import json


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def to_json(self):
        return json.loads(json.dumps({}))

    def add_nodes(self, nodes):
        for node in nodes:
            if node['id'] not in self.nodes:
                self.nodes[node['id']] = node