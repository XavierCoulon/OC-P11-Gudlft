from ... import server

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class TestFunctional:

	# clubs_dataset = [
	# 	{"name": "Club 1", "email": "club1@gmail.com", "points": "13"},
	# 	{"name": "Club 2", "email": "club2@gmail.com", "points": "12"},
	# 	{"name": "Club 3", "email": "club3@gmail.com", "points": "2"},
	# 	{"name": "Club 4", "email": "club4@gmail.com", "points": "0"},
	# 	{"name": "Club 5", "email": "club5@gmail.com", "points": "5"},
	# 	{"name": "Club 6", "email": "club5@gmail.com", "points": "22"},
	# ]
	#
	# @classmethod
	# def setup_class(cls):
	# 	server.clubs = cls.clubs_dataset

	def test_main_user_story(self):
		driver.get("http://127.0.0.1:5000")
		assert "GUDLFT Registration" in driver.title
		email = driver.find_element(By.NAME, "email")
		email.send_keys("john@simplylift.co")
		email.submit()
		assert driver.find_element(By.TAG_NAME, "h2").text == "Welcome, john@simplylift.co"
		driver.quit()


# class TestFunctionalTest:
#
# 	clubs_dataset = [
# 		{"name": "Club 1", "email": "club1@gmail.com", "points": "13"},
# 		{"name": "Club 2", "email": "club2@gmail.com", "points": "12"},
# 		{"name": "Club 3", "email": "club3@gmail.com", "points": "2"},
# 		{"name": "Club 4", "email": "club4@gmail.com", "points": "0"},
# 		{"name": "Club 5", "email": "club5@gmail.com", "points": "5"},
# 		{"name": "Club 6", "email": "club5@gmail.com", "points": "22"},
# 	]
#
# 	@classmethod
# 	def setup_class(cls):
# 		server.clubs = cls.clubs_dataset
# 		print(server.clubs)
#
# 	def test_main_user_story(self):
# 		driver.get("http://127.0.0.1:5000")
# 		assert "GUDLFT Registration" in driver.title
# 		email = driver.find_element(By.NAME, "email")
# 		print(self.clubs_dataset[0]["email"])
# 		print(server.clubs)
# 		email.send_keys(self.clubs_dataset[0]["email"])
# 		#email.send_keys("john@simplylift.co")
# 		email.submit()
# 		#assert driver.find_element(By.TAG_NAME, "h2").text == "Welcome, john@simplylift.co"
# 		assert driver.find_element(By.TAG_NAME, "h2").text == "Welcome, club1@gmail.com"
#
# 		driver.quit()
