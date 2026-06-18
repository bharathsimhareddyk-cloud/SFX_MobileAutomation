import json
import time

import requests

from helper.ApiConstants import LOGIN_SEND_OTP, LOGIN_VERIFY_OTP, GET_REFERRALS, REFRESH_TOKEN, \
    SEARCH_REFERRAL, RIDER_DETAILS, GET_REFERRAL_EARNING, TRAINING_SCOPE, ONBOARDING_PAYMENT_CONFIG, HELP_CATEGORY, \
    RIDER_UPDATES, HELP_CATEGORY_DETAILS
from helper.DBUtils import DBUtil, get_staging_db, fetch_otp_for_mobile
from helper.TestConfigs import TestConfig


def make_post_call(url, data, headers):
    post_response = None
    attempt = 0
    max_retries = 3
    wait_time = 2
    while attempt < max_retries:
        try:
            post_response = requests.post(url, data=json.dumps(data), headers=headers)
            if post_response.status_code in [400]:
                attempt = attempt + 1
                if attempt < max_retries:
                    print("Status code {}.. Retrying in {} seconds".format(post_response.status_code, wait_time))
                    time.sleep(wait_time)
                else:
                    print("Max retries reached.")
            else:
                break
        except requests.exceptions.RequestException as e:
            print('An error occurred : ', e)
    return post_response

def make_put_call(url, data, headers):
    post_response = None
    attempt = 0
    max_retries = 3
    wait_time = 2
    while attempt < max_retries:
        try:
            post_response = requests.put(url, data=json.dumps(data), headers=headers)
            if post_response.status_code in [400]:
                attempt = attempt + 1
                if attempt < max_retries:
                    print("Status code {}.. Retrying in {} seconds".format(post_response.status_code, wait_time))
                    time.sleep(wait_time)
                else:
                    print("Max retries reached.")
            else:
                break
        except requests.exceptions.RequestException as e:
            print('An error occurred : ', e)
    return post_response


def make_get_call(url, data, headers):
    get_response = None
    attempt = 0
    max_retries = 3
    wait_time = 2
    while attempt < max_retries:
        try:
            get_response = requests.get(url, params=data, headers=headers)
            # print(curlify.to_curl(get_response.request))
            # print("Response :::{}".format(get_response.content))
            if get_response.status_code in [400]:
                attempt = attempt + 1
                if attempt < max_retries:
                    print("Status code {}.. Retrying in {} seconds".format(get_response.status_code, wait_time))
                    time.sleep(wait_time)
                else:
                    print("Max retries reached.")
            else:
                break
        except requests.exceptions.RequestException as e:
            print('An error occurred : ', e)
    return get_response


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ApiEngine(metaclass=Singleton):

    def __init__(self, number=None):
        if number is None:
            self.mobile_number = TestConfig().get_config()['mobile_number']
        else:
            self.mobile_number = number

        db = get_staging_db()
        # Fetch the token from expiring token table from DB
        self.rider_id = db.execute_query(
            f"select sfx_rider_id from frodo_staging.RMS_riderinfo where allotted_phone={self.mobile_number}")[
            0]['sfx_rider_id']
        print(self.rider_id)
        login_token_result = db.execute_query(
            f"select `key` from RMS_expiringtoken WHERE object_pk = {self.rider_id}")
        print(login_token_result)
        self.token = login_token_result[0]['key']
        # Call validate token api to refresh the token obtained from db
        self.refresh_token()

    def get_token_by_login_api(self):
        make_post_call(LOGIN_SEND_OTP.get('url'), headers=LOGIN_SEND_OTP.get('headers'),
                       data=LOGIN_SEND_OTP.get('params'))
        db = get_staging_db()
        otp = fetch_otp_for_mobile(TestConfig().get_config().get('mobile_number'))
        verify_otp_data = LOGIN_VERIFY_OTP['params']
        verify_otp_data['OTP'] = otp
        print(otp)
        current_time_milliseconds = int(time.time() * 1000)
        verify_otp_data['init_time'] = current_time_milliseconds
        response = make_post_call(LOGIN_VERIFY_OTP.get('url'), headers=LOGIN_VERIFY_OTP.get('headers'),
                                  data=verify_otp_data)
        print(response.json())
        self.token = response.json()['login_data']['token']

    def get_refferals(self, category=None):
        if category is None:
            category = []
        referral_list = []
        referral_headers = GET_REFERRALS['headers'].copy()
        referral_headers['authorization'] = 'Token ' + self.token
        referral_body = GET_REFERRALS.get('params').copy()
        referral_body['status_list'] = category
        response = make_post_call(GET_REFERRALS.get('url'), headers=referral_headers, data=referral_body)
        response_json = response.json()
        referral_list.extend(response_json['data'])
        no_of_pages = response_json['pages']
        for i in range(1, no_of_pages):
            referral_body['page_no'] = i + 1
            response = make_post_call(GET_REFERRALS.get('url'), headers=referral_headers, data=referral_body)
            response_json = response.json()
            referral_list.extend(response_json['data'])
        return referral_list

    def get_referral_earning(self):
        referral_earning_headers = GET_REFERRAL_EARNING['headers'].copy()
        referral_earning_headers['authorization'] = 'Token ' + self.token
        referral_earning_body = GET_REFERRAL_EARNING.get('params').copy()
        response = make_get_call(GET_REFERRAL_EARNING.get('url'), headers=referral_earning_headers, data=referral_earning_body)
        response_json = response.json()
        return response_json

    def search_refferal(self, query):
        search_referral_list = []
        search_referral_headers = SEARCH_REFERRAL['headers'].copy()
        search_referral_headers['authorization'] = 'Token ' + self.token
        search_referral_body = SEARCH_REFERRAL.get('params').copy()
        search_referral_body['search_text'] = query
        response = make_post_call(SEARCH_REFERRAL.get('url'), headers=search_referral_headers,
                                  data=search_referral_body)
        response_json = response.json()
        search_referral_list.extend(response_json)
        return search_referral_list

    def get_rider_details(self):
        rider_detail_headers = RIDER_DETAILS['headers'].copy()
        rider_detail_headers['authorization'] = 'Token ' + self.token
        rider_detail_body = RIDER_DETAILS.get('params').copy()
        response = make_get_call(RIDER_DETAILS.get('url'), headers=rider_detail_headers, data=rider_detail_body)
        response_json = response.json()
        return response_json

    def get_rider_updates(self, latitude, longitude):
        rider_update_headers = RIDER_UPDATES['headers'].copy()
        rider_update_headers['authorization'] = 'Token ' + self.token
        rider_update_body = RIDER_UPDATES.get('params').copy()
        rider_update_body['latitude'] = latitude
        rider_update_body['longitude'] = longitude
        rider_update_body['is_joining_bonus_enabled'] = False
        response = make_get_call(RIDER_UPDATES.get('url'), headers=rider_update_headers, data=rider_update_body)
        response_json = response.json()
        return response_json

    def refresh_token(self):
        refresh_headers = REFRESH_TOKEN['headers'].copy()
        refresh_headers['authorization'] = 'Token ' + self.token
        refresh_body = REFRESH_TOKEN.get('params').copy()
        refresh_body["allotted_phone"] = self.mobile_number
        refresh_url = REFRESH_TOKEN.get('url')
        refresh_url = refresh_url.format(rider_id=self.rider_id)
        response = make_post_call(refresh_url, headers=refresh_headers, data=refresh_body)
        response_json = response.json()
        self.token = response_json.get('token')

    def get_training_order(self, latitude, longitude):
        training_order_headers = TRAINING_SCOPE['headers'].copy()
        training_order_headers['authorization'] = 'Token ' + self.token
        training_order_body = TRAINING_SCOPE.get('params').copy()
        training_order_body['latitude'] = latitude
        training_order_body['longitude'] = longitude
        print(TRAINING_SCOPE.get('url'))
        print(training_order_headers)
        print(training_order_body)
        response = make_get_call(TRAINING_SCOPE.get('url'), headers=training_order_headers, data=training_order_body)
        response_json = response.json()
        return response_json

    def get_onboarding_payment_config(self):
        onboarding_payment_config_headers = ONBOARDING_PAYMENT_CONFIG['headers'].copy()
        onboarding_payment_config_headers['authorization'] = 'Token ' + self.token
        response = make_get_call(ONBOARDING_PAYMENT_CONFIG.get('url'), headers=onboarding_payment_config_headers, data={})
        response_json = response.json()
        return response_json

    def get_help_categories(self):
        help_category_headers = HELP_CATEGORY['headers'].copy()
        help_category_headers['authorization'] = 'Token ' + self.token
        help_category_body = HELP_CATEGORY.get('params').copy()

        response = make_put_call(HELP_CATEGORY.get('url'), headers=help_category_headers, data=help_category_body)
        response_json = response.json()
        return response_json

    def get_help_category_details(self, category_id):
        help_category_details_headers = HELP_CATEGORY_DETAILS['headers'].copy()
        help_category_details_headers['authorization'] = 'Token ' + self.token
        help_category_details_body = HELP_CATEGORY_DETAILS.get('params').copy()

        response = make_post_call(HELP_CATEGORY_DETAILS.get('url').format(category_id), headers=help_category_details_headers,
                                  data=help_category_details_body)
        response_json = response.json()
        return response_json