import random

from backend.src.api_nobelprize import search_laureate_json
from backend.src.api_nobelprize import search_prize_json
from backend.src.model.laureate import Laureate
from backend.src.shared.singleton import Singleton


class LaureateController(metaclass=Singleton):
    def __init__(self):
        pass

    def get_laureate(self, id):
        """
        :param id: Id of the laureate
        :return: Instance of Laureate corresponding to given id
        """

        # TODO: get actual laureate
        return Laureate()

    def get_ids_from_laureates_list(self, laureates, field):
        return set((v['id'],field) for v in laureates)
        #return list({v['id']: v for v in laureates}.values())

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

    """def get_neighbours_json(self, id, limit):
        neighbours = []
        neighbours_ids = self.get_neighbours_ids(id, limit)
        for id in neighbours_ids:
            neighbours += search_laureate_json(id=id)
        return neighbours
    """