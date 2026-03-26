from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.claim_page import ClaimPage

def test_initiate_claim_request():
    driver = get_driver("chrome")
    driver.get("https://opensource-demo.orangehrmlive.com")

    # Login as employee
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")  # Replace with employee credentials if available

    # Create claim
    claim_page = ClaimPage(driver)
    claim_page.create_claim(
        claim_type="Travel",
        amount="1500",
        reason="Client meeting travel expenses"
    )

    # Validate claim submission
    assert "Successfully Saved" in driver.page_source
    driver.quit()
