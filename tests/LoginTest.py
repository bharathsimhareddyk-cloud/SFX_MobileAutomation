import time
import unittest

from helper.BaseMobileUtil import AndroidDriver
from helper.DBUtils import fetch_otp_for_mobile
from helper.TestConfigs import TestConfig
from pages.LoginPage import LoginAndOTPPage
from pages.PermissionsAndLanguagePage import PermissionsAndLanguagePage


class LoginTest(unittest.TestCase):

    def setUp(self):
        # AndroidDriver.clear_app_data()
        self.driver = AndroidDriver().get_android_driver()
        self.permissionPage = PermissionsAndLanguagePage(self.driver)
        self.loginAndOTPPage = LoginAndOTPPage(self.driver)

    def tearDown(self):
        AndroidDriver().terminate_app()

    def navigate_past_permissions_and_language(self, language="English"):
        # time.sleep(2)
        self.permissionPage.allow_permissions()
        self.permissionPage.allow_permissions()
        self.permissionPage.select_preferred_language_new_ui(language)

    def test_01_login_with_otp(self):
        mobile_number = TestConfig().get_config().get('mobile_number')
        self.navigate_past_permissions_and_language()
        self.loginAndOTPPage.enter_mobile_number(mobile_number)
        self.loginAndOTPPage.proceed_with_otp_flow()
        self.permissionPage.allow_permissions()

        otp = fetch_otp_for_mobile(mobile_number)
        self.loginAndOTPPage.enter_otp(otp)
        self.loginAndOTPPage.submit_otp()
        self.permissionPage.allow_permissions()


if __name__ == '__main__':
    unittest.main()
