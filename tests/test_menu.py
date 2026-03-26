from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_menu_items_visible():
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    dashboard = DashboardPage(driver)

    for menu in dashboard.menu_items.keys():
        assert dashboard.is_menu_visible(menu)
    driver.quit()
