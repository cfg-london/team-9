import json


class Entity:
    @staticmethod
    def to_entity(entity, type):

        ans = json.loads(json.dumps({'id':'', 'type':'', 'label':'', 'value':''}))

        ans['type'] = type
        ans['value'] = entity

        if type == 'laureate':
            ans['id'] = 'laureate_' + entity['id']
            ans['label'] = '{} {}'.format(entity['firstname'], entity['surname'])
        elif type == 'laureate_page':
            ans['id'] = 'laureate_page_' + entity['id']
            ans['label'] = '{} {}'.format(entity['firstname'], entity['surname'])
        elif type == 'prize':
            ans['id'] = 'prize_{}_{}'.format(entity['year'], entity['category'])

            # TODO: label
            # ans['label'] = '{} {}'.format(entity['firstname'], entity['surname'])
        elif type == 'prize_page':
            ans['id'] = 'prize_page_{}_{}'.format(entity['year'], entity['category'])
            # TODO: label
        elif type == 'graph':
            ans['id'] = 'graph_{}'.format(entity['id'])
            # TODO: label
        elif type == 'edge_node':
            ans['id'] = '{}_{}_{}_{}'.format(entity['from'], entity['to'], entity['category'], entity['value'])
            ans['label'] = '{}: {}'.format(entity['category'], entity['value'])
        else:
            raise Exception('Invalid entity type')

        return ans