from src.util.requests import HTTPVerb, parse_response, web_request


ENDPOINT = "https://api.housecanary.com/v2/property/details"


def check_septic(address: str, zipcode: str) -> str:
    params = {"address": address, "zipcode": zipcode}
    response = web_request(ENDPOINT, HTTPVerb.Get, params=params)
    data = parse_response(response)

    if isinstance(data, str):
        return data

    return data["property/details"]["result"]["property"]["sewer"]
