import pytest
from .. import server


@pytest.fixture()
def client():
    server.app.config["TESTING"] = True
    return server.app.test_client()


clubs_dataset = [
    {"name": "Club 1", "email": "club1@gmail.com", "points": "40"},
    {"name": "Club 2", "email": "club2@gmail.com", "points": "12"},
    {"name": "Club 3", "email": "club3@gmail.com", "points": "3"},
    {"name": "Club 4", "email": "club4@gmail.com", "points": "1"},
    {"name": "Club 5", "email": "club5@gmail.com", "points": "16"},
    {"name": "Club 6", "email": "club5@gmail.com", "points": "22"},
    ]

competitions_dataset = [
    {"name": "Competition 1", "date": "2023-10-22 13:30:00", "numberOfPlaces": "18"},
    {"name": "Competition 2", "date": "2023-10-22 13:30:00", "numberOfPlaces": "4"},
    {"name": "Competition 3", "date": "2023-10-22 13:30:00", "numberOfPlaces": "0"},
    {"name": "Competition 5", "date": "2023-10-22 13:30:00", "numberOfPlaces": "20"},
    {"name": "Competition 6", "date": "2020-10-22 13:30:00", "numberOfPlaces": "20"}
]

clubs_booking_dataset = {
    "Club 1": {"Competition 1": 0, "Competition 2": 0, "Competition 3": 0},
    "Club 2": {"Competition 1": 11, "Competition 2": 0, "Competition 3": 0},
    "Club 3": {"Competition 1": 0, "Competition 2": 0, "Competition 3": 0}
}

