from SPARQLWrapper import JSON

from .api_config import SPARKQL_CONNECTION

_SPARKQL_PREFIXES = """
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
PREFIX nobel: <http://data.nobelprize.org/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX yago: <http://yago-knowledge.org/resource/>
PREFIX viaf: <http://viaf.org/viaf/>
PREFIX meta: <http://www4.wiwiss.fu-berlin.de/bizer/d2r-server/metadata#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX d2r: <http://sites.wiwiss.fu-berlin.de/suhl/bizer/d2r-server/config.rdf#>
PREFIX dbpedia: <http://dbpedia.org/resource/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX map: <http://data.nobelprize.org/resource/#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX freebase: <http://rdf.freebase.com/ns/>
PREFIX dbpprop: <http://dbpedia.org/property/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
"""

_SPARKQL_CONCEPT_QUERY = """
SELECT DISTINCT ?link WHERE {
    ?subject ?predicate %s.
    ?subject rdfs:seeAlso ?link
}
LIMIT %s
"""


def _query_wo_prefix(statement):
    statement = _SPARKQL_PREFIXES + statement
    SPARKQL_CONNECTION.setQuery(statement)
    SPARKQL_CONNECTION.setReturnFormat(JSON)
    return SPARKQL_CONNECTION.query().convert()


def find_relevant_resources(concept, limit=1):
    statement = _SPARKQL_CONCEPT_QUERY % (concept, limit)

    result = _query_wo_prefix(statement)
    result_list = result["results"]["bindings"]

    return list(map(lambda x: x["link"]["value"], result_list))


_SPARKQL_1_2_NEIGHBOURS = """
SELECT * {
 {
  SELECT DISTINCT ?target_object WHERE {
    <http://data.nobelprize.org/resource/laureate/%s> ?predicate ?target_object
  }
 }
 UNION {
  SELECT DISTINCT ?target_object WHERE {
    <http://data.nobelprize.org/resource/laureate/%s> ?predicate ?object.
    ?object ?object_predicate ?target_object
  }
 }
}
"""


def fetch_1_2_grade_concepts(laureate_id):
    result = _query_wo_prefix(_SPARKQL_1_2_NEIGHBOURS % (laureate_id, laureate_id))
    result_list = result["results"]["bindings"]

    return list(map(lambda x: x["target_object"]["value"], result_list))
