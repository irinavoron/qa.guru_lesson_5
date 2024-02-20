import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_size():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 900
    browser.config.window_height = 1200

    yield

    browser.quit()
