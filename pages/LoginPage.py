import time

from appium.webdriver.common.appiumby import AppiumBy

from helper.BasePage import BasePage


class LoginAndOTPPage(BasePage):
    MOBILE_NUMBER_EDITTEXT = (AppiumBy.XPATH, "//android.widget.EditText")
    MOBILE_NUMBER_INPUT = (
        AppiumBy.XPATH, "//android.widget.EditText[@text='+91 ']/android.view.View[3]"
    )
    CONTINUE_BUTTON = (
        AppiumBy.XPATH,
        "//android.view.View[@content-desc='Login input container']/android.view.View[1]/android.widget.Button",
    )
    PROCEED_WITH_OTP_BUTTON = (AppiumBy.XPATH,
                               "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
    CAROUSAL_IMAGES = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Carousel Images"]')
    MOBILE_NUMBER_TEXTBOX = (AppiumBy.XPATH, '//android.widget.TextView[@text="Enter the mobile number"]')
    CONTINUE_TV = (AppiumBy.XPATH, '//android.widget.TextView[@text="Continue"]')
    PROCEED_WITH_OTP_TV = (AppiumBy.XPATH, '//android.widget.TextView[@text="Proceed with OTP Flow"]')
    # TC_FIRST_TV = (AppiumBy.XPATH,
    #                '//android.widget.TextView[@text="By continuing you agree to our privacy policy and"]')
    TC_SECOND_TV = (AppiumBy.XPATH, '//android.widget.TextView[@text="Terms and Conditions"]')
    STAGING_BUTTON = (AppiumBy.XPATH,
                      '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]')

    EMPTY_MOBILE_NUMBER_TV = (AppiumBy.XPATH, '//android.widget.TextView[@text="Mobile number cannot be empty"]')

    OTP_PAGE_TITLE = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/tv_otp_title')
    OTP_PAGE_SUBTITLE = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/tv_otp_subtitle')
    OTP_PAGE_CHANGE_NUMBER = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/tv_edit_mobile')
    OTP_PAGE_OTP_BOX = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/et_otp')
    OTP_PAGE_RESEND_TIMER = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/tv_resend_otp_timer')
    OTP_PAGE_RESEND_TV = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/tv_resend_otp')
    OTP_PAGE_SUBMIT_BUTTON = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/bt_otp_submit')
    OTP_PAGE_INFO_TV = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/otp_information')
    OTP_PAGE_DETECT_OTP_TV = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/tv_detect_otp')

    SNACKBAR_TV = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/snackbar_text')
    NAV_BACK = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/iv_back')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_mobile_number(self, mobile_number):
        # Always use the EditText directly, not the child view
        field = self.find_element(self.MOBILE_NUMBER_EDITTEXT)
        field.click()
        time.sleep(0.5)
        field.clear()
        if mobile_number:
            field.send_keys(mobile_number)

    def click_continue(self):
        if self.is_element_present(self.CONTINUE_BUTTON):
            self.click_element(self.CONTINUE_BUTTON)
        else:
            self.click_element(self.CONTINUE_TV)

    def proceed_with_otp_flow(self):
        if self.is_element_present(self.CONTINUE_BUTTON):
            self.click_continue()
        else:
            self.click_element(self.PROCEED_WITH_OTP_BUTTON)

    def submit_otp(self):
        self.click_element(self.OTP_PAGE_SUBMIT_BUTTON)

    def enter_otp(self, otp):
        otp_field = self.find_element(self.OTP_PAGE_OTP_BOX)
        otp_field.clear()
        otp_field.send_keys(otp)

    def gettext_mobile_number_tv(self):
        return self.get_element_text(self.MOBILE_NUMBER_TEXTBOX)

    def gettext_continue_tv(self):
        return self.get_element_text(self.CONTINUE_TV)

    def click_continue_tv(self):
        self.click_element(self.CONTINUE_TV)

    def gettext_proceed_with_otp_tv(self):
        return self.get_element_text(self.PROCEED_WITH_OTP_TV)

    def gettext_tc_first_tv(self):
        return self.get_element_text(self.TC_FIRST_TV)

    def gettext_tc_second_tv(self):
        return self.get_element_text(self.TC_SECOND_TV)

    def ispresent_staging_button(self):
        return self.is_element_present(self.STAGING_BUTTON)

    def ispresent_corousal_images(self):
        return self.is_element_present(self.CAROUSAL_IMAGES)

    def ispresent_mobile_number_edittext(self):
        return self.is_element_present(self.MOBILE_NUMBER_EDITTEXT)

    def gettext_mobile_number_empty_error(self):
        return self.get_element_text(self.EMPTY_MOBILE_NUMBER_TV)

    def gettext_entered_number(self):
        return self.get_element_text(self.MOBILE_NUMBER_EDITTEXT)

    def gettext_otp_title(self):
        return self.get_element_text(self.OTP_PAGE_TITLE)

    def gettext_otp_subtitle(self):
        return self.get_element_text(self.OTP_PAGE_SUBTITLE)

    def gettext_otp_edittext(self):
        return self.get_element_text(self.OTP_PAGE_OTP_BOX)

    def ispresent_otp_resend_timer(self):
        return self.is_element_present(self.OTP_PAGE_RESEND_TIMER)

    def gettext_otp_resend_tv(self):
        return self.get_element_text(self.OTP_PAGE_RESEND_TV)

    def click_otp_resend_tv(self):
        self.click_element(self.OTP_PAGE_RESEND_TV)

    def gettext_otp_info(self):
        return self.get_element_text(self.OTP_PAGE_INFO_TV)

    def gettext_otp_change_number(self):
        return self.get_element_text(self.OTP_PAGE_CHANGE_NUMBER)

    def click_otp_change_number(self):
        self.click_element(self.OTP_PAGE_CHANGE_NUMBER)

    def gettext_otp_submit_button(self):
        return self.get_element_text(self.OTP_PAGE_SUBMIT_BUTTON)

    def gettext_otp_detect_tv(self):
        return self.get_element_text(self.OTP_PAGE_DETECT_OTP_TV)

    def gettext_snackbar_tv(self):
        return self.get_element_text(self.SNACKBAR_TV)

    def navigate_back(self):
        self.click_element(self.NAV_BACK)
