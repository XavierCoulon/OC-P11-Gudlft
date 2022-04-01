from ..conftest import clubs_dataset
from ... import server


class TestLoginClass:

	@classmethod
	def setup_class(cls):
		server.clubs = clubs_dataset

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
		server.clubs = clubs_dataset
		response = client.post("/show_summary", data={"email": "club1@gmail.com"}, follow_redirects=True)
		data = response.data.decode()
		assert response.status_code == 200
		assert f"Welcome, club1@gmail.com" in data

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
