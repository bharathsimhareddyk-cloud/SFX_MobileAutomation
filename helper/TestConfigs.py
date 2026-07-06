import os
from dotenv import load_dotenv

load_dotenv()

# ── App Constants ─────────────────────────────────────────────────────────────
APP_CONSTANTS = {
    'app_id'     : os.getenv('APP_ID'),
    'activity_id': os.getenv('ACTIVITY_ID')
}

# ── Rider Config ──────────────────────────────────────────────────────────────
RIDER_CONFIG = {
    'mobile_number': {
        'food delivery': os.getenv('MOBILE_NUMBER_FOOD_DELIVERY')
    },
    'api-key'     : os.getenv('API_KEY'),
    'device-id'   : os.getenv('DEVICE_ID'),
    'version'     : os.getenv('VERSION'),
    'version-name': os.getenv('VERSION_NAME')
}

# ── Test Data ─────────────────────────────────────────────────────────────────
ALREADY_REFERRED_NUMBER = os.getenv('ALREADY_REFERRED_NUMBER')


# ── Singleton Metaclass ───────────────────────────────────────────────────────
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


# ── Test Config ───────────────────────────────────────────────────────────────
class TestConfig(metaclass=Singleton):

    def __init__(self):
        self.rider_type = 'food delivery'

    def get_config(self):
        config                  = RIDER_CONFIG.copy()
        config['mobile_number'] = config['mobile_number'][self.rider_type]
        return config

    def set_type(self, new_type):
        self.rider_type = new_type