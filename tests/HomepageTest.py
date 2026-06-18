import subprocess
import time
import unittest
from datetime import datetime

from helper.ApiUtils import ApiEngine
from helper.BaseMobileUtil import AndroidDriver
from helper.TestConfigs import TestConfig, RIDER_CONFIG
from pages.HomePage import HomePage
from pages.PermissionsAndLanguagePage import PermissionsAndLanguagePage
# from tests.BaseMobileUtils import AndroidDriver
# from tests.MyDocumentsTest import MyDocumentsTest


class HomePageTest(unittest.TestCase):

    homepage = None

    def setUp(self):
        self.driver = AndroidDriver().get_android_driver()
        self.permissionPage = PermissionsAndLanguagePage(self.driver)
        self.homePage = HomePage(self.driver)

    def tearDown(self):
         AndroidDriver().terminate_app()


    def test_01_home_button(self):
        self.homePage.click_slots_icon_layout()
        time.sleep(0.2)
        self.homePage.click_offers_icon_layout()
        time.sleep(0.2)
        self.homePage.click_earnings_icon_layout()
        time.sleep(0.2)
        self.homePage.click_history_icon_layout()
        time.sleep(0.2)
        self.homePage.click_home_icon_layout()


if __name__ == '__main__':
    unittest.main()
