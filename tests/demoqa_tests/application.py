from tests.demoqa_tests.pages.left_panel import LeftPanel
from tests.demoqa_tests.pages.simple_registration_form import SimpleRegistrationForm


class ApplicationManager:
    def __init__(self):
        self.simple_registration = SimpleRegistrationForm()
        self.left_panel = LeftPanel()


app = ApplicationManager()
