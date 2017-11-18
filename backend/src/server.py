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


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

class HomepageGraph(Resource):
    def get(self):
        """Get a random homepage graph as json"""

        graph = Graph()  # TODO: get actual correct graph
        return graph.as_json()


class Prize(Resource):
    def get(self, year, category):
        return PrizeController().get_prize(int(year), category)


class PrizePage(Resource):
    def get(self, year, category):
        return PrizeController().get_prize_page(int(year), category)


class Laureate(Resource):
    def get(self, id):
        return LaureateController().get_laureate(int(id))


class LaureatePage(Resource):
    def get(self, id):
        return LaureateController().get_laureate_page(int(id))


class LaureateNeighbours(Resource):
    def get(self, id, limit):
        return LaureateController().get_neighbours_json(int(id), int(limit))


api.add_resource(HomepageGraph, "/homepage_graph")

api.add_resource(Prize, "/prize/year/<year>/category/<category>")
api.add_resource(PrizePage, "/prize/page/year/<year>/category/<category>")

api.add_resource(Laureate, "/laureate/id/<id>")
api.add_resource(LaureatePage, "/laureate/page/id/<id>")
api.add_resource(LaureateNeighbours, "/laureate/neighbours/id/<id>/limit/<limit>")

app.run(debug=True)
