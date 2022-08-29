import time
import pytest

import requests
import logging

log = logging.getLogger()

urls = [("https://www.aqa.science/admin/", 200),
        ("https://www.aqa.science/users/706/", 403),
        ("https://www.aqa.science", 200)]


def reporting():
    log.error("Something vet wrong")
    return f'Test failed with {requests.get(urls[0][0]).status_code}'


@pytest.mark.smoke
@pytest.mark.slow
def test_request():
    response = requests.get(urls[0][0])
    assert response.status_code == 200, f"Test response : {response.text}"


@pytest.mark.smoke
def test_request_second(fix_special):
    response = requests.get(urls[1][0])
    assert response.status_code == 200, f"Test response : {response.text}"


@pytest.mark.slow
@pytest.mark.smoke
def test_request_third():
    response = requests.get(urls[0][0])
    assert response.status_code == 200, f"Test response : {response.text}"


@pytest.mark.parametrize("url , code", urls)
def test_request_furth(url, code):
    response = requests.get(url)
    assert response.status_code == code, f"Test response : {response.text}"
