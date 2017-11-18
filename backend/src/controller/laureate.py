import random

from backend.src.api_nobelprize import search_laureate_json
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

    def get_all_neighbours(self, id):
        laureate_info = search_laureate_json(id=id)[0]
        relevant_similarity = ['bornCountry', 'bornCity', 'gender']
        neighbours = []

        for field in relevant_similarity:
            dict = {field: laureate_info[field]}
            neighbours += search_laureate_json(**dict)

        prizes = laureate_info['prizes']
        neighbours += search_laureate_json()
        return neighbours

    def get_neighbours_json(self, id, limit):
        neighbours = self.get_all_neighbours(id)

        # TODO change random with something smarter
        return random.sample(neighbours, min(limit, len(neighbours)))