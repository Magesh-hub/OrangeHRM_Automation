from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username_field = (By.ID, "txtUsername")
    password_field = (By.ID, "txtPassword")
    login_button = (By.ID, "btnLogin")
    error_message = (By.ID, "spanMessage")

    def login(self, username, password):
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)
