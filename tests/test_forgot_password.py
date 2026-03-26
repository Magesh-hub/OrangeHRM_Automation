from utils.driver_factory import get_driver
from pages.login_page import LoginPage

def test_forgot_password():
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.find_element_by_link_text("Forgot your password?").click()
    driver.find_element_by_id("securityAuthentication_userName").send_keys("Admin")
    driver.find_element_by_id("btnSearchValues").click()
    assert "instructions" in driver.page_source.lower()
    driver.quit()
