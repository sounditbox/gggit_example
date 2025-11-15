import requests


def fetch_data_from_url(url: str):
    return requests.get(url).json()
