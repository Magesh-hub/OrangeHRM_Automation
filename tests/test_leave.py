from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.leave_page import LeavePage

def test_assign_leave():
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")

    # Login as Admin
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Assign leave
    leave_page = LeavePage(driver)
    leave_page.assign_leave(
        employee="Linda Anderson",
        leave_type="Annual Leave",
        from_date="2026-03-27",
        to_date="2026-03-28"
    )

    # Validate success message
    assert "Successfully Assigned" in leave_page.get_success_message()
    driver.quit()
