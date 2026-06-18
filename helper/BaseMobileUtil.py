import subprocess
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options

from helper.TestConfigs import APP_CONSTANTS


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    @property
    def instances(self):
        return self._instances


class AndroidDriver(metaclass=Singleton):

    def __init__(self):
        self.android_driver = None

    def get_android_driver(self):
        if self.android_driver is not None:
            return self.android_driver
        self.start_server()
        return self.android_driver

    def terminate_app(self):
        if self.android_driver is not None:
            self.android_driver.quit()
            self.android_driver = None
            AndroidDriver._instances.pop(AndroidDriver, None)

    @staticmethod
    def clear_app_data():
        subprocess.run(
            ["adb", "shell", "pm", "clear", APP_CONSTANTS['app_id']],
            capture_output=True,
            text=True,
            timeout=30,
        )

    def start_server(self):
        device_path = "http://localhost:4723/wd/hub"
        desired_configuration = dict(
            platformName='Android',
            automationName='uiautomator2',
            appPackage=APP_CONSTANTS['app_id'],
            appActivity=APP_CONSTANTS['activity_id'],
            autoGrantPermissions=True,
            autoDismissAlerts=True,
            noReset=True,
            newCommandTimeout=300,
            adbExecTimeout=60000,
            androidDeviceReadyTimeout=60,
            uiautomator2ServerLaunchTimeout=60000,
            uiautomator2ServerInstallTimeout=60000,
            androidInstallTimeout=90000,
            appWaitDuration=60000,
            enableImageInjection=True,
            imageMatchSettings={"mode": "accurate"},
        )

        udid = self._get_connected_device_udid()
        if udid:
            desired_configuration['udid'] = udid

        desired_options = UiAutomator2Options().load_capabilities(desired_configuration)
        desired_options.set_capability("appium:forceAppLaunch", True)
        self.android_driver = webdriver.Remote(device_path, options=desired_options)
        time.sleep(2)

    @staticmethod
    def _get_connected_device_udid():
        try:
            completed = subprocess.run(
                ["adb", "devices"],
                capture_output=True,
                text=True,
                check=True,
                timeout=10,
            )
        except (subprocess.SubprocessError, FileNotFoundError):
            return None

        lines = completed.stdout.strip().splitlines()[1:]
        devices = [line.split()[0] for line in lines if line.strip().endswith("device")]
        return devices[0] if devices else None