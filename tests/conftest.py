import pytest
from .. import server


@pytest.fixture()
def client():
    server.app.config["TESTING"] = True
    return server.app.test_client()


clubs_booking_dataset = {
    "Club 1": {"Competition 1": 0, "Competition 2": 0, "Competition 3": 0},
    "Club 2": {"Competition 1": 11, "Competition 2": 0, "Competition 3": 0},
    "Club 3": {"Competition 1": 0, "Competition 2": 0, "Competition 3": 0}
}

