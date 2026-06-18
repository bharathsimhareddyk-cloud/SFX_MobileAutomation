from appium.webdriver.common.appiumby import AppiumBy

from helper.BasePage import BasePage


class PermissionsAndLanguagePage(BasePage):
    ALLOW_FOREGROUND_ONLY_BUTTON = (
        AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    )
    ALLOW_PERMISSION_BUTTON = (
        AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button"
    )
    DENY_PERMISSION_BUTTON = (
        AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button"
    )

    LANGUAGE_OPTIONS = {
        "English": (
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[1]",
        ),
        "Hindi": (
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[2]",
        ),
        "Kannada": (
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[3]",
        ),
        "Hinglish": (
            AppiumBy.XPATH,
            "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[4]",
        ),
    }

    SUBMIT_BUTTON = (AppiumBy.XPATH, "//android.widget.Button")

    def __init__(self, driver):
        super().__init__(driver)

    def allow_device_location(self):
        if self.is_element_present(self.ALLOW_FOREGROUND_ONLY_BUTTON):
            self.click_element(self.ALLOW_FOREGROUND_ONLY_BUTTON)

    def allow_permissions(self):
        self.allow_device_location()
        if self.is_element_present(self.ALLOW_PERMISSION_BUTTON):
            self.click_element(self.ALLOW_PERMISSION_BUTTON)

    def deny_permissions(self):
        if self.is_element_present(self.DENY_PERMISSION_BUTTON):
            self.click_element(self.DENY_PERMISSION_BUTTON)

    def select_preferred_language_new_ui(self, language="English"):
        self.click_element(self.LANGUAGE_OPTIONS[language])
        self.click_submit()

    def click_submit(self):
        self.click_element(self.SUBMIT_BUTTON)
