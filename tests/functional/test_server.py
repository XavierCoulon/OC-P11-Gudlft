from ... import server

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class TestFunctional():

	def test_main_user_story(self):
		driver.get("http://127.0.0.1:5000")
		assert "GUDLFT Registration" in driver.title
		email = driver.find_element(By.NAME, "email")
		email.send_keys("john@simplylift.co")
		email.submit()
		assert driver.find_element(By.TAG_NAME, "h2").text == "Welcome, john@simplylift.co"
		driver.quit()

