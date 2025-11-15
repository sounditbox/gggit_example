import requests


def fetch_json(url: str):
    return requests.get(url).json()
