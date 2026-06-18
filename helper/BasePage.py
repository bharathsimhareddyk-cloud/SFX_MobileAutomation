from selenium.common.exceptions import NoSuchElementException

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, value):
        self.find_element(locator).send_keys(value)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False