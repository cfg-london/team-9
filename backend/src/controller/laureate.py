import random

from backend.src.api_nobelprize import search_laureate_json
from backend.src.api_nobelprize import search_prize_json
from backend.src.model.graph import Graph
from backend.src.shared.entity import Entity
from backend.src.shared.singleton import Singleton


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

        return laureates[0]

    def get_ids_from_laureates_list(self, laureates, field):
        return set((v['id'],field) for v in laureates)
        #return list({v['id']: v for v in laureates}.values())

    def get_graph(self, id, cnt_nodes):
        laureate = search_laureate_json(id=id)
        if not laureate:
            raise Exception('Invalid id')
        laureate = laureate[0]

        first_level_cnt = (cnt_nodes + 1) / 2
        lvl1 = self.get_neighbours_json(id, first_level_cnt)
        lvl1 = Entity.to_entities()

        graph = Graph()
        graph.add_nodes(lvl1)

        cnt_nodes -= first_level_cnt
        for neighbour in lvl1:
            if cnt_nodes <= 0:
                break

            n = random.randint(1, 2) # 1 or 2 neighbours?
            lvl2 = self.get_neighbours_json(neighbour['id'], n)
            graph.add_nodes(lvl2)
            graph.add_edges(neighbour, lvl2)

        return graph


    def get_all_neighbours_ids(self, id):
        laureate_info = search_laureate_json(id=id)[0] #list with only one element
        relevant_similarity = ['bornCountry', 'bornCity']

        similar_laureates_ids = set()

        for field in relevant_similarity:
            dict = {field: laureate_info[field]}
            neighbours = search_laureate_json(**dict)
            similar_laureates_ids |= self.get_ids_from_laureates_list(neighbours, field)

        laureate_prizes = laureate_info['prizes']
        relevant_prizes_similarity = ['category', 'year']
        sum=0
        for field in relevant_prizes_similarity:
            for laureate_prize in laureate_prizes:
                dict = {field: laureate_prize[field]}
                similar_prizes = search_prize_json(**dict)
                sum+=len(similar_prizes)
                for similar_prize in similar_prizes:
                    similar_laureates_ids|= set([(laureate['id'],field) for laureate in similar_prize['laureates']])
                #for id in similar_laureates_ids:
                #    neighbours += search_laureate_json(id=id)
        return similar_laureates_ids

    def get_neighbours_json(self, id, limit):
        neighbours = self.get_all_neighbours_ids(id)
        print(len(neighbours))
        # TODO change random with something smarter
        return random.sample(neighbours, min(limit, len(neighbours)))

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
