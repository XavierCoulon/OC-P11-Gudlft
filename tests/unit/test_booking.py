from ..conftest import clubs_dataset, competitions_dataset, clubs_booking_dataset
from ... import server


class TestBookingClass:

	@classmethod
	def setup_class(cls):
		server.clubs = clubs_dataset
		server.competitions = competitions_dataset
		server.clubs_booking = clubs_booking_dataset

	def test_book_club_competition_found(self, client):
		response = client.get(f"/book/{competitions_dataset[0]['name']}/{clubs_dataset[0]['name']}")
		data = response.data.decode()
		assert response.status_code == 200
		assert f"Places available: {competitions_dataset[0]['numberOfPlaces']}" in data

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
