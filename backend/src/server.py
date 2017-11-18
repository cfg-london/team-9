from flask import Flask
from flask_restful import Api, Resource, reqparse

from backend.src.controller.laureate import LaureateController
from backend.src.controller.prize import PrizeController
from backend.src.model.graph import Graph

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("workflow", type=dict)


@app.route('/')
def index():
    return 'Index!'


# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers',
#                          'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response

class HomepageGraph(Resource):
    def get(self):
        """Get a random homepage graph as json"""

        graph = Graph()  # TODO: get actual correct graph
        return graph.as_json()


class PrizePage(Resource):
    def get(self, year, category):
        return PrizeController().get_prize(int(year), category).as_json()


class LaureatePage(Resource):
    def get(self, id):
        return LaureateController().get_laureate(int(id))

class LaureateNeighbours(Resource):
    def get(self, id, limit):
        return LaureateController().get_neighbours_json(int(id), int(limit))

api.add_resource(HomepageGraph, "/homepage_graph")
api.add_resource(PrizePage, "/prize/year/<year>/category/<category>")
api.add_resource(LaureatePage, "/laureate/id/<id>")
api.add_resource(LaureateNeighbours, "/laureate/neighbours/id/<id>/limit/<limit>")

# api.add_resource(WorkflowItem, "/users/<user_id>/workflows/<workflow_id>")
# api.add_resource(WorkflowStart, "/users/<user_id>/workflows/<workflow_id>/start")
# api.add_resource(WorkflowInterrupt, "/users/<user_id>/workflows/<workflow_id>/interrupt")
# api.add_resource(TaskList, "/users/<user_id>/tasks")
# api.add_resource(TaskItem, "/users/<user_id>/tasks/<workflow_id>", "/users/<user_id>/tasks/<workflow_id>/<task_id>")
# api.add_resource(ResetDB, "/resetDB")
# api.add_resource(SelectAction, "/users/<user_id>/next-action/<workflow_id>/<next_node>")

app.run(debug=True)
