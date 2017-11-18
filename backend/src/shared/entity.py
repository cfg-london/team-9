import json


class Entity:
    @staticmethod
    def to_entity(entity, type):

        ans = json.loads(json.dumps({'id':'', 'type':'', 'value':''}))

        ans['type'] = type
        ans['value'] = entity

        if type == 'laureate':
            ans['id'] = 'laureate_' + entity['id']
        elif type == 'laureate_page':
            ans['id'] = 'laureate_page_' + entity['id']
        elif type == 'prize':
            ans['id'] = 'prize_{}_{}'.format(entity['year'], entity['category'])
        elif type == 'prize_page':
            ans['id'] = 'prize_page_{}_{}'.format(entity['year'], entity['category'])
        elif type == 'graph':
            ans['id'] = 'graph_{}'.format(entity['id'])
        elif type == 'edge':
            ans['id'] = '' # irrelevant, not used, but required by generalization
        else:
            raise Exception('Invalid entity type')

        return ans