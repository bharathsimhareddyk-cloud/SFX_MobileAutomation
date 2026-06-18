APP_CONSTANTS = {
    'app_id': 'in.shadowfax.gandalf.staging',
    'activity_id': 'in.shadowfax.gandalf.MainActivity'
}

# Device Configurations
# DEVICE_CONFIGS = {
#     'real_device': {
#         "platformName": "Android",
#         "deviceName": "your_phone_serial",  # real device
#         "appPackage": APP_CONSTANTS['app_id'],
#         "appActivity": APP_CONSTANTS['activity_id'],
#         "noReset": True
#     },
#     'emulator': {
#         "platformName": "Android",
#         "deviceName": "emulator-5554",      # emulator name from adb devices
#         "appPackage": APP_CONSTANTS['app_id'],
#         "appActivity": APP_CONSTANTS['activity_id'],
#         "noReset": True
#     }
# }

# "Food delivery mode"
RIDER_CONFIG = {
    'mobile_number': {
        'food delivery': '7013779790'
    },
    'api-key': 'sgXeeoxo8dQ_YXHtSPofrmGosi8TKOYWmsixUhf1uPU58ZFhG5u3U4x8',
    'device-id': '10b82b23fe20b617',
    'version': '616',
    'version-name': '25.10'
}


ALREADY_REFERRED_NUMBER = "1234567890"


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TestConfig(metaclass=Singleton):

    def __init__(self):
        self.rider_type = 'food delivery'

    def get_config(self):
        rider_config = RIDER_CONFIG.copy()
        rider_config['mobile_number'] = rider_config['mobile_number'][self.rider_type]
        return rider_config

    def set_type(self, new_type):
        self.rider_type = new_type
