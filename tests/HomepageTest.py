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
        self.homePage.wait_and_click(self.homePage.SLOTS_ICON_LAYOUT)
        self.homePage.wait_and_click(self.homePage.OFFERS_ICON_LAYOUT)
        self.homePage.wait_and_click(self.homePage.EARNINGS_ICON_LAYOUT)
        self.homePage.wait_and_click(self.homePage.HISTORY_ICON_LAYOUT)
        self.homePage.wait_and_click(self.homePage.HOME_ICON_LAYOUT)


if __name__ == '__main__':
    unittest.main()
