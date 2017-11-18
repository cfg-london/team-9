import json

import flask


class Graph:
    def __init__(self):
        pass

    def as_json(self):
        """Returns self graph as JSON representation"""

        # TODO
        return flask.jsonify({'key': 'value'})
