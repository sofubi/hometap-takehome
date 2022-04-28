from pytest_httpx import HTTPXMock

from tests.conftest import (
    FAILURE_RESPONSE,
    MOCK_URL,
    SUCCESS_RESPONSE,
    TEST_ENDPOINT,
    UNKOWN_RESPONSE,
)


def test_successful_response(httpx_mock: HTTPXMock, client):
    httpx_mock.add_response(
        url=MOCK_URL,
        json=SUCCESS_RESPONSE,
    )

    response = client.get(TEST_ENDPOINT)

    assert "Septic confirmed" in response.text


def test_failure_response(httpx_mock: HTTPXMock, client):
    httpx_mock.add_response(url=MOCK_URL, json=FAILURE_RESPONSE)

    response = client.get(TEST_ENDPOINT)

    assert "No septic" in response.text


def test_unknown_response(httpx_mock: HTTPXMock, client):
    httpx_mock.add_response(url=MOCK_URL, json=UNKOWN_RESPONSE)

    response = client.get(TEST_ENDPOINT)

    assert "Cannot determine septic" in response.text


def test_missing_params(client):
    response = client.get("/v1/septic?address=123+Main+St")

    assert "Both the address and zipcode are required" in response.text

    response = client.get("/v1/septic?zipcode=94132")

    assert "Both the address and zipcode are required" in response.text


def test_bad_params(client):
    response = client.get("/v1/septic?address=")

    assert response.status_code == 400
