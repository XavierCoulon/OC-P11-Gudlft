import pytest
import server


@pytest.fixture()
def client():
	server.app.config["TESTING"] = True
	return server.app.test_client()


@pytest.fixture()
def email_unknown():
	return "email_unknown@gmail.com"


@pytest.fixture()
def email_known():
	return "admin@irontemple.com"


@pytest.fixture()
def clubs():
	clubs = {
		"clubs": [
			{"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
			{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
			{"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"}
		]
	}
	return clubs
