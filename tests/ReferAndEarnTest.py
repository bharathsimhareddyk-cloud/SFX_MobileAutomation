import unittest
from helper.BaseMobileUtil import AndroidDriver
from pages.PermissionsAndLanguagePage import PermissionsAndLanguagePage
from pages.ReferAndEarnPage import ReferAndEarnPage


class ReferAndEarnTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = AndroidDriver().get_android_driver()
        cls.permissionPage = PermissionsAndLanguagePage(cls.driver)
        cls.referAndEarnPage = ReferAndEarnPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        AndroidDriver().terminate_app()

    def test_01_refer_earn(self):
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.HAMBURGER_MENU)
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.REFERANDEARN)
        self.referAndEarnPage.enter_friend_phone_number()
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.REFERNOW)
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.REFERMORE)
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.REFERRALEARNINGS)
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.SHOWDETAILS)
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.OK)
        self.referAndEarnPage.click_viewall()
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.SEARCHMOBILENUMBER)
        self.referAndEarnPage.search_mobile_number("9979979797")
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.SEEALLUPDATES)
        self.referAndEarnPage.click_closesheet()
        self.referAndEarnPage.click_search_close()
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.ALLREFERRALSSEARCH)
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.REFERRED)
        self.referAndEarnPage.click_joined()
        self.referAndEarnPage.click_declined()
        self.referAndEarnPage.click_invalid()
        self.referAndEarnPage.click_completed()
        self.referAndEarnPage.click_expired()
        self.referAndEarnPage.click_apply()
        self.referAndEarnPage.wait_and_click(self.referAndEarnPage.ALLREFERRALSSEARCH)
        self.referAndEarnPage.click_all()
        self.referAndEarnPage.click_apply()
        self.referAndEarnPage.click_backbutton()
        self.referAndEarnPage.click_navigatetohome()


if __name__ == '__main__':
    unittest.main()
