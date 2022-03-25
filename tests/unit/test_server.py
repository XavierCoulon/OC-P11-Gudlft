

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
		data={"competition": "Spring Festival", "club": "Simply Lift", "places": 20},
		follow_redirects=True
	)
	data = response.data.decode()
	assert response.status_code == 200
	assert "Not enough points!" in data



