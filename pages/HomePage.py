from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey

from helper.BasePage import BasePage


class HomePage(BasePage):
    HOME_ICON_LAYOUT = (AppiumBy.ID, "in.shadowfax.gandalf.staging:id/nav_home")
    SLOTS_ICON_LAYOUT = (AppiumBy.ID, "in.shadowfax.gandalf.staging:id/nav_slots")
    OFFERS_ICON_LAYOUT = (AppiumBy.ID, "in.shadowfax.gandalf.staging:id/nav_infinity")
    EARNINGS_ICON_LAYOUT = (AppiumBy.ID, "in.shadowfax.gandalf.staging:id/nav_payouts")
    HISTORY_ICON_LAYOUT = (AppiumBy.ID, "in.shadowfax.gandalf.staging:id/nav_history")
    NAVIGATION_DRAWER = (AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer")
    HELP_BUTTON = (AppiumBy.ID, "in.shadowfax.gandalf.staging:id/iv_help_icon")
    SCROLL_UP_TEXTVIEW = (AppiumBy.ID, "in.shadowfax.gandalf.staging:id/scroll_up_text")
    DUTY_STATUS = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/dutyText')
    DUTY_SWITCH = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/dutySwitch')



    def __init__(self, driver):
        super().__init__(driver)

    def verify_homepage(self):
        return self.is_element_present(self.HOME_ICON_LAYOUT)

    def click_home_icon_layout(self):
        self.click_element(self.HOME_ICON_LAYOUT)

    def click_slots_icon_layout(self):
        self.click_element(self.SLOTS_ICON_LAYOUT)

    def click_offers_icon_layout(self):
        self.click_element(self.OFFERS_ICON_LAYOUT)

    def click_earnings_icon_layout(self):
        self.click_element(self.EARNINGS_ICON_LAYOUT)

    def click_history_icon_layout(self):
        self.click_element(self.HISTORY_ICON_LAYOUT)

    def click_help_button(self):
        self.click_element(self.HELP_BUTTON)
