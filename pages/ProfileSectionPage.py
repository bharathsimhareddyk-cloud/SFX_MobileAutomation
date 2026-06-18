from appium.webdriver.common.appiumby import AppiumBy
from helper.BasePage import BasePage


class ProfileSectionPage(BasePage):

    HAMBURGER_MENU = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
    PROFILE_NAVIGATION_BUTTON = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/profile_chevron')
    PERSONAL_INFO = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/personal_info')
    BACK_BUTTON=(AppiumBy.ID,'in.shadowfax.gandalf.staging:id/back')
    MY_DOCUMENTS=(AppiumBy.ID,'in.shadowfax.gandalf.staging:id/document')
    BANK_ACCOUNT=(AppiumBy.ID,'in.shadowfax.gandalf.staging:id/bank_account')
    SIGN_OUT = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/signout')
    SHADOWFAX_KIT=(AppiumBy.ID,'in.shadowfax.gandalf.staging:id/kit_chevron')
    TERMS_AND_CONDITIONS=(AppiumBy.ID,'in.shadowfax.gandalf.staging:id/tnc_chevron')
    WHATSAPP_TOGGLE=(AppiumBy.ID,'in.shadowfax.gandalf.staging:id/whatsapp_toggle')


    def click_hamburger_menu(self):             # ✅ was missing
        self.click_element(self.HAMBURGER_MENU)

    def click_profile_navigation_button(self):  # ✅ was missing
        self.click_element(self.PROFILE_NAVIGATION_BUTTON)

    def click_personalinfo(self):
        self.click_element(self.PERSONAL_INFO)


    def click_back(self):
            self.click_element(self.BACK_BUTTON)

    def click_my_documents(self):
        self.click_element(self.MY_DOCUMENTS)

    def click_bank_account(self):
        self.click_element(self.BANK_ACCOUNT)

    def click_shadowfax_kit(self):
        self.click_element(self.SHADOWFAX_KIT)

    def click_terms_and_conditions(self):
        self.click_element(self.TERMS_AND_CONDITIONS)

    def click_whatsapp_toggle(self):
      self.click_element(self.WHATSAPP_TOGGLE)

    def click_sign_out(self):
        self.click_element(self.SIGN_OUT)

    def click_home_view(self):
        pass



