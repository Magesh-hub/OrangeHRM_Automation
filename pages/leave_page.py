from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LeavePage(BasePage):
    assign_leave_button = (By.ID, "menu_leave_assignLeave")
    employee_field = (By.ID, "assignleave_txtEmployee_empName")
    leave_type_dropdown = (By.ID, "assignleave_txtLeaveType")
    from_date = (By.ID, "assignleave_txtFromDate")
    to_date = (By.ID, "assignleave_txtToDate")
    assign_button = (By.ID, "assignBtn")
    success_message = (By.CLASS_NAME, "message")

    def assign_leave(self, employee, leave_type, from_date, to_date):
        self.click(self.assign_leave_button)
        self.enter_text(self.employee_field, employee)
        self.enter_text(self.leave_type_dropdown, leave_type)
        self.enter_text(self.from_date, from_date)
        self.enter_text(self.to_date, to_date)
        self.click(self.assign_button)

    def get_success_message(self):
        return self.get_text(self.success_message)
