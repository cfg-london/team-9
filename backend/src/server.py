import json
import random

from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from backend.src.controller.laureate import LaureateController
from backend.src.controller.prize import PrizeController
from backend.src.model.graph import Graph
from backend.src.shared.cache import Cache

from backend.src.shared.entity import Entity

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("workflow", type=dict)


@app.route('/')
def index():
    return 'Index!'


@app.after_request
def after_request(response):
    """
    Adds headers to allow redirect to different port
    """

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# ------ Homepage graph ------------------------------------------------

class HomepageGraph(Resource):
    def get(self):
        """Get a random homepage graph as json"""
        return LaureateController().get_graph(Cache().best_laureates[0]['id'], 6).to_json()

# ------ Prizes --------------------------------------------------

class Prize(Resource):
    def get(self, year, category):
        prize = PrizeController().get_prize(int(year), category)
        return Entity.to_entity(prize, type='prize')


class PrizePage(Resource):
    def get(self, year, category):
        page = PrizeController().get_prize_page(int(year), category)
        return Entity.to_entity(page, type='prize_page')


# ------ Laureates --------------------------------------------------

class Laureate(Resource):
    def get(self, id):
        l = LaureateController().get_laureate(int(id))
        return Entity.to_entity(l, type='laureate', score=Cache().get_laureate_score(id))


class LaureatePage(Resource):
    def get(self, id):
        page = LaureateController().get_laureate_page(int(id))
        return Entity.to_entity(page, type='laureate_page')


class LaureateNeighbours(Resource):
    def get(self, id, limit):
        # print(LaureateController().get_neighbours_json(int(id), int(limit)))
        ids = [n[0][0] for n in LaureateController().get_neighbours_json(int(id), int(limit))]
        return json.loads(json.dumps([Entity.to_entity(LaureateController().get_laureate(id), 'laureate', Cache().get_laureate_score(id)) for id in ids]))

class LaureateGraph(Resource):
    def get(self, id, limit):
        return LaureateController().get_graph(int(id), int(limit)).to_json()

# ------ Best laureates --------------------------------------------------

class BestLaureates(Resource):
    def get(self):
        laureates = (LaureateController().get_laureate(laur['id']) for laur in Cache().best_laureates)
        entities = [Entity.to_entity(laur, 'laureate', best['score']) for (laur, best) in zip(laureates, Cache().best_laureates) ]
        return json.loads(json.dumps(entities))

# ------ Relevant links --------------------------------------------------

class RelevantLinks(Resource):
    def post(self):
        id = request.form['id']
        text = request.form['text']

        return LaureateController().find_relevant_links_dict(int(id), text)



api.add_resource(HomepageGraph, "/homepage_graph")

api.add_resource(Prize, "/prize/year/<year>/category/<category>")
api.add_resource(PrizePage, "/prize/page/year/<year>/category/<category>")

api.add_resource(Laureate, "/laureate/id/<id>")
api.add_resource(LaureatePage, "/laureate/page/id/<id>")
api.add_resource(LaureateNeighbours, "/laureate/neighbours/id/<id>/limit/<limit>")
api.add_resource(LaureateGraph, "/laureate/graph/id/<id>/limit/<limit>")


api.add_resource(BestLaureates, "/laureate/best")

api.add_resource(RelevantLinks, "/laureate/relevant_links")

Cache() # Initialize cache
app.run(debug=True)
