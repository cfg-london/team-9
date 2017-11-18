import random

from backend.src.api_nobelprize import search_laureate_json, fetch_1_2_grade_concepts, find_relevant_resources
from backend.src.api_nobelprize import search_prize_json
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

    def get_ids_from_laureates_list(self, laureates, field, field_value):
        return set((v['id'],field, field_value) for v in laureates)
        #return list({v['id']: v for v in laureates}.values())

    def get_all_neighbours_ids(self, id):
        laureate_info = search_laureate_json(id=id)[0] #list with only one element
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
                    similar_laureates_ids|= set([(laureate['id'],field, laureate_prize[field]) for laureate in similar_prize['laureates']])
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
                matches = list(filter(lambda x: word in x, possible_linked_words))

                if matches:
                    # only one resource will be fetched
                    relevant_links[word] = find_relevant_resources(word, limit=1)[0]
        return relevant_links




