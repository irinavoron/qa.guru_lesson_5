from selene import have
from tests.demoqa_tests.pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open('/automation-practice-form')

    # WHEN
    registration_page.fill_first_name('firstName')
    registration_page.fill_last_name('lastName')
    registration_page.fill_email('email@example.com')
    registration_page.select_gender('Female')
    registration_page.fill_phone_number('1234567890')
    registration_page.fill_birth_date('1985', 'April', '18')
    registration_page.fill_subject('english')
    registration_page.select_hobby('Sports')
    registration_page.upload_picture('picture.jpg')
    registration_page.fill_address('Some Street, 1')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')

    registration_page.submit()

    # THEN
    registration_page.registration_data.should(have.texts(
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
