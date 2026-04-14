from utils.base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD_HEADER = "h6:has-text('Dashboard')"

    def is_dashboard_visible(self):
        return self.is_visible(self.DASHBOARD_HEADER)