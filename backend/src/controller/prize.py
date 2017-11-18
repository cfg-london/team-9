from backend.src.model.prize import Prize
from backend.src.shared.singleton import Singleton


class PrizeController(metaclass=Singleton):
    def __init__(self):
        pass

    def get_prize(self, year, category):
        """
        :param year: The year of the prize
        :param category: The category of the prize
        :return: A Prize instance corresponding to the year and category given
        """

        # TODO: return actual correct prize
        return Prize()
