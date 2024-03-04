from pathlib import Path
from selene import browser, command, by, have
import tests

class RegistrationPage:

    def open(self, url):
        browser.open(url)


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('firstName')
    browser.element('#lastName').type('lastName')
    browser.element('#userEmail').type('email@example.com')
    browser.element('[name=gender][value=Female]+label').click()
    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1985')).click()
    browser.element('.react-datepicker__month-select').click().element(by.text('April')).click()
    browser.element(f'.react-datepicker__day--0{18}').click()

    browser.element('#subjectsInput').type('english').press_enter()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).perform(command.js.scroll_into_view)
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).click()
    browser.element('#uploadPicture').set_value(
        str(Path(tests.__file__).parent.joinpath('resources/picture.jpg').absolute())
    )
    browser.element('#currentAddress').type('Some Street, 1')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Delhi')).click()

    browser.element('#submit').click()

    # THEN
    browser.element('.table').all('td').even.should(have.texts(
        'firstName lastName',
        'email@example.com',
        'Female',
        '1234567890',
        '18 April,1985',
        'English',
        'Sports',
        'picture.jpg',
        'Some Street, 1',
        'NCR Delhi'
        )
    )
