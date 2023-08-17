import yaml
import requests
import json
import pytest

with open("config.yaml", "r") as f:
    d = yaml.safe_load(f)


def auth():
    data = {
        "username": d["username"],
        "password": d["password"]
    }
    res = requests.post(url=d["url_auth"], data=json.dumps(data))
    return res.json()["token"]


@pytest.fixture()
def create_posts():
    token = auth()
    headers = {
        "X-Auth-Token": token
    }
    data = {
        "title": "title",
        "description": "description",
        "content": "content",
    }
    res = requests.post(url=d["url_create"], headers=headers, data=data)
    return res.json()["description"]
