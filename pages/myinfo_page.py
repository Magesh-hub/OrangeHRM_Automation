from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyInfoPage(BasePage):
    submenus = {
        "Personal Details": (By.LINK_TEXT, "Personal Details"),
        "Contact Details": (By.LINK_TEXT, "Contact Details"),
        "Emergency Contacts": (By.LINK_TEXT, "Emergency Contacts")
    }

    def is_submenu_visible(self, submenu_name):
        locator = self.submenus[submenu_name]
        return self.wait.until(lambda d: d.find_element(*locator).is_displayed())
