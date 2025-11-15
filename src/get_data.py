import requests


def fetch_JSON_from_url(url: str):
    return requests.get(url).json()
