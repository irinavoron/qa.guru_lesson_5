from pathlib import Path
from selene import browser, by, command, have

import tests
from tests.demoqa_tests.data.users import User


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def register(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element(f'[name=gender][value={user.gender}]+label').click()
        browser.element('#userNumber').type(user.phone_number)

        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(f'{user.birth_date.year}')).click()
        browser.element('.react-datepicker__month-select').click().element(
            by.text(user.birth_date.strftime('%B'))).click()
        browser.element(f'.react-datepicker__day--0{user.birth_date.day}').click()

        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(user.hobby)).perform(command.js.scroll_into_view)
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(user.hobby)).click()
        browser.element('#uploadPicture').set_value(
            str(Path(tests.__file__).parent.joinpath(f'resources/{user.file}').absolute())
        )
        browser.element('#currentAddress').type(user.address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.city)).click()

        browser.element('#submit').click()

    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            user.birth_date.strftime('%d %B,%Y'),
            user.subject,
            user.hobby,
            user.file,
            user.address,
            f'{user.state} {user.city}'
        )
        )
