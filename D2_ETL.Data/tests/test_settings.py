from json import load

from Settings import settings, Files

data = {}


def setup_module():
    global data
    with open(Files.CONF, "r", encoding="utf-8") as file:
        data = load(file)


def test_api_key():
    assert data["ApiKey"] == settings.ApiKey
