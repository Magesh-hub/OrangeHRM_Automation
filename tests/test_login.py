import pytest
import pandas as pd
from utils.driver_factory import get_driver
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password", pd.read_csv("data/credentials.csv").values)
def test_login(username, password):
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)
    login_page.login(username, password)

    if username == "Admin" and password == "admin123":
        assert "Dashboard" in driver.title
    else:
        assert login_page.get_error_message() == "Invalid credentials"
    driver.quit()

def test_homepage_accessible():
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")
    assert "OrangeHRM" in driver.title
    driver.quit()

def test_login_fields_visible():
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)
    assert driver.find_element(*login_page.username_field).is_displayed()
    assert driver.find_element(*login_page.password_field).is_displayed()
    driver.quit()
