from server import clubs_booking


def test_login_email_unknown(client, email_unknown):
	response = client.post("/showSummary", data={"email": email_unknown}, follow_redirects=True)
	data = response.data.decode()
	assert response.status_code == 200
	assert "Sorry, that email was not found." in data


def test_login_email_known(client, email_known):
	response = client.post("/showSummary", data={"email": email_known}, follow_redirects=True)
	data = response.data.decode()
	assert response.status_code == 200
	assert f"Welcome, {email_known}" in data


def test_not_enough_points_to_purchase(client):
	response = client.post(
		"/purchasePlaces",
		data={"competition": "Spring Festival", "club": "Iron Temple", "places": 5},
		follow_redirects=True
	)
	data = response.data.decode()
	assert response.status_code == 200
	assert "Not enough points!" in data


def test_enough_points_to_purchase(client):
	response = client.post(
		"/purchasePlaces",
		data={"competition": "Spring Festival", "club": "Iron Temple", "places": 4},
		follow_redirects=True
	)
	data = response.data.decode()
	assert response.status_code == 200
	assert "Great-booking complete!" in data


def test_can_not_book_more_than_twelve_places_in_one_time(client):
	clubs_booking["Simply Lift"] = {"Spring Festival": 0}
	response = client.post(
		"/purchasePlaces",
		data={"competition": "Spring Festival", "club": "Simply Lift", "places": 13},
		follow_redirects=True
	)

	data = response.data.decode()
	assert response.status_code == 200
	assert "Not possible, you have already booked" in data


def test_can_not_book_more_than_twelve_places_in_multiple_times(client):
	clubs_booking["Simply Lift"] = {"Spring Festival": 0}
	client.post(
		"/purchasePlaces",
		data={"competition": "Spring Festival", "club": "Simply Lift", "places": 7},
		follow_redirects=True
	)
	response = client.post(
		"/purchasePlaces",
		data={"competition": "Spring Festival", "club": "Simply Lift", "places": 6},
		follow_redirects=True
	)

	data = response.data.decode()
	assert response.status_code == 200
	assert "Not possible, you have already booked" in data


