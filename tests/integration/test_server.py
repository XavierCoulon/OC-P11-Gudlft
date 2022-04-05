from ... import server


class TestIntegrationClass:

	# @classmethod
	# def setup_class(cls):
	# 	server.clubs = clubs_dataset
	# 	server.competitions = competitions_dataset
	# 	server.clubs_booking = clubs_booking_dataset

	def test_load_clubs_and_log(self, client):
		server.clubs = server.load_json("tests/clubs_dataset")
		response = client.post("/show_summary", data={"email": "club7@gmail.com"}, follow_redirects=True)
		data = response.data.decode()
		assert response.status_code == 200
		assert f"Welcome, club7@gmail.com" in data

	def test_log_and_purchase(self, client):
		server.clubs = server.load_json("tests/clubs_dataset")
		server.competitions = server.load_json("tests/competitions_dataset")
		client.post("/show_summary", data={"email": "club7@gmail.com"}, follow_redirects=True)
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition 1", "club": "Club 7", "places": 1},
			follow_redirects=True
		)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Great-booking complete!" in data
