import unittest
from time import sleep

from helper.BaseMobileUtil import AndroidDriver
from pages import PermissionsAndLanguagePage
from pages.CashDepositPage import CashDepositPage


class CashDepostTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = AndroidDriver().get_android_driver()
        cls.permissionPage = PermissionsAndLanguagePage(cls.driver)
        cls.cashDepositPage = CashDepositPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        AndroidDriver().terminate_app()

    def test_01_cash_deposit(self):
        self.cashDepositPage.wait_and_click(self.cashDepositPage.HAMBURGER_MENU)
        self.cashDepositPage.wait_and_click(self.cashDepositPage.CASHDEPOSITPAGE)
        self.cashDepositPage.wait_and_click(self.cashDepositPage.HOWITWORKS)
        self.cashDepositPage.wait_and_click(self.cashDepositPage.OK)
        self.cashDepositPage.wait_and_click(self.cashDepositPage.TRANSACTIONHISTORY)
        self.cashDepositPage.wait_and_click(self.cashDepositPage.NAVIGATEUPBACK)
        self.cashDepositPage.navigate_to_home_page()
