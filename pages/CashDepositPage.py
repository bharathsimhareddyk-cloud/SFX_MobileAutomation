from appium.webdriver.common.appiumby import AppiumBy
from helper.BasePage import BasePage


class CashDepositPage(BasePage):
    HAMBURGER_MENU = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open navigation drawer"]')

    CASHDEPOSITPAGE = (AppiumBy.XPATH,
                       '(//android.view.ViewGroup[@resource-id="in.shadowfax.gandalf.staging:id/main"])[3]')

    HOWITWORKS = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/how_upi_works_text')

    OK = (AppiumBy.ID, 'android:id/button1')

    TRANSACTIONHISTORY = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/transaction_history_text')

    NAVIGATEUPBACK = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')

    NAVIGATEUPBACKTOHOMEPAGE = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')

    def click_hamburger_menu(self):
        self.click_element(self.HAMBURGER_MENU)

    def click_cash_deposit(self):
        self.click_element(self.CASHDEPOSITPAGE)

    def click_how_works(self):
        self.click_element(self.HOWITWORKS)

    def click_ok(self):
        self.click_element(self.OK)

    def click_transactionhistory(self):
        self.click_element(self.TRANSACTIONHISTORY)

    def click_navigate_to_cash_deposit_page(self):
        self.click_element(self.NAVIGATEUPBACK)

    def navigate_to_home_page(self):
        self.click_element(self.NAVIGATEUPBACKTOHOMEPAGE)
