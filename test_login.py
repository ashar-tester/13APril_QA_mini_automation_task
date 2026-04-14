from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open("https://opensource-demo.orangehrmlive.com/")
    login.login("Admin", "admin123")

    assert dashboard.is_dashboard_visible()


def test_invalid_login(page):
    login = LoginPage(page)

    login.open("https://opensource-demo.orangehrmlive.com/")
    login.login("Admin", "wrongpass")

    assert "Invalid credentials" in login.get_error()