from selene import browser, have


class LeftPanel:
    def __init__(self):
        self.text_box = browser.all('.left-pannel li').element_by(have.text('Text Box'))

    def open_simple_registration_form(self):
        browser.open('/elements')
        self.text_box.click()
