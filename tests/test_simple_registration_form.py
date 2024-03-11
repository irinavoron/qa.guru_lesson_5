from selene import have

from tests.demoqa_tests.application import app
from tests.demoqa_tests.data import users


def test_simple_registration_form():
    user = users.student

    app.left_panel.open_simple_registration_form()

    app.simple_registration.fill_full_name(user.full_name)
    app.simple_registration.fill_email(user.email)
    app.simple_registration.fill_current_address(user.current_address)
    app.simple_registration.fill_permanent_address(user.permanent_address)

    app.simple_registration.submit_form()

    app.simple_registration.output.should(have.texts(
        user.full_name,
        user.email,
        user.current_address,
        user.permanent_address
    )
    )
