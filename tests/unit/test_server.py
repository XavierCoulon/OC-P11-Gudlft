from ... import server


class TestClass:

	load_dataset = [
		{"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
		{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
		{"name": "She Lifts","email": "kate@shelifts.co.uk", "points": "12"}
	]

	clubs_dataset = [
		{"name": "Club 1", "email": "club1@gmail.com", "points": "13"},
		{"name": "Club 2", "email": "club2@gmail.com", "points": "12"},
		{"name": "Club 3", "email": "club3@gmail.com", "points": "2"},
		{"name": "Club 4", "email": "club4@gmail.com", "points": "0"},
		{"name": "Club 5", "email": "club5@gmail.com", "points": "5"},
		{"name": "Club 6", "email": "club5@gmail.com", "points": "22"},
	]

	competitions_dataset = [
		{"name": "Competition 1", "date": "2023-10-22 13:30:00", "numberOfPlaces": "13"},
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

	@classmethod
	def setup_class(cls):
		server.clubs = cls.clubs_dataset
		server.competitions = cls.competitions_dataset
		server.clubs_booking = cls.clubs_booking_dataset

	def test_load_json(self):
		assert server.load_json("tests/unit/load_dataset") == self.load_dataset

	def test_index(self, client):
		response = client.get("/")
		data = response.data.decode()
		assert response.status_code == 200
		assert "Welcome to the GUDLFT Registration Portal" in data

	def test_login_email_unknown(self, client):
		response = client.post("/show_summary", data={"email": "email_unknown@gmail.com"}, follow_redirects=True)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Sorry, that email was not found." in data

	def test_login_email_known(self, client):
		response = client.post("/show_summary", data={"email": "club1@gmail.com"}, follow_redirects=True)
		data = response.data.decode()
		assert response.status_code == 200
		assert f"Welcome, club1@gmail.com" in data

	def test_book_club_competition_found(self, client):
		response = client.get(f"/book/{self.competitions_dataset[0]['name']}/{self.clubs_dataset[0]['name']}")
		data = response.data.decode()
		assert response.status_code == 200
		assert f"Places available: {self.competitions_dataset[0]['numberOfPlaces']}" in data

	def test_book_club_competition_not_found(self, client):
		response = client.get("/book/competition_not_existing/club_not_existing")
		data = response.data.decode()
		assert response.status_code == 200
		assert "Competition or club not found" in data

	def test_can_not_book_more_than_twelve_places_in_one_time(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition 1", "club": "Club 1", "places": 13},
			follow_redirects=True
		)

		data = response.data.decode()
		assert response.status_code == 200
		assert "Not possible, you have already booked" in data

	def test_can_not_book_more_than_twelve_places_in_multiple_times(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition 1", "club": "Club 2", "places": 3},
			follow_redirects=True
		)

		data = response.data.decode()
		assert response.status_code == 200
		assert "Not possible, you have already booked" in data

	def test_enough_points_to_purchase(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition 1", "club": "Club 3", "places": 1},
			follow_redirects=True
		)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Great-booking complete!" in data

	def test_not_enough_points_to_purchase(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition 1", "club": "Club 4", "places": 1},
			follow_redirects=True
		)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Not enough points!" in data

	def test_not_enough_places_available_in_competition(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition 3", "club": "Club 1", "places": 6},
			follow_redirects=True
		)

		data = response.data.decode()
		assert response.status_code == 200
		assert "Not enough places available in the competition!" in data

	def test_places_booked_update_competition_points(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition 5", "club": "Club 5", "places": 5},
			follow_redirects=True
		)

		data = response.data.decode()
		assert response.status_code == 200
		assert "Number of Places: 15" in data

	def test_can_not_book_places_on_post_dated_competition(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition 6", "club": "Club 5", "places": 5},
			follow_redirects=True
		)

		data = response.data.decode()
		assert response.status_code == 200
		assert "Not possible to book places on a post-dated competition" in data

	def test_display_clubs_points(self, client):
		response = client.get("/points")
		data = response.data.decode()
		assert response.status_code == 200
		assert "Club: Club 6 / points: 22" in data

	def test_logout(self, client):
		response = client.get("/logout", follow_redirects=True)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Welcome to the GUDLFT Registration Portal" in data
