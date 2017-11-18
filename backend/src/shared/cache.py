import time

from backend.src.controller.scorer import Scorer
from backend.src.shared.singleton import Singleton


class Cache(metaclass=Singleton):
    CACHE_TIME = 24 * 60 * 60 # in seconds (24 hours)
    MAX_BEST_SIZE = 10
    PRECOMPUTED_IDS = (297, 26, 46, 202, 1, 39)

    def __init__(self):
        self.laureate_scores = {}
        self.best_laureates = [] # TODO: implement as heap if MAX_BEST_SIZE is required to be higher
        self.init()

    def get_laureate_score(self, id):
        temp = self.laureate_scores.get(id, None)
        if temp is None or temp['update_time'] < time.time() - Cache.CACHE_TIME:
            self.recompute_laureate_score(id)

        return self.laureate_scores[id]['score']

    def recompute_laureate_score(self, id):
        score = Scorer().compute_laureate_score(id)
        self.laureate_scores[id] = {'update_time':time.time(), 'score': score}

        if not self.best_laureates or score > self.best_laureates[0]['score']:
            # print(self.best_laureates)
            if id in (l['id'] for l in self.best_laureates):
                return

            new_entry = {'id': id, 'score': score}
            if len(self.best_laureates) >= Cache.MAX_BEST_SIZE:
                self.best_laureates[0] = new_entry
            else:
                self.best_laureates.append(new_entry)

        self.best_laureates.sort(key=lambda x: x['score'])

    def init(self):
        for id in Cache.PRECOMPUTED_IDS:
            self.recompute_laureate_score(id)

        # print(self.best_laureates)
        print('Cache initialized')

