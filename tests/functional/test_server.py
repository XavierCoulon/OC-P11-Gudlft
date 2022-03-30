import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_get_index():
	driver.get("http://127.0.0.1:5000")
	time.sleep(5)
	assert "GUDLFT" in driver.title
	driver.quit()

