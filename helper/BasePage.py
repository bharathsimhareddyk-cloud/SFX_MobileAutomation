from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ── Wait Config ───────────────────────────────────────────────────────────────
DEFAULT_TIMEOUT   = 10
MAX_SCROLL_SWIPES = 10
MAX_RETRIES       = 3


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # ── Element Finders ───────────────────────────────────────────────────────
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    # ── Waits ─────────────────────────────────────────────────────────────────
    def wait_for_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_and_click(self, locator, timeout=DEFAULT_TIMEOUT):
        for attempt in range(MAX_RETRIES):
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                ).click()
                return
            except StaleElementReferenceException:
                if attempt == MAX_RETRIES - 1:
                    raise
                # DOM refreshed — retry finding and clicking the element

    # ── Actions ───────────────────────────────────────────────────────────────
    def click_element(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, value):
        self.find_element(locator).send_keys(value)

    def get_text(self, locator):
        return self.find_element(locator).text

    # ── Scroll ────────────────────────────────────────────────────────────────
    def scroll_and_click(self, locator_strategy, locator_value):
        size    = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.8)
        end_y   = int(size['height'] * 0.2)

        for _ in range(MAX_SCROLL_SWIPES):
            try:
                self.driver.find_element(locator_strategy, locator_value).click()
                return
            except (NoSuchElementException, StaleElementReferenceException):
                self.driver.swipe(start_x, start_y, start_x, end_y, duration=800)

        raise TimeoutException(
            f"Element '{locator_value}' not found after {MAX_SCROLL_SWIPES} swipes"
        )