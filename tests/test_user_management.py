from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_create_user_and_login():
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    admin_page = AdminPage(driver)
    admin_page.add_user("newuser1", "Password@123")
    driver.quit()

    # Verify login with new user
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)
    login_page.login("newuser1", "Password@123")
    assert "Dashboard" in driver.title
    driver.quit()

def test_new_user_in_list():
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    admin_page = AdminPage(driver)
    admin_page.search_user("newuser1")
    assert "newuser1" in driver.page_source
    driver.quit()
