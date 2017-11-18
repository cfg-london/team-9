import json


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def to_json(self):
        return json.loads(json.dumps({'nodes':self.nodes, 'edges':self.edges}))

    def add_nodes(self, nodes):
        for node in nodes:
            if node['id'] not in self.nodes:
                self.nodes[node['id']] = node

    def add_node(self, node):
        if node['id'] not in self.nodes:
            self.nodes[node['id']] = node

    def add_edge(self, fr, to):
        self.edges.append(json.loads(json.dumps({'from':fr['id'], 'to':to['id']})))