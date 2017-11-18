import json


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def to_json(self):
        return json.loads(json.dumps({'nodes':[v for v in self.nodes.values()], 'edges':self.edges}))

    def add_nodes(self, nodes):
        for node in nodes:
            if node['id'] not in self.nodes:
                self.nodes[node['id']] = node

    def add_node(self, node):
        if node['id'] not in self.nodes:
            self.nodes[node['id']] = node

    def add_edge(self, fr, to):
        new_edge = json.loads(json.dumps({'from':fr['id'], 'to':to['id']}))
        if new_edge in self.edges:
            return
        self.edges.append(new_edge)