import unittest
from helper.BaseMobileUtil import AndroidDriver
from pages.PermissionsAndLanguagePage import PermissionsAndLanguagePage
from pages.PaymentTransactionsPage import PaymentTransactionsPage


class PaymentTransactionsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = AndroidDriver().get_android_driver()
        cls.permissionPage = PermissionsAndLanguagePage(cls.driver)
        cls.PaymentTransactionsPage = PaymentTransactionsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        AndroidDriver().terminate_app()

    def test_01_payment_transactions(self):
        self.PaymentTransactionsPage.wait_and_click(self.PaymentTransactionsPage.HAMBURGER_MENU)
        self.PaymentTransactionsPage.wait_and_click(self.PaymentTransactionsPage.PAYMENT_TRANSACTIONS)
        self.PaymentTransactionsPage.click_backbutton()




        if __name__ == '__main__':
            unittest.main()