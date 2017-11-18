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