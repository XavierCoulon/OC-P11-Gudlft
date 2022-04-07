from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestFunctional:

	def test_main_user_story(self):
		driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		driver.get("http://127.0.0.1:5000")
		assert "GUDLFT Registration" in driver.title
		email = driver.find_element(By.NAME, "email")
		email.send_keys("main_use_case@gmail.com")
		email.submit()
		assert driver.find_element(By.TAG_NAME, "h2").text == "Welcome, main_use_case@gmail.com"

		# driver.implicitly_wait(10)
		# driver.find_element(by=By.XPATH, value="//a[@href='/book/Competition%20Main%20Use%20Case%201/Club%20Main%20Use%20Case']").click()
		# assert driver.find_element(By.TAG_NAME, "h2").text == "Competition Main Use Case 1"
		#
		# places = driver.find_element(By.NAME, "places")
		# places.send_keys("12")
		# places.submit()
		# assert driver.find_element(By.TAG_NAME, "li").text == "Great-booking complete!"
		#
		# driver.delete_all_cookies()
		driver.quit()


