import json
import random
from urllib import parse, request as urllib_request

from backend.src.api_nobelprize import search_laureate_json, fetch_1_2_grade_concepts, find_relevant_resources
from backend.src.api_nobelprize import search_prize_json
from backend.src.model.graph import Graph
from backend.src.shared.cache import Cache
from backend.src.shared.entity import Entity
from backend.src.shared.singleton import Singleton


def _filter_keyword(word, possible_linked_words):
    if len(word) < 4:
        return False

    try:
        dec = int(word)
        return True
    except:
        return word in possible_linked_words


class LaureateController(metaclass=Singleton):
    def __init__(self):
        pass

    def get_laureate(self, id):
        """
        :param id: ID of the laureate
        :return: Instance of laureate corresponding to given id
        """
        laureates = search_laureate_json(id=id)

        if not laureates:
            raise Exception('Invalid id')

        picture_full_data = (self.get_pictures(laureates[0]['firstname']))['itemListElement'][0]['result']
        if 'image' in picture_full_data.keys():
            laureates[0]['picture'] = picture_full_data['image']['contentUrl']
        else:
            laureates[0]['picture'] = ''

        return laureates[0]

    def get_pictures(self, laureate_name):
        api_key = 'AIzaSyBjF9PR6yqceWYNacfqPLQyqV6snvbaroc'
        service_url = 'https://kgsearch.googleapis.com/v1/entities:search'

        params = {
            'query': laureate_name,
            'limit': 10,
            'indent': True,
            'key': api_key,
        }
        t = parse.urlencode(params)
        url = service_url + '?' + t
        request = urllib_request.urlopen(url)
        response = request.read()
        response = json.loads(response.decode('utf-8'))
        return response

    def get_ids_from_laureates_list(self, laureates, field, field_value):
        return set((v['id'], field, field_value) for v in laureates)
        # return list({v['id']: v for v in laureates}.values())

    def get_graph(self, id, cnt_nodes):
        laureate = search_laureate_json(id=id)
        if not laureate:
            raise Exception('Invalid id')
        laureate = Entity.to_entity(laureate[0], 'laureate', score=Cache().get_laureate_score(id))

        neighbours = self.get_neighbours_json(id, cnt_nodes)

        graph = Graph()
        graph.add_node(laureate)

        for temp in neighbours:
            temp2 = temp[0]
            id = temp2[0]

            neighbour = self.get_laureate(id)
            neighbour = Entity.to_entity(neighbour, type='laureate', score=Cache().get_laureate_score(id))

            edge_node = {'from': laureate['id'], 'to': neighbour['id'], 'category': temp2[1], 'value': temp2[2]}
            edge_node = Entity.to_entity(edge_node, type='edge_node')

            graph.add_node(edge_node)
            graph.add_node(neighbour)

            graph.add_edge(laureate, edge_node)
            graph.add_edge(edge_node, neighbour)

        return graph

    def get_all_neighbours_ids(self, id):
        laureate_info = search_laureate_json(id=id)
        if not laureate_info:
            raise Exception('Invalid id')

        laureate_info = laureate_info[0]
        relevant_similarity = ['bornCountry', 'bornCity']

        similar_laureates_ids = set()

        for field in relevant_similarity:
            dict = {field: laureate_info[field]}
            neighbours = search_laureate_json(**dict)
            similar_laureates_ids |= self.get_ids_from_laureates_list(neighbours, field, laureate_info[field])

        laureate_prizes = laureate_info['prizes']
        relevant_prizes_similarity = ['category', 'year']
        sum=0
        for field in relevant_prizes_similarity:
            for laureate_prize in laureate_prizes:
                dict = {field: laureate_prize[field]}
                similar_prizes = search_prize_json(**dict)
                sum+=len(similar_prizes)
                for similar_prize in similar_prizes:
                    similar_laureates_ids |= set([(laureate['id'], field, laureate_prize[field]) for laureate in similar_prize['laureates']])
                    # for id in similar_laureates_ids:
                    #    neighbours += search_laureate_json(id=id)
        return similar_laureates_ids

    def get_neighbours_json(self, id, limit):
        neighbours = self.get_all_neighbours_ids(id)

        random.seed(12345)

        neighbours = random.sample(neighbours, 3 * limit)

        print(neighbours)

        neighbours = [(n, self.compute_score(n[0])) for n in neighbours]
        neighbours.sort(key=lambda x: x[1], reverse=True)

        return neighbours[:min(limit, len(neighbours))]

    """
    def get_neighbours_json(self, id, limit):
        neighbours = []
        neighbours_ids = self.get_neighbours_ids(id, limit)
        for id in neighbours_ids:
            neighbours += search_laureate_json(id=id)
        return neighbours
    """

    def get_laureate_page(self, id):
        """
        :param id: Id of target laureate
        :return: A JSON representation of all information that should be contained in a laureate page
        """

        # TODO
        pass

    def find_relevant_links_dict(self, id, text):
        """
        Given a laureate and a text connected to him, find a mapping from relevant words to links.

        :param id: The id of the laureate.
        :param text: The text to find words into.
        :return: A mapping from relevant words to links.
        """
        possible_linked_words = fetch_1_2_grade_concepts(laureate_id=id)

        relevant_links = {}
        for line in text.split('\n'):
            for word in line.split(' '):
                word = word.strip('.')
                matches = list(filter(lambda x: (_filter_keyword(word,
                                                                 possible_linked_words)),
                                      possible_linked_words))

                if matches:
                    relevant_resources = find_relevant_resources(word, limit=1)
                    if len(relevant_resources) > 0:
                        # only one resource will be fetched
                        relevant_links[word] = relevant_resources[0]

        return json.dumps(relevant_links)

    def compute_score(self, id):
        return Cache().get_laureate_score(id)


