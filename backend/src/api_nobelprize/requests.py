import json
from urllib import parse, request as urllib_request
from .api_config import CONFIG


def search_laureate_json(**kwargs):
    """
    This method allows you to find and list all Nobel Laureates.

    One Nobel Laureate may be awarded more than one Nobel Prize.
    To find the corresponding Nobel Prize(s) that has been awarded to a
    specific Laureate, use the ID parameter that corresponds to Laureate ID
    parameter in the method "prizes".


    :param format: Output format (csv or json).
    :type format: str
    :param id: ID of a unique Nobel Laureate.
    :type id: int
    :param bornCountry: Search for laureates by country of birth.
    :type bornCountry: str
    :param bornCountryCode: Search for laureates by country of birth
                            based on country code.
    :type bornCountryCode: str
    :param bornCity: Search for laureates by city of birth.
    :type bornCity: str
    :param bornCountry: Search for laureates by country where they died.
    :type bornCountry: str
    :param diedCountryCode: Search for laureates by country where they
                            died based on country code.
    :type diedCountryCode: str
    :param diedCity: Search for laureates by city where they died.
    :type diedCity: str
    :param bornDate: Search for laureates by year (YYYY) or
                     date (YYYYMMDD) of birth.
    :type bornDate: str
    :param bornDateTo: End of search for laureaes by year (YYYY) or
                       date (YYYYMMDD) of birth. Requires the bornDate
                       param to be set.
    :type bornDateTo: str
    :param diedDate: Search for laureaes by year (YYYY) or
                     date (YYYYMMDD) of death.
    :type diedDate: str
    :param diedDateTo: End of search for laureaes by year (YYYY) or
                       date (YYYYMMDD) of death. Requires the diedDate
                       param to be set.
    :type diedDateTo: str
    :param motivation: Search for laureates based on the motivation of
                       receiving the prize.
    :type motivation: str
    :param gender: Search for laureates by gender.
                   Possible values are: All, Male, Female or Organization.
    :type gender: str
    :param affiliation: Search for laureates by affiliaton.
    :type affiliation: str
    :return:
    """
    parameters = parse.urlencode(kwargs)
    request = urllib_request.urlopen(
        "%s?%s" % (CONFIG["laureate_endpoint_json"], parameters)
    )

    # Read and load as json
    # TODO: Error checking
    response = request.read()
    if isinstance(response, bytes):
        response = response.decode('UTF-8')
    response_json = json.loads(response)

    # TODO: Error checking
    laureates = response_json["laureates"]
    return laureates
