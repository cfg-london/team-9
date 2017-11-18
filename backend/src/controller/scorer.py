import backend.src.controller.laureate


class Scorer:
    def __init__(self):
        pass

    def compute_laureate_score(self, id):
        len(backend.src.controller.laureate.LaureateController().get_all_neighbours_ids(id))