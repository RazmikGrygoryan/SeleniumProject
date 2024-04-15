from pages.base_page import BasePage
from pages.locators.eco_friendly import EcoFriendlyLocators
from selenium.webdriver.common.action_chains import ActionChains


class EcoFriendly(BasePage):
    page_url = "collections/eco-friendly.html"
    value = None
    text_actual_size = None
    actual_size = None
    qty_text = None
    qty = None
    text_size = None
    size = None

    def choose_item(self):
        self.find(EcoFriendlyLocators.product).click()
        self.size = self.find(EcoFriendlyLocators.size_option)
        self.text_size = self.find(EcoFriendlyLocators.size_option).text
        self.size.click()
        self.find(EcoFriendlyLocators.color_option).click()
        self.qty = self.find(EcoFriendlyLocators.input_qty)
        self.qty_text = self.find(EcoFriendlyLocators.input_qty).text
        self.qty.clear()
        self.qty.send_keys(10)
        self.find(EcoFriendlyLocators.add_to_cart).click()
        self.element_is_visible(EcoFriendlyLocators.shopping_cart).click()

    def check_right_size(self):
        assert self.text_size == self.find(EcoFriendlyLocators.size).text

    def check_right_qty(self):
        assert self.qty_text == self.find(EcoFriendlyLocators.qty).text

    def filter(self):
        self.find(EcoFriendlyLocators.filter_size).click()
        self.actual_size = self.find(EcoFriendlyLocators.actual_size)
        self.text_actual_size = self.find(EcoFriendlyLocators.actual_size).text
        self.actual_size.click()
        self.value = self.find(EcoFriendlyLocators.filter_value).text
        self.find(EcoFriendlyLocators.clear_all).click()

    def check_value_filter(self):
        assert self.value == self.text_actual_size

    def compare_product(self):
        self.action.move_to_element(self.find(EcoFriendlyLocators.product_item))
        self.action.click(self.find(EcoFriendlyLocators.compare_button))
        self.action.perform()

    def check_name_item(self):
        assert self.find(EcoFriendlyLocators.product_name).text == \
               self.find(EcoFriendlyLocators.first_name_product).text
