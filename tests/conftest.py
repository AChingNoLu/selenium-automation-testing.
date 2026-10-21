import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS", "0") == "1":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1365,900")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    browser.get(BASE_URL)
    yield browser
    browser.quit()

@pytest.fixture
def logged_in(driver):
    from selenium.webdriver.common.by import By
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(lambda d: "inventory.html" in d.current_url)
    return driver
