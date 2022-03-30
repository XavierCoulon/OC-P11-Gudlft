import pytest
from .. import server


@pytest.fixture()
def client():
    server.app.config["TESTING"] = True
    #server.app.config["LIVESERVER_PORT"] = 8943
    return server.app.test_client()


@pytest.fixture()
def load_dataset():
    return[
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts","email": "kate@shelifts.co.uk", "points": "12"}
    ]

