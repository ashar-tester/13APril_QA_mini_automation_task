from utils.base_page import BasePage

class PIMPage(BasePage):
    PIM_MENU = "//span[text()='PIM']"
    EMPLOYEE_NAME = "input[placeholder='Type for hints...']"
    SEARCH_BTN = "//button[@type='submit']"
    RESULT = ".oxd-table-body"

    def go_to_pim(self):
        self.click(self.PIM_MENU)

    def search_employee(self, name):
        self.fill(self.EMPLOYEE_NAME, name)
        self.click(self.SEARCH_BTN)

    def is_result_visible(self):
        return self.is_visible(self.RESULT)