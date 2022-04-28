from enum import auto
from typing import Any, Dict, Optional

import httpx
from strenum import UppercaseStrEnum


class HTTPVerb(UppercaseStrEnum):
    Get = auto()
    Post = auto()
    Put = auto()
    Patch = auto()
    Delete = auto()


def web_request(
    url: str,
    verb: HTTPVerb,
    params: Optional[Dict[str, Any]] = None,
    payload: Optional[Dict[str, Any]] = None,
) -> httpx.Response:
    with httpx.Client() as client:
        request = client.build_request(verb, url, params=params, json=payload)
        response = client.send(request)

    return response


def parse_response(response: httpx.Response) -> str | Dict[str, Any]:
    if response.status_code not in range(200, 299):
        return response.reason_phrase

    body = response.json()[0]

    response.close()

    return body
