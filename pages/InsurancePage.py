from appium.webdriver.common.appiumby import AppiumBy
from helper.BasePage import BasePage


class InsurancePage(BasePage):
    HAMBURGER_MENU = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
    INSURANCE = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="in.shadowfax.gandalf.staging:id/main"])[2]')
    HELP = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/help_tv')
    INSURANCE_RELATED_ISSUE = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/help_issues_chevron_icon')
    RADIOBUTTON_ISSUE_DETAIL_LIST = (AppiumBy.XPATH,
                                     '//android.widget.RadioButton[@text="I met with an accident. How do I claim Insurance"]')
    NEXT_ISSUE_CONFIRM = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/btn_issue_confirm')
    NAVIGATE_BACK = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
    YOUR_TICKETS = (AppiumBy.XPATH, '//android.widget.TextView[@text="YOUR TICKETS"]')
    ISSUES = (AppiumBy.XPATH, '//android.widget.TextView[@text="ISSUES"]')
    FAQ = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/tv_faq')
    CLOSE = (AppiumBy.ID, 'com.android.chrome:id/close_button')
    HELP_BACK_BUTTON = (AppiumBy.XPATH,
                        '//android.widget.TextView[@resource-id="in.shadowfax.gandalf.staging:id/title"]')
    VIEW_INSURANCE_DETAILS = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/btn_start_insurance')
    ACCEPT = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/accept')
    BACK_BUTTON = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/back')
    HOME_VIEW = (AppiumBy.ID, 'in.shadowfax.gandalf.staging:id/navigation_bar_item_large_label_view')

    # NAVIGATE_BACK = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
    # NAVIGATE_BACK = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')

    def click_hamburger_menu(self):  # ✅ was missing
        self.click_element(self.HAMBURGER_MENU)

    def click_insurance(self):
        self.click_element(self.INSURANCE)

    def click_help(self):
        self.click_element(self.HELP)

    def click_insurance_related_issue(self):
        self.click_element(self.INSURANCE_RELATED_ISSUE)

    def click_radiobutton_issue_detail_list(self):
        self.click_element(self.RADIOBUTTON_ISSUE_DETAIL_LIST)

    def click_next_issue_confirm(self):
        self.click_element(self.NEXT_ISSUE_CONFIRM)

    def click_navigate_back(self):
        self.click_element(self.NAVIGATE_BACK)

    def click_your_tickets(self):
        self.click_element(self.YOUR_TICKETS)

    def click_issues(self):
        self.click_element(self.ISSUES)

    def click_faq(self):
        self.click_element(self.FAQ)

    def click_close(self):
        self.click_element(self.CLOSE)

    def click_help_back_button(self):
        self.click_element(self.HELP_BACK_BUTTON)

    def click_view_insurance_details(self):
        self.click_element(self.VIEW_INSURANCE_DETAILS)

    def click_accept(self):
        self.click_element(self.ACCEPT)

    def click_back(self):
        self.click_element(self.BACK_BUTTON)

    def click_home_view(self):
        self.click_element(self.HOME_VIEW)

    # def click_navigate_back(self):
    #     self.click_element(self.NAVIGATE_BACK)
