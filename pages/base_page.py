from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def element_is_visible(self, locator, timeout=25):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=25):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def action_chains(self):
        return self.action
