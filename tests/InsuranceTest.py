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
        self.insurancePage.click_hamburger_menu()
        self.insurancePage.click_insurance()
        sleep(2)
        self.insurancePage.click_help()
        sleep(2)
        self.insurancePage.click_insurance_related_issue()
        sleep(2)
        self.insurancePage.click_radiobutton_issue_detail_list()
        self.insurancePage.click_next_issue_confirm()
        sleep(2)
        self.insurancePage.click_navigate_back()
        sleep(2)
        self.insurancePage.click_your_tickets()
        self.insurancePage.click_issues()
        self.insurancePage.click_faq()
        sleep(2)
        self.insurancePage.click_close()
        sleep(2)
        self.insurancePage.click_help_back_button()
        sleep(2)
        self.insurancePage.click_view_insurance_details()
        sleep(3)
        self.insurancePage.click_accept()
        self.insurancePage.click_back()
        self.insurancePage.click_home_view()
