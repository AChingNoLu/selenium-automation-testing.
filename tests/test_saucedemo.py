"""Six Selenium test cases for SauceDemo."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from conftest import PASSWORD, USERNAME

def test_01_login_success(driver):
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(lambda d: "inventory.html" in d.current_url)
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

def test_02_login_wrong_password(driver):
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    )
    assert "Username and password do not match" in error.text
    assert "inventory.html" not in driver.current_url

def test_03_add_product_to_cart(logged_in):
    driver = logged_in
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"

def test_04_remove_product_from_cart(logged_in):
    driver = logged_in
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    assert not driver.find_elements(By.CLASS_NAME, "cart_item")
    assert not driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

def test_05_sort_products_price_low_to_high(logged_in):
    driver = logged_in
    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")
    prices = [float(p.text.replace("$", "")) for p in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
    assert len(prices) >= 2
    assert prices == sorted(prices)

def test_06_logout(logged_in):
    driver = logged_in
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-button")))
    assert driver.current_url.rstrip("/") == "https://www.saucedemo.com"
