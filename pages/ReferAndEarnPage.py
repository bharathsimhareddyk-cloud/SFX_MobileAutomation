import random
from appium.webdriver.common.appiumby import AppiumBy
from helper.BasePage import BasePage


class ReferAndEarnPage(BasePage):
    # ── Locators ──────────────────────────────────────────────────────────────
    HAMBURGER_MENU = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
    REFERANDEARN = (AppiumBy.XPATH,
                    '(//android.view.ViewGroup[@resource-id="in.shadowfax.gandalf.staging:id/main"])[4]')
    PHONE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="refer_phone_input"]')
    REFERNOW = (AppiumBy.XPATH, '//android.view.View[@resource-id="refer_submit_button"]/android.widget.Button')
    REFERMORE = (AppiumBy.XPATH, '//android.widget.Button')  # ⚠️ verify resource-id
    REFERRALEARNINGS = (AppiumBy.XPATH, '//android.view.View[@resource-id="home_tab_earnings"]/android.view.View')
    SHOWDETAILS = (AppiumBy.XPATH,
                   '//android.view.View[@resource-id="status_show_details_button"]/android.widget.Button')
    OK = (AppiumBy.XPATH, '//android.widget.Button')  # ⚠️ verify resource-id
    VIEWALLREFERRALS = (AppiumBy.ID, 'status_view_all')
    SEARCHMOBILENUMBER = (AppiumBy.XPATH, '//android.widget.EditText/android.view.View[1]')
    SEEALLUPDATES = (AppiumBy.XPATH, '//android.widget.TextView[@text="See all updates"]')
    CLOSESHEET = (AppiumBy.XPATH, '//android.widget.Button')
    SEARCHCLOSEBUTTON = (AppiumBy.XPATH, '//android.widget.EditText[@text="9979979797"]/android.widget.Button')
    ALLREFERRALSSEARCH = (AppiumBy.XPATH, '//android.view.View[@resource-id="all_referrals_search"]/android.view.View')
    REFERRED = (AppiumBy.XPATH,
                '//android.view.View[@resource-id="all_referrals_filter"]/android.view.View[2]/android.widget.CheckBox')
    JOINED = (AppiumBy.XPATH,
              '//android.view.View[@resource-id="all_referrals_filter"]/android.view.View[3]/android.widget.CheckBox')
    DECLINED = (AppiumBy.XPATH,
                '//android.view.View[@resource-id="all_referrals_filter"]/android.view.View[4]/android.widget.CheckBox')
    INVALID = (AppiumBy.XPATH,
               '//android.view.View[@resource-id="all_referrals_filter"]/android.view.View[5]/android.widget.CheckBox')
    COMPLETED = (AppiumBy.XPATH,
                 '//android.view.View[@resource-id="all_referrals_filter"]/android.view.View[6]/android.widget.CheckBox')
    EXPIRED = (AppiumBy.XPATH,
               '//android.view.View[@resource-id="all_referrals_filter"]/android.view.View[7]/android.widget.CheckBox')
    APPLYBUTTON = (AppiumBy.XPATH, '//android.widget.Button')
    ALL = (AppiumBy.XPATH,
           '//android.view.View[@resource-id="all_referrals_filter"]/android.view.View[1]/android.widget.CheckBox')
    BACK_BUTTON = (AppiumBy.XPATH, '//android.widget.Button')
    BACK_NAVIGATETOHOME = (AppiumBy.XPATH,
                           '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Button')

    # ── Helpers ───────────────────────────────────────────────────────────────
    @staticmethod
    def generate_phone_number():
        first_digit = random.choice("6789")
        remaining = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        return first_digit + remaining

    # ── Actions ───────────────────────────────────────────────────────────────
    def click_hamburger_menu(self):
        self.wait_and_click(self.HAMBURGER_MENU)

    def click_refer_earn(self):
        self.wait_and_click(self.REFERANDEARN)

    def enter_friend_phone_number(self):
        invalid_number = "1" + ''.join([str(random.randint(0, 9)) for _ in range(9)])
        valid_number = self.generate_phone_number()

        field = self.wait_for_element(self.PHONE_INPUT)
        field.click()
        field.send_keys(invalid_number)
        field.clear()
        field.send_keys(valid_number)
        self.driver.hide_keyboard()

        print(f"[ReferAndEarn] Invalid: {invalid_number} | Valid: {valid_number}")

    # def search_mobile_number(self, number):
    #         field = self.wait_for_element(self.SEARCHMOBILENUMBER)
    #         field.click()
    #         field.clear()
    #         field.send_keys(number)
    #         self.driver.hide_keyboard()
    def search_mobile_number(self, number):
        field = self.wait_for_element(self.SEARCHMOBILENUMBER)
        field.click()
        self.driver.execute_script('mobile: type', {'text': str(number)})  # bypass send_keys

    def navigate_back(self):
        size = self.driver.get_window_size()
        self.driver.swipe(0, size['height'] // 2, size['width'] // 3, size['height'] // 2, duration=300)

    def click_refer_now(self):
        self.wait_and_click(self.REFERNOW)

    def click_refer_more(self):
        self.wait_and_click(self.REFERMORE)

    def click_refer_earnings(self):
        self.wait_and_click(self.REFERRALEARNINGS)

    def click_show_details(self):
        self.wait_and_click(self.SHOWDETAILS)

    def click_ok(self):
        self.wait_and_click(self.OK)

    def click_viewall(self):
        self.scroll_and_click(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("VIEW ALL")')

    def click_see_all(self):
        self.scroll_and_click(self.SEEALLUPDATES)

    def click_closesheet(self):
        self.wait_and_click(self.CLOSESHEET)

    def click_search_close(self):
        self.wait_and_click(self.SEARCHCLOSEBUTTON)

    def click_all_referrals(self):
        self.wait_and_click(self.VIEWALLREFERRALS)

    def click_referred(self):
        self.wait_and_click(self.REFERRED)

    def click_joined(self):
        self.wait_and_click(self.JOINED)

    def click_declined(self):
        self.wait_and_click(self.DECLINED)

    def click_invalid(self):
        self.wait_and_click(self.INVALID)

    def click_completed(self):
        self.wait_and_click(self.COMPLETED)

    def click_expired(self):
        self.wait_and_click(self.EXPIRED)

    def click_apply(self):
        self.wait_and_click(self.APPLYBUTTON)

    def click_all(self):
        self.wait_and_click(self.ALL)

    def click_backbutton(self):
        self.wait_and_click(self.BACK_BUTTON)

    def click_navigatetohome(self):
        self.wait_and_click(self.BACK_NAVIGATETOHOME)
