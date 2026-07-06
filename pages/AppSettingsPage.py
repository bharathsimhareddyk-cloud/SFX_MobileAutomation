import random
from appium.webdriver.common.appiumby import AppiumBy
from helper.BasePage import BasePage

class AppSettingsPage(BasePage):
    # ── Locators ──────────────────────────────────────────────────────────────

    HAMBURGER_MENU = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
    APP_SETTINGS =(AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="in.shadowfax.gandalf.staging:id/main"])[7]')
    BATTERY_SETTINGS = (AppiumBy.XPATH,'//androidx.compose.ui.platform.ComposeView[@resource-id="in.shadowfax.gandalf.staging:id/compose_view"]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]')
    BACK_TO_SETTINGS = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/back')
    DEFAULT_SIM = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView[@resource-id="in.shadowfax.gandalf.staging:id/compose_view"]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]')
    ASK_EVERY_TIME = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/askEveryTimeText')
    APP_LANGUAGE = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView[@resource-id="in.shadowfax.gandalf.staging:id/compose_view"]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[5]')
    HINDI_LANGUAGE = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[2]')
    HINGLISH_LANGUAGE = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[3]')
    ENGLISH_LANGUAGE = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[1]')
    SUBMIT_LANGUAGE_BUTTON = (AppiumBy.XPATH, '//android.widget.Button')
    NOTIFICATIONS = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView[@resource-id="in.shadowfax.gandalf.staging:id/compose_view"]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[7]')
    BACK_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView')
    CHECK_FOR_APP_UPDATE= (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView[@resource-id="in.shadowfax.gandalf.staging:id/compose_view"]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[9]')
    APP_ISSUE = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView[@resource-id="in.shadowfax.gandalf.staging:id/compose_view"]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[11]')
    APP_CRASHING =(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[2]/android.widget.CheckBox')
    APP_IS_VERY_SLOW = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[3]/android.widget.CheckBox')
    UNABLE_TO_GO_ONLINE = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[4]/android.widget.CheckBox')
    ERROR_MESSAGE = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[5]/android.widget.CheckBox')
    BATTERY_DRAIN = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[6]/android.widget.CheckBox')
    OTHERS = (AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[7]/android.widget.CheckBox')
    DESCRIPTION =(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[1]')
    SUGGESTION =(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[2]')
    SUBMIT_ISSUE_BUTTON = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[10]/android.widget.Button')
    BACK_TO_HOMEPAGE = (AppiumBy.XPATH, '//android.widget.Button')



    # ── Actions ───────────────────────────────────────────────────────────────
    def enter_text(self, locator, text):
        self.wait_and_click(locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
        self.driver.hide_keyboard()

    def click_hamburger_menu(self):
        self.wait_and_click(self.HAMBURGER_MENU)

    def click_app_settings(self):
        self.wait_and_click(self.APP_SETTINGS)

    def click_battery_settings(self):
        self.wait_and_click(self.BATTERY_SETTINGS)

    def click_back_button(self):
        self.wait_and_click(self.BACK_TO_SETTINGS)

    def click_default_sim(self):
        self.wait_and_click(self.DEFAULT_SIM)

    def click_ask_every_time(self):
        self.wait_and_click(self.ASK_EVERY_TIME)

    def click_language(self):
        self.wait_and_click(self.APP_LANGUAGE)

    def click_hindi_language(self):
        self.wait_and_click(self.HINDI_LANGUAGE)

    def click_hinglish_language(self):
        self.wait_and_click(self.HINGLISH_LANGUAGE)

    def click_english_language(self):
        self.wait_and_click(self.ENGLISH_LANGUAGE)

    def click_submit_button(self):
        self.wait_and_click(self.SUBMIT_LANGUAGE_BUTTON)

    def click_notifications(self):
        self.wait_and_click(self.NOTIFICATIONS)

    def click_back_button_to_settings(self):
        self.wait_and_click(self.BACK_BUTTON)

    def click_check_for_app_update(self):
        self.wait_and_click(self.CHECK_FOR_APP_UPDATE)

    def click_app_issue(self):
        self.wait_and_click(self.APP_ISSUE)

    def click_app_crashing(self):
        self.wait_and_click(self.APP_CRASHING)

    def click_app_is_very_slow(self):
        self.wait_and_click(self.APP_IS_VERY_SLOW)

    def click_unable_to_go_online(self):
        self.wait_and_click(self.UNABLE_TO_GO_ONLINE)

    def click_error_message(self):
        self.wait_and_click(self.ERROR_MESSAGE)

    def click_battery_drain(self):
        self.wait_and_click(self.BATTERY_DRAIN)

    def click_others(self):
        self.wait_and_click(self.OTHERS)

    def enter_description(self, text):
        self.enter_text(self.DESCRIPTION, text)  # types text, then hides keyboard

    def enter_suggestion(self, text):
        self.enter_text(self.SUGGESTION, text)  # types text, then hides keyboard

    def click_submit_issue(self):
        self.wait_and_click(self.SUBMIT_ISSUE_BUTTON)

    def click_back_to_homepage(self):
        self.wait_and_click(self.BACK_TO_HOMEPAGE)


