import unittest
from time import sleep

from helper.BaseMobileUtil import AndroidDriver
from pages.InsurancePage import InsurancePage
from pages.PermissionsAndLanguagePage import PermissionsAndLanguagePage


class InsuranceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = AndroidDriver().get_android_driver()
        cls.permissionPage = PermissionsAndLanguagePage(cls.driver)
        cls.insurancePage = InsurancePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        AndroidDriver().terminate_app()

    # @classmethod
    # def tearDownClass(cls):
    #     try:
    #         cls.insurancePage.click_home_view()
    #     except Exception:
    #         pass

    # Do NOT terminate the app

    def test_01_insurance_test(self):
        self.insurancePage.wait_and_click(self.insurancePage.HAMBURGER_MENU)
        self.insurancePage.wait_and_click(self.insurancePage.INSURANCE)
        self.insurancePage.wait_and_click(self.insurancePage.HELP)
        self.insurancePage.wait_and_click(self.insurancePage.INSURANCE_RELATED_ISSUE)
        self.insurancePage.wait_and_click(self.insurancePage.RADIOBUTTON_ISSUE_DETAIL_LIST)
        self.insurancePage.wait_and_click(self.insurancePage.NEXT_ISSUE_CONFIRM)
        self.insurancePage.wait_and_click(self.insurancePage.NAVIGATE_BACK)
        self.insurancePage.wait_and_click(self.insurancePage.YOUR_TICKETS)
        self.insurancePage.wait_and_click(self.insurancePage.ISSUES)
        self.insurancePage.wait_and_click(self.insurancePage.FAQ)
        self.insurancePage.wait_and_click(self.insurancePage.CLOSE)
        self.insurancePage.wait_and_click(self.insurancePage.HELP_BACK_BUTTON)
        self.insurancePage.wait_and_click(self.insurancePage.VIEW_INSURANCE_DETAILS)
        self.insurancePage.wait_and_click(self.insurancePage.ACCEPT)
        self.insurancePage.wait_and_click(self.insurancePage.BACK_BUTTON)
        self.insurancePage.wait_and_click(self.insurancePage.HOME_VIEW)
