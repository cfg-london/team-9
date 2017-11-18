import time

from backend.src.controller.scorer import Scorer
from backend.src.shared.singleton import Singleton


class Cache(metaclass=Singleton):
    CACHE_TIME = 24 * 60 * 60
    MAX_BEST_SIZE = 10

    def __init__(self):
        self.laureate_scores = {'id':{'update_time':None, 'score':None}}
        self.best = [] # TODO: implement as heap
        self.init()

    def get_laureate_score(self, id):
        temp = self.laureate_scores.get(id, None)
        if temp is None or temp['update_time'] < time.time() - Cache.CACHE_TIME:
            self.recompute_laureate_score(id)

        return self.laureate_scores[id]['score']

    def recompute_laureate_score(self, id):
        score = Scorer().compute_laureate_score(id)
        self.laureate_scores[id] = {'update_time':time.time(), 'score': score}

        if not self.best or score > self.best[0]['score']:
            new_entry = {'id': id, 'score': score}
            if len(self.best) >= Cache.MAX_BEST_SIZE:
                self.best[0] = new_entry
            else:
                self.best.append(new_entry)

        self.best.sort(key=lambda x: x['score'])

    def init(self):
        for id in range(0, 20, 2):
            self.recompute_laureate_score(id)

        print('Cache initialized')

