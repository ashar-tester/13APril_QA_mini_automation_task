from pages.login_page import LoginPage
from pages.pim_page import PIMPage

def test_search_employee(page):
    login = LoginPage(page)
    pim = PIMPage(page)

    login.open("https://opensource-demo.orangehrmlive.com/")
    login.login("Admin", "admin123")

    pim.go_to_pim()
    pim.search_employee("Linda")

    assert pim.is_result_visible()