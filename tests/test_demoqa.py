from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(users.student)

    registration_page.should_have_registered(users.student)
