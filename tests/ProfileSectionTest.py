import unittest
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
        self.profileSectionPage.wait_and_click(self.profileSectionPage.HAMBURGER_MENU)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.PROFILE_NAVIGATION_BUTTON)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.PERSONAL_INFO)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.BACK_BUTTON)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.MY_DOCUMENTS)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.BANK_ACCOUNT)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.BACK_BUTTON)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.BACK_BUTTON)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.SHADOWFAX_KIT)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.BACK_BUTTON)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.TERMS_AND_CONDITIONS)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.BACK_BUTTON)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.WHATSAPP_TOGGLE)
        self.profileSectionPage.wait_and_click(self.profileSectionPage.WHATSAPP_TOGGLE)

        # self.profileSectionPage.wait_and_click(self.profileSectionPage.SIGN_OUT)


if __name__ == '__main__':
    unittest.main()
