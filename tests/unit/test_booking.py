
class TestBookingClass:

	def test_book_club_competition_known(self, client):
		response = client.get("/book/Competition Known/Club Known")
		data = response.data.decode()
		assert response.status_code == 200
		assert "Places available: 18" in data

	def test_book_club_competition_not_found(self, client):
		response = client.get("/book/competition_not_existing/club_not_existing")
		data = response.data.decode()
		assert response.status_code == 200
		assert "Competition or club not found" in data

	def test_can_not_book_more_than_twelve_places_in_one_time(self, client):
		response = client.post(
			"/purchase_places",
			data={
				"competition": "Competition Can Not Book More Than 12",
				"club": "Club Can Not Book More Than 12", "places": 13},
			follow_redirects=True
		)

		data = response.data.decode()
		assert response.status_code == 200
		assert "Can not book more than 12 places!" in data

	def test_can_not_book_more_than_twelve_places_in_multiple_times(self, client):
		response = client.post(
			"/purchase_places",
			data={
				"competition": "Competition Can Not Book More Than 12",
				"club": "Club Can Not Book More Than 12", "places": 3},
			follow_redirects=True
		)

		data = response.data.decode()
		assert response.status_code == 200
		assert "Not possible, you have already booked" in data

	def test_enough_points_to_purchase(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition Enough Points", "club": "Club Enough Points", "places": 1},
			follow_redirects=True
		)
		data = response.data.decode()

		assert response.status_code == 200
		assert "Great-booking complete!" in data
		assert "Points available: 17" in data

	def test_not_enough_points_to_purchase(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition Not Enough Points", "club": "Club Not Enough Points", "places": 1},
			follow_redirects=True
		)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Not enough points!" in data

	def test_not_enough_places_available_in_competition(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition Not Enough Places", "club": "Club Enough Points", "places": 2},
			follow_redirects=True
		)

		data = response.data.decode()
		assert response.status_code == 200
		assert "Not enough places available in the competition!" in data

	def test_places_booked_update_competition_points(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition Places Updated", "club": "Club Places Updated", "places": 3},
			follow_redirects=True
		)

		data = response.data.decode()
		assert response.status_code == 200
		assert "Number of Places: 7" in data

	def test_can_not_book_places_on_post_dated_competition(self, client):
		response = client.post(
			"/purchase_places",
			data={"competition": "Competition Postdated", "club": "Club Postdated", "places": 1},
			follow_redirects=True
		)

		data = response.data.decode()
		assert response.status_code == 200
		assert "Not possible to book places on a post-dated competition" in data
