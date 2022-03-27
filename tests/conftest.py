import pytest
import server


@pytest.fixture()
def client():
	server.app.config["TESTING"] = True
	return server.app.test_client()


@pytest.fixture()
def clubs():
	clubs = [
				{"name": "Club 1", "email": "club1@gmail.com", "points": "13"},
				{"name": "Club 2", "email": "club2@gmail.com", "points": "12"},
				{"name": "Club 3", "email": "club3@gmail.com", "points": "2"},
				{"name": "Club 4", "email": "club3@gmail.com", "points": "0"}
			]
	return clubs


@pytest.fixture()
def competitions():
	competitions = [
				{"name": "Competition 1", "date": "2020-03-27 10:00:00", "numberOfPlaces": "13"},
				{"name": "Competition 2", "date": "2020-10-22 13:30:00", "numberOfPlaces": "4"},
				{"name": "Competition 3", "date": "2020-10-22 13:30:00", "numberOfPlaces": "0"}
			]
	return competitions


@pytest.fixture()
def clubs_booking():
	clubs_booking = {
		"Club 1": {"Competition 1": 0, "Competition 2": 0, "Competition 3": 0},
		"Club 2": {"Competition 1": 11, "Competition 2": 0, "Competition 3": 0},
		"Club 3": {"Competition 1": 0, "Competition 2": 0, "Competition 3": 0}
	}
	return clubs_booking
