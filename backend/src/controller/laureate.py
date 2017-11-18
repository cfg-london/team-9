import random

from backend.src.api_nobelprize import search_laureate_json
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

    def get_laureate_page(self, id):
        """
        :param id: Id of target laureate
        :return: A JSON representation of all information that should be contained in a laureate page
        """

        # TODO
        pass
