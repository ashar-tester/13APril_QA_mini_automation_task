from pages.login_page import LoginPage

def test_logout(page):
    login = LoginPage(page)

    login.open("https://opensource-demo.orangehrmlive.com/")
    login.login("Admin", "admin123")

    page.locator(".oxd-userdropdown-tab").click()
    page.locator("//a[text()='Logout']").click()

    assert page.locator("input[name='username']").is_visible()