import subprocess
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options

from helper.TestConfigs import APP_CONSTANTS

# ── Appium Server ─────────────────────────────────────────────────────────────
APPIUM_SERVER_URL = 'http://localhost:4723/wd/hub'

# ── Driver Capabilities ───────────────────────────────────────────────────────
BASE_CAPABILITIES = {
    'platformName'                      : 'Android',
    'automationName'                    : 'uiautomator2',
    'appPackage'                        : APP_CONSTANTS['app_id'],
    'appActivity'                       : APP_CONSTANTS['activity_id'],
    'autoGrantPermissions'              : True,
    'autoDismissAlerts'                 : True,
    'noReset'                           : True,
    'newCommandTimeout'                 : 300,
    'adbExecTimeout'                    : 60000,
    'androidDeviceReadyTimeout'         : 60,
    'uiautomator2ServerLaunchTimeout'   : 60000,
    'uiautomator2ServerInstallTimeout'  : 60000,
    'androidInstallTimeout'             : 90000,
    'appWaitDuration'                   : 60000,
    'enableImageInjection'              : True,
    'imageMatchSettings'                : {'mode': 'accurate'},
}


# ── Singleton Metaclass ───────────────────────────────────────────────────────
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

    @property
    def instances(self):
        return self._instances


# ── Android Driver ────────────────────────────────────────────────────────────
class AndroidDriver(metaclass=Singleton):

    def __init__(self):
        self.android_driver = None

    def get_android_driver(self):
        if self.android_driver is None:
            self._start_session()
        return self.android_driver

    def terminate_app(self):
        if self.android_driver is not None:
            self.android_driver.quit()
            self.android_driver = None
            AndroidDriver._instances.pop(AndroidDriver, None)

    @staticmethod
    def clear_app_data():
        subprocess.run(
            ['adb', 'shell', 'pm', 'clear', APP_CONSTANTS['app_id']],
            capture_output=True,
            text=True,
            timeout=30
        )

    # ── Private ───────────────────────────────────────────────────────────────
    def _start_session(self):
        capabilities = BASE_CAPABILITIES.copy()

        udid = self._get_connected_device_udid()
        if udid:
            capabilities['udid'] = udid

        options = UiAutomator2Options().load_capabilities(capabilities)
        options.set_capability('appium:forceAppLaunch', True)

        self.android_driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
        time.sleep(2)

    @staticmethod
    def _get_connected_device_udid():
        try:
            result = subprocess.run(
                ['adb', 'devices'],
                capture_output=True,
                text=True,
                check=True,
                timeout=10
            )
        except (subprocess.SubprocessError, FileNotFoundError):
            return None

        lines   = result.stdout.strip().splitlines()[1:]
        devices = [line.split()[0] for line in lines if line.strip().endswith('device')]
        return devices[0] if devices else None