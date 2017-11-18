import time

import pickle

from backend.src.api_nobelprize import search_laureate_json
from backend.src.controller.scorer import Scorer
from backend.src.shared.singleton import Singleton
from backend.src.shared.utils import get_ids_from_laureates_list


class Cache(metaclass=Singleton):
    CACHE_TIME = 24 * 60 * 60 # in seconds (24 hours)
    MAX_BEST_SIZE = 8

    LONDON_IDS = get_ids_from_laureates_list(search_laureate_json(bornCity='London'))[:10]

    PRECOMPUTED_IDS = (297, 26, 46, 202, 1, 39)
    PRECOMPUTED_IDS += LONDON_IDS


    def __init__(self):
        self.laureate_scores = {}
        self.best_laureates = [] # TODO: implement as heap if MAX_BEST_SIZE is required to be higher
        self.init()

    def get_laureate_score(self, id):
        temp = self.laureate_scores.get(id, None)
        if temp is None:
            self.recompute_laureate_score(id)

        return self.laureate_scores[id]['score']

    def recompute_laureate_score(self, id):
        score = Scorer().compute_laureate_score(id)
        self.laureate_scores[id] = {'update_time':time.time(), 'score': score}

        # print(self.best_laureates)
        # print(id)
        # print(score)
        if not self.best_laureates or score > self.best_laureates[0]['score'] or len(self.best_laureates) < Cache.MAX_BEST_SIZE:
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
        try:
            f = open('cache.ser', 'rb')
            x = pickle.load(f)
            self.__dict__ = x.__dict__
            f.close()
            print('Loaded cache')

        except Exception as e:
            print('No serialized cache found')
            for id in Cache.PRECOMPUTED_IDS:
                self.recompute_laureate_score(id)

        IMPROVE = False
        if IMPROVE:
            for id in range(990, 2000):
                print(id)

                try:
                    self.get_laureate_score(id)
                except Exception:
                    pass

                print('done id {}'.format(id))
                if id % 10 == 1:
                    f = open('cache.ser', 'wb')
                    pickle.dump(self, f)
                    f.close()

                    print('Cache dumped, {}'.format(id))


        # print(self.best_laureates)
        # print('Cache initialized')

