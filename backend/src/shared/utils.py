
def get_ids_from_laureates_list(laureates):
    return tuple(set((v['id']) for v in laureates))