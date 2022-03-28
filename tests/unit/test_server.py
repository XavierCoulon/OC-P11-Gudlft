import server


def test_login_email_unknown(client, clubs):
	server.clubs = clubs
	response = client.post("/showSummary", data={"email": "email_unknown@gmail.com"}, follow_redirects=True)
	data = response.data.decode()
	assert response.status_code == 200
	assert "Sorry, that email was not found." in data


def test_login_email_known(client, clubs):
	server.clubs = clubs
	response = client.post("/showSummary", data={"email": "club1@gmail.com"}, follow_redirects=True)
	data = response.data.decode()
	assert response.status_code == 200
	assert f"Welcome, club1@gmail.com" in data


def test_can_not_book_more_than_twelve_places_in_one_time(client, clubs, competitions, clubs_booking):
	server.clubs = clubs
	server.competitions = competitions
	server.clubs_booking = clubs_booking
	response = client.post(
		"/purchasePlaces",
		data={"competition": "Competition 1", "club": "Club 1", "places": 13},
		follow_redirects=True
	)

	data = response.data.decode()
	assert response.status_code == 200
	assert "Not possible, you have already booked" in data


def test_can_not_book_more_than_twelve_places_in_multiple_times(client, clubs, competitions, clubs_booking):
	server.clubs = clubs
	server.competitions = competitions
	server.clubs_booking = clubs_booking
	response = client.post(
		"/purchasePlaces",
		data={"competition": "Competition 1", "club": "Club 2", "places": 3},
		follow_redirects=True
	)

	data = response.data.decode()
	assert response.status_code == 200
	assert "Not possible, you have already booked" in data


def test_enough_points_to_purchase(client, clubs, competitions):
	server.clubs = clubs
	server.competitions = competitions
	response = client.post(
		"/purchasePlaces",
		data={"competition": "Competition 1", "club": "Club 3", "places": 1},
		follow_redirects=True
	)
	data = response.data.decode()
	assert response.status_code == 200
	assert "Great-booking complete!" in data


def test_not_enough_points_to_purchase(client, clubs, competitions):
	server.clubs = clubs
	server.competitions = competitions
	response = client.post(
		"/purchasePlaces",
		data={"competition": "Competition 1", "club": "Club 4", "places": 1},
		follow_redirects=True
	)
	data = response.data.decode()
	assert response.status_code == 200
	assert "Not enough points!" in data


def test_not_enough_places_available_in_competition(client, clubs, clubs_booking, competitions):
	server.clubs = clubs
	server.competitions = competitions
	server.clubs_booking = clubs_booking

	response = client.post(
		"/purchasePlaces",
		data={"competition": "Competition 3", "club": "Club 1", "places": 6},
		follow_redirects=True
	)

	data = response.data.decode()
	assert response.status_code == 200
	assert "Not enough places available in the competition!" in data


def test_places_booked_update_competition_points(client, clubs, clubs_booking, competitions):
	server.clubs = clubs
	server.competitions = competitions
	server.clubs_booking = clubs_booking

	response = client.post(
		"/purchasePlaces",
		data={"competition": "Competition 5", "club": "Club 5", "places": 5},
		follow_redirects=True
	)

	data = response.data.decode()
	assert response.status_code == 200
	assert "Number of Places: 15" in data
