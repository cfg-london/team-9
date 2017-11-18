import json
import os

from SPARQLWrapper import SPARQLWrapper

dir_path = os.path.dirname(os.path.realpath(__file__))

CONFIG = None
SPARKQL_CONNECTION = None

with open(os.path.join(dir_path, 'nobelprize_config.json')) as config_file:
    file_data = config_file.read()
    CONFIG = json.loads(file_data)
    SPARKQL_CONNECTION = SPARQLWrapper(CONFIG["sparql_endpoint"])