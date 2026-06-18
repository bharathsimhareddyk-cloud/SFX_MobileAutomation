import unittest
from time import sleep

from helper.BaseMobileUtil import AndroidDriver
from pages.ProfileSectionPage import ProfileSectionPage
from pages.PermissionsAndLanguagePage import PermissionsAndLanguagePage


class ProfileSectionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = AndroidDriver().get_android_driver()
        cls.permissionPage = PermissionsAndLanguagePage(cls.driver)
        cls.profileSectionPage = ProfileSectionPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        AndroidDriver().terminate_app()
    # @classmethod
    # def tearDownClass(cls):
    #     try:
    #         cls.profileSectionPage.click_home_view()
    #     except Exception:
    #         pass

    def test_01_profile_section(self):
        # Navigate to Personal Info screen
        self.profileSectionPage.click_hamburger_menu()
        self.profileSectionPage.click_profile_navigation_button()
        sleep(2)
        self.profileSectionPage.click_personalinfo()
        sleep(2)
        self.profileSectionPage.click_back()
        sleep(2)
        self.profileSectionPage.click_my_documents()
        sleep(2)
        self.profileSectionPage.click_bank_account()
        sleep(2)
        self.profileSectionPage.click_back()
        self.profileSectionPage.click_back()
        self.profileSectionPage.click_shadowfax_kit()
        self.profileSectionPage.click_back()
        self.profileSectionPage.click_terms_and_conditions()
        sleep(2)
        self.profileSectionPage.click_back()
        self.profileSectionPage.click_whatsapp_toggle()
        sleep(2)
        self.profileSectionPage.click_whatsapp_toggle()


        # self.profileSectionPage.click_sign_out()



if __name__ == '__main__':
    unittest.main()