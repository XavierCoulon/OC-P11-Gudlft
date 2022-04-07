
class TestLoginClass:

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
		response = client.post("/show_summary", data={"email": "email_known@gmail.com"}, follow_redirects=True)
		data = response.data.decode()
		assert response.status_code == 200
		assert f"Welcome, email_known@gmail.com" in data

	def test_display_clubs_points(self, client):
		response = client.get("/points")
		data = response.data.decode()
		assert response.status_code == 200
		assert "Club: Display Points 10 / points: 10" in data

	def test_logout(self, client):
		response = client.get("/logout", follow_redirects=True)
		data = response.data.decode()
		assert response.status_code == 200
		assert "Welcome to the GUDLFT Registration Portal" in data
