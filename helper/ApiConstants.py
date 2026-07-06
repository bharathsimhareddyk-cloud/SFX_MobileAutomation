from helper.TestConfigs import TestConfig, RIDER_CONFIG

# ── Base URLs ─────────────────────────────────────────────────────────────────
BASE_URL     = 'https://frodo.staging.shadowfax.in/'
RMS_BASE_URL = 'https://rms-backend.staging.shadowfax.in/'

# ── Common Headers ────────────────────────────────────────────────────────────
COMMON_HEADER = {
    'Content-Type' : 'application/json; charset=utf-8',
    'api-key'      : RIDER_CONFIG.get('api-key'),
    'authorization': 'Token',
    'device-id'    : RIDER_CONFIG.get('device-id'),
    'locale'       : 'en',
    'referrer'     : 'Rider-app-Android',
    'version'      : RIDER_CONFIG.get('version'),
    'version-name' : RIDER_CONFIG.get('version-name')
}

# ── Login ─────────────────────────────────────────────────────────────────────
LOGIN_SEND_OTP = {
    'url'    : BASE_URL + 'app/v5/send-otp/',
    'headers': COMMON_HEADER,
    'params' : {
        'allotted_phone': ''
    }
}

LOGIN_VERIFY_OTP = {
    'url'    : BASE_URL + 'app/v5/verify-otp/',
    'headers': COMMON_HEADER,
    'params' : {
        'allotted_phone'  : '',
        'utm_params'      : '{"utm_source":"google-play&utm_medium=organic", "utm_medium":"organic"}',
        'app_version_code': int(RIDER_CONFIG.get('version'))
    }
}

# ── Refer and Earn ────────────────────────────────────────────────────────────
GET_REFERRALS = {
    'url'    : BASE_URL + 'app/v1/referrals/',
    'headers': COMMON_HEADER,
    'params' : {
        'status_list': [],
        'page_no'    : 1,
        'num_results': 10
    }
}

GET_REFERRAL_EARNING = {
    'url'    : BASE_URL + 'app/v2/referral/summary/',
    'headers': dict(COMMON_HEADER, referrer='Rider-app-Android'),
    'params' : {
        'size': 'xxhdpi'
    }
}

SEARCH_REFERRAL = {
    'url'    : BASE_URL + 'app/v1/referral/search/',
    'headers': COMMON_HEADER,
    'params' : {
        'search_text': ''
    }
}

# ── General ───────────────────────────────────────────────────────────────────
RIDER_DETAILS = {
    'url'    : BASE_URL + 'app/v1/rider-details/',
    'headers': COMMON_HEADER,
    'params' : {
        'version'         : RIDER_CONFIG['version'],
        'rider_basic_info': 'true'
    }
}

REFRESH_TOKEN = {
    'url'    : BASE_URL + 'app/v5/{rider_id}/validate_token/',
    'headers': COMMON_HEADER,
    'params' : {
        'allotted_phone': ''
    }
}

TRAINING_SCOPE = {
    'url'    : BASE_URL + 'app/v1/fetch_training_scope/',
    'headers': COMMON_HEADER,
    'params' : {
        'latitude' : '',
        'longitude': ''
    }
}

RIDER_UPDATES = {
    'url'    : RMS_BASE_URL + 'app/v2/rider-updates/',
    'headers': COMMON_HEADER,
    'params' : {
        'latitude'                : '',       # note: was 'latitide' (typo fixed)
        'longitude'               : '',
        'is_joining_bonus_enabled': ''
    }
}

ONBOARDING_PAYMENT_CONFIG = {
    'url'    : BASE_URL + 'app/v1/payment/onboarding-payment-config/',
    'headers': COMMON_HEADER,
    'params' : {}
}

HELP_CATEGORY = {
    'url'    : BASE_URL + 'app/v1/help_section_categories/',
    'headers': COMMON_HEADER,
    'params' : {
        'payout_type': '',
        'source'     : 1
    }
}

HELP_CATEGORY_DETAILS = {
    'url'    : BASE_URL + 'app/v1/category/{}/details/',
    'headers': COMMON_HEADER,
    'params' : {
        'payout_type': ''
    }
}