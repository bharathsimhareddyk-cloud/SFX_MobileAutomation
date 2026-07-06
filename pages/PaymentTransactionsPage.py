import random
from appium.webdriver.common.appiumby import AppiumBy
from helper.BasePage import BasePage

class PaymentTransactionsPage(BasePage):
    # ── Locators ──────────────────────────────────────────────────────────────

    HAMBURGER_MENU = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
    PAYMENT_TRANSACTIONS = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="in.shadowfax.gandalf.staging:id/main"])[6]')
    BACK_BUTTON = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/back')

    # ── Actions ───────────────────────────────────────────────────────────────
    def click_hamburger_menu(self):
        self.wait_and_click(self.HAMBURGER_MENU)
    def click_payment_transactions(self):
        self.wait_and_click(self.PAYMENT_TRANSACTIONS)

    def click_backbutton(self):
            self.wait_and_click(self.BACK_BUTTON)



