from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.myinfo_page import MyInfoPage

def test_myinfo_submenus():
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    myinfo