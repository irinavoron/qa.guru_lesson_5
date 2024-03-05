from tests.demoqa_tests.data import users
from tests.demoqa_tests.pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open('/automation-practice-form')
    registration_page.register(users.student)

    registration_page.should_have_registered(users.student)
