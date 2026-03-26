from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ClaimPage(BasePage):
    claim_button = (By.ID, "menu_claim_viewClaimModule")
    add_claim_button = (By.ID, "btnAdd")
    claim_type_dropdown = (By.ID, "claimType")
    amount_field = (By.ID, "amount")
    reason_field = (By.ID, "reason")
    save_button = (By.ID, "btnSave")

    def create_claim(self, claim_type, amount, reason):
        self.click(self.claim_button)
        self.click(self.add_claim_button)
        self.enter_text(self.claim_type_dropdown, claim_type)
        self.enter_text(self.amount_field, amount)
        self.enter_text(self.reason_field, reason)
        self.click(self.save_button)
