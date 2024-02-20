from selene import browser, command, by, have
import os


def test_form_filling():
    browser.open("/automation-practice-form")
    browser.element("#firstName").type('Irina')
    browser.element("#lastName").type("Voron")
    browser.element('#userEmail').with_(type_by_js=True).type('voron@gmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__month-select').click().element(by.text('February')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1970')).click()
    browser.element(by.text('28')).click()
    browser.element('#subjectsInput').type('english').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture.jpg'))
    browser.element('#currentAddress').type('NCR, Delhi')
    browser.element('#state').click().element('#react-select-3-option-0').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#submit').click()
    browser.element('[class~="modal-title"]').should(have.exact_text('Thanks for submitting the form'))

    browser.element('.table').should(have.text('Irina Voron'))
    browser.element('.table').should(have.text('voron@gmail.com'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('1234567890'))
    browser.element('.table').should(have.text('28 February,1970'))
    browser.element('.table').should(have.text('English'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('picture.jpg'))
    browser.element('.table').should(have.text('NCR, Delhi'))
    browser.element('.table').should(have.text('NCR Delhi'))
