import random
import json
from backend.src.api_nobelprize import search_laureate_json

def getAllNeibghours(id):
    laureate_info = search_laureate_json(id=id)[0]
    relevant_similarity = ['bornCountry', 'bornCity', 'gender']
    neighbours = []
    for field in relevant_similarity:
        dict = {field:laureate_info[field]}
        neighbours+=search_laureate_json(**dict)
    prizes = laureate_info['prizes']
    neighbours+=search_laureate_json()
    return neighbours

def getNeibghours(name, number):
    neibghours = getAllNeibghours(name)
    #TODO change random with something smarter
    return random.sample(neibghours, number)

