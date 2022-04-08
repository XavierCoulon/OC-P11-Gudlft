
class TestIntegrationClass:

	def test_log_and_purchase(self, client):
		response = client.post("/show_summary", data={"email": "log_and_purchase@gmail.com"}, follow_redirects=True)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Welcome, log_and_purchase@gmail.com" in data

		response = client.post(
			"/purchase_places",
			data={"competition": "Competition Log And Purchase", "club": "Club Log And Purchase", "places": 1},
			follow_redirects=True
		)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Great-booking complete!" in data
		assert "Points available: 0" in data

	def test_log_and_logout(self, client):
		response = client.post("/show_summary", data={"email": "log_and_purchase@gmail.com"}, follow_redirects=True)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Welcome, log_and_purchase@gmail.com" in data

		response = client.get("/logout", follow_redirects=True)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Welcome to the GUDLFT Registration Portal" in data
