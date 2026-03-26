from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminPage(BasePage):
    add_button = (By.ID, "btnAdd")
    username_field = (By.ID, "systemUser_userName")
    password_field = (By.ID, "systemUser_password")
    confirm_password_field = (By.ID, "systemUser_confirmPassword")
    save_button = (By.ID, "btnSave")
    search_field = (By.ID, "searchSystemUser_userName")
    search_button = (By.ID, "searchBtn")

    def add_user(self, username, password):
        self.click(self.add_button)
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.enter_text(self.confirm_password_field, password)
        self.click(self.save_button)

    def search_user(self, username):
        self.enter_text(self.search_field, username)
        self.click(self.search_button)
