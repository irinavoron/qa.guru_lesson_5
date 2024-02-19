from selene import browser, command, be, have
import os


def test_form_filling():
    browser.open("/")
    browser.element("#firstName").type('Irina')
    browser.element("#lastName").type("Voron")
    browser.element('#userEmail').with_(type_by_js=True).type('voron@gmail.com')
    browser.element('#dateOfBirthInput').click().perform(command.select_all).type('28 Feb 1960')
    browser.element('[for="gender-radio-2"]').perform(command.js.scroll_into_view).click()
    browser.element('#userNumber').type('1234567890')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture.jpg'))
    browser.element('#currentAddress').type('Belarus, Minsk')
    #browser.element('#state').click().element('')

    browser.element('#submit').click()
    browser.element('[class~="modal-title"]').should(have.exact_text('Thanks for submitting the form'))

    #browser.all().should(have.exact_texts('Irina Voron', 'voron@gmail.com', 'Female'))


