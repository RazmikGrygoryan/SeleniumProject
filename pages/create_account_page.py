from pages.base_page import BasePage
from pages.locators.create_account import CreateAccountLocators


class CreateAccount(BasePage):
    page_url = "customer/account/create/"

    def login_form(self, first_name, second_name, email, passw, passw_confirmed):
        self.find(CreateAccountLocators.first_name).send_keys(first_name)
        self.find(CreateAccountLocators.second_name).send_keys(second_name)
        self.find(CreateAccountLocators.email).send_keys(email)
        self.find(CreateAccountLocators.passw).send_keys(passw)
        self.find(CreateAccountLocators.passw_confirmed).send_keys(passw_confirmed)
        self.find(CreateAccountLocators.create_account).click()

    def check_right_text(self, text):
        right_text = self.element_is_visible(CreateAccountLocators.success_text)
        assert right_text.text == text

    def check_correct_title(self, text):
        correct_title = self.element_is_visible(CreateAccountLocators.title_wrapper)
        assert correct_title.text == text

    def check_is_error_account(self, text):
        text_error = self.element_is_visible(CreateAccountLocators.error_message)
        assert text_error.text == text

    def incorrect_email(self, text):
        error_email = self.element_is_visible(CreateAccountLocators.email_error)
        assert error_email.text == text
