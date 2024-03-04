from pathlib import Path

from selene import browser, command, by, have

import tests


class RegistrationPage:
    def __init__(self):
        self.registration_data = browser.element('.table').all('td').even

    def open(self, url):
        browser.open(url)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def select_gender(self, gender):
        browser.element(f'[name=gender][value={gender}]+label').click()

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)

    def fill_birth_date(self, year, month, day):
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def select_hobby(self, hobby):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).perform(command.js.scroll_into_view)
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()

    def upload_picture(self, file_name):
        browser.element('#uploadPicture').set_value(
            str(Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute())
        )

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)

    def fill_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()

    def fill_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()

    def submit(self):
        browser.element('#submit').click()
