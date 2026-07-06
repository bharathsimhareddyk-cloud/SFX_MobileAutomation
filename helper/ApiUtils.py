import json
import time

import requests

from helper.ApiConstants import (
    LOGIN_SEND_OTP, LOGIN_VERIFY_OTP,
    GET_REFERRALS, GET_REFERRAL_EARNING, SEARCH_REFERRAL,
    RIDER_DETAILS, RIDER_UPDATES, REFRESH_TOKEN,
    TRAINING_SCOPE, ONBOARDING_PAYMENT_CONFIG,
    HELP_CATEGORY, HELP_CATEGORY_DETAILS
)
from helper.DBUtils import DBUtil, get_staging_db, fetch_otp_for_mobile
from helper.TestConfigs import TestConfig

# ── Retry Config ──────────────────────────────────────────────────────────────
MAX_RETRIES = 3
WAIT_TIME   = 2
RETRY_CODES = [400]


# ── HTTP Helpers ──────────────────────────────────────────────────────────────
def _make_request(method, url, data, headers):
    """Generic retry wrapper for HTTP requests."""
    response = None
    for attempt in range(MAX_RETRIES):
        try:
            if method == 'GET':
                response = requests.get(url, params=data, headers=headers)
            elif method == 'POST':
                response = requests.post(url, data=json.dumps(data), headers=headers)
            elif method == 'PUT':
                response = requests.put(url, data=json.dumps(data), headers=headers)

            if response.status_code in RETRY_CODES:
                if attempt < MAX_RETRIES - 1:
                    print(f"Status {response.status_code} — retrying in {WAIT_TIME}s...")
                    time.sleep(WAIT_TIME)
                else:
                    print("Max retries reached.")
            else:
                break

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    return response


def make_get_call(url, data, headers):
    return _make_request('GET', url, data, headers)

def make_post_call(url, data, headers):
    return _make_request('POST', url, data, headers)

def make_put_call(url, data, headers):
    return _make_request('PUT', url, data, headers)


# ── Singleton Metaclass ───────────────────────────────────────────────────────
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


# ── API Engine ────────────────────────────────────────────────────────────────
class ApiEngine(metaclass=Singleton):

    def __init__(self, number=None):
        self.mobile_number = number or TestConfig().get_config()['mobile_number']

        db            = get_staging_db()
        self.rider_id = db.execute_query(
            f"SELECT sfx_rider_id FROM frodo_staging.RMS_riderinfo "
            f"WHERE allotted_phone={self.mobile_number}"
        )[0]['sfx_rider_id']

        token_result = db.execute_query(
            f"SELECT `key` FROM RMS_expiringtoken WHERE object_pk={self.rider_id}"
        )
        self.token = token_result[0]['key']
        self.refresh_token()

    # ── Auth ──────────────────────────────────────────────────────────────────
    def get_token_by_login_api(self):
        make_post_call(LOGIN_SEND_OTP['url'], LOGIN_SEND_OTP['params'], LOGIN_SEND_OTP['headers'])

        otp  = fetch_otp_for_mobile(TestConfig().get_config().get('mobile_number'))
        body = LOGIN_VERIFY_OTP['params'].copy()
        body['OTP']       = otp
        body['init_time'] = int(time.time() * 1000)

        response   = make_post_call(LOGIN_VERIFY_OTP['url'], body, LOGIN_VERIFY_OTP['headers'])
        self.token = response.json()['login_data']['token']

    def refresh_token(self):
        headers                  = self._auth_headers(REFRESH_TOKEN)
        body                     = REFRESH_TOKEN['params'].copy()
        body['allotted_phone']   = self.mobile_number
        url                      = REFRESH_TOKEN['url'].format(rider_id=self.rider_id)

        response   = make_post_call(url, body, headers)
        self.token = response.json().get('token')

    # ── Referrals ─────────────────────────────────────────────────────────────
    def get_referrals(self, category=None):
        headers              = self._auth_headers(GET_REFERRALS)
        body                 = GET_REFERRALS['params'].copy()
        body['status_list']  = category or []

        response      = make_post_call(GET_REFERRALS['url'], body, headers)
        response_json = response.json()
        referral_list = list(response_json['data'])

        for page in range(1, response_json['pages']):
            body['page_no'] = page + 1
            response_json   = make_post_call(GET_REFERRALS['url'], body, headers).json()
            referral_list.extend(response_json['data'])

        return referral_list

    def get_referral_earning(self):
        headers = self._auth_headers(GET_REFERRAL_EARNING)
        body    = GET_REFERRAL_EARNING['params'].copy()
        return make_get_call(GET_REFERRAL_EARNING['url'], body, headers).json()

    def search_referral(self, query):
        headers              = self._auth_headers(SEARCH_REFERRAL)
        body                 = SEARCH_REFERRAL['params'].copy()
        body['search_text']  = query
        return make_post_call(SEARCH_REFERRAL['url'], body, headers).json()

    # ── Rider ─────────────────────────────────────────────────────────────────
    def get_rider_details(self):
        headers = self._auth_headers(RIDER_DETAILS)
        body    = RIDER_DETAILS['params'].copy()
        return make_get_call(RIDER_DETAILS['url'], body, headers).json()

    def get_rider_updates(self, latitude, longitude):
        headers                          = self._auth_headers(RIDER_UPDATES)
        body                             = RIDER_UPDATES['params'].copy()
        body['latitude']                 = latitude
        body['longitude']                = longitude
        body['is_joining_bonus_enabled'] = False
        return make_get_call(RIDER_UPDATES['url'], body, headers).json()

    # ── Training ──────────────────────────────────────────────────────────────
    def get_training_order(self, latitude, longitude):
        headers             = self._auth_headers(TRAINING_SCOPE)
        body                = TRAINING_SCOPE['params'].copy()
        body['latitude']    = latitude
        body['longitude']   = longitude
        return make_get_call(TRAINING_SCOPE['url'], body, headers).json()

    # ── Onboarding ────────────────────────────────────────────────────────────
    def get_onboarding_payment_config(self):
        headers = self._auth_headers(ONBOARDING_PAYMENT_CONFIG)
        return make_get_call(ONBOARDING_PAYMENT_CONFIG['url'], {}, headers).json()

    # ── Help ──────────────────────────────────────────────────────────────────
    def get_help_categories(self):
        headers = self._auth_headers(HELP_CATEGORY)
        body    = HELP_CATEGORY['params'].copy()
        return make_put_call(HELP_CATEGORY['url'], body, headers).json()

    def get_help_category_details(self, category_id):
        headers = self._auth_headers(HELP_CATEGORY_DETAILS)
        body    = HELP_CATEGORY_DETAILS['params'].copy()
        url     = HELP_CATEGORY_DETAILS['url'].format(category_id)
        return make_post_call(url, body, headers).json()

    # ── Private Helper ────────────────────────────────────────────────────────
    def _auth_headers(self, api_constant):
        """Returns headers with Authorization token injected."""
        headers                  = api_constant['headers'].copy()
        headers['authorization'] = f'Token {self.token}'
        return headers