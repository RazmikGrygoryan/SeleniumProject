from selenium.webdriver.common.by import By


class CreateAccountLocators:
    first_name = (By.ID, 'firstname')
    second_name = (By.ID, 'lastname')
    email = (By.ID, 'email_address')
    passw = (By.ID, 'password')
    passw_confirmed = (By.ID, 'password-confirmation')
    create_account = (By.XPATH, '//button[@class="action submit primary"]')
    success_text = (By.CSS_SELECTOR, '[class="message-success success message"]')
    title_wrapper = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
    error_message = (By.CSS_SELECTOR, '[class="message-error error message"]')
    email_error = (By.ID, 'email_address-error')
