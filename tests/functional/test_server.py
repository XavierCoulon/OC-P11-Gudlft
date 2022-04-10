from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestFunctional:
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

	def get_link_and_click(self, href):
		return self.driver.find_element(by=By.XPATH, value=f"//a[@href='{href}']").click()

	def get_el_and_submit(self, name, value):
		el = self.driver.find_element(By.NAME, name)
		el.send_keys(value)
		return el.submit()

	def test_bout_en_bout(self):
		"""
		Use case:
			- log in
			- book 12 places on competion
			- try to book one more place on the same competition (reject)
			- book 1 place on another competition
		"""
		self.driver.get("http://127.0.0.1:5000")
		assert "GUDLFT Registration" in self.driver.title

		self.get_el_and_submit("email", "main_use_case@gmail.com")
		assert self.driver.find_element(By.TAG_NAME, "h2").text == "Welcome, main_use_case@gmail.com"

		self.get_link_and_click("/book/Competition%20Main%20Use%20Case%201/Club%20Main%20Use%20Case")
		assert self.driver.find_element(By.TAG_NAME, "h2").text == "Competition Main Use Case 1"

		self.get_el_and_submit("places", "12")
		assert self.driver.find_element(By.TAG_NAME, "li").text == "Great-booking complete!"

		self.get_link_and_click("/book/Competition%20Main%20Use%20Case%201/Club%20Main%20Use%20Case")
		self.get_el_and_submit("places", "1")
		assert self.driver.find_element(
			By.TAG_NAME, "li").text == "Not possible, you have already booked 12 places, the maximum must be <= 12"

		self.get_link_and_click("/book/Competition%20Main%20Use%20Case%202/Club%20Main%20Use%20Case")
		self.get_el_and_submit("places", "1")
		assert self.driver.find_element(By.TAG_NAME, "li").text == "Great-booking complete!"

		self.get_link_and_click("/logout")
		assert "GUDLFT Registration" in self.driver.title

		self.driver.quit()
