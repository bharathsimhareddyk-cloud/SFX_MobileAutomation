import unittest
from helper.BaseMobileUtil import AndroidDriver
from pages.PermissionsAndLanguagePage import PermissionsAndLanguagePage
from pages.AppSettingsPage import AppSettingsPage


class AppSettingsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = AndroidDriver().get_android_driver()
        cls.permissionPage = PermissionsAndLanguagePage(cls.driver)
        cls.AppSettingsPage = AppSettingsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        AndroidDriver().terminate_app()

    def test_01_navigate_to_app_settings(self):
            self.AppSettingsPage.wait_and_click(self.AppSettingsPage.HAMBURGER_MENU)
            self.AppSettingsPage.wait_and_click(self.AppSettingsPage.APP_SETTINGS)

    def test_02_battery_and_sim_settings(self):
            self.AppSettingsPage.click_battery_settings()
            self.AppSettingsPage.click_back_button()
            self.AppSettingsPage.click_default_sim()
            self.AppSettingsPage.click_ask_every_time()

    def test_03_change_app_language(self):
            self.AppSettingsPage.click_language()
            self.AppSettingsPage.click_hindi_language()
            self.AppSettingsPage.click_hinglish_language()
            self.AppSettingsPage.click_english_language()
            self.AppSettingsPage.click_submit_button()

    def test_04_notifications_settings(self):
            self.AppSettingsPage.click_notifications()
            self.AppSettingsPage.click_back_button_to_settings()

    def test_05_check_for_app_update(self):
            self.AppSettingsPage.wait_and_click(self.AppSettingsPage.CHECK_FOR_APP_UPDATE)

    def test_06_report_app_issue(self):
            self.AppSettingsPage.click_app_issue()
            self.AppSettingsPage.click_app_crashing()
            self.AppSettingsPage.click_app_is_very_slow()
            self.AppSettingsPage.click_unable_to_go_online()
            self.AppSettingsPage.click_error_message()
            self.AppSettingsPage.click_battery_drain()
            self.AppSettingsPage.click_others()
            self.AppSettingsPage.enter_description("Automated Test Execution")
            self.AppSettingsPage.enter_suggestion("App performance could be improved during peak usage hours.")
            self.AppSettingsPage.click_submit_issue()

    def test_07_back_to_homepage(self):
            self.AppSettingsPage.click_back_to_homepage()