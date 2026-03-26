from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    menu_items = {
        "Admin": (By.ID, "menu_admin_viewAdminModule"),
        "PIM": (By.ID, "menu_pim_viewPimModule"),
        "Leave": (By.ID, "menu_leave_viewLeaveModule"),
        "Time": (By.ID, "menu_time_viewTimeModule"),
        "Recruitment": (By.ID, "menu_recruitment_viewRecruitmentModule"),
        "My Info": (By.ID, "menu_pim_viewMyDetails"),
        "Performance": (By.ID, "menu__Performance"),
        "Dashboard": (By.ID, "menu_dashboard_index")
    }

    def is_menu_visible(self, menu_name):
        locator = self.menu_items[menu_name]
        return self.wait.until(lambda d: d.find_element(*locator).is_displayed())
