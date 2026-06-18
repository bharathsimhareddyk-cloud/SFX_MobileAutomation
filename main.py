import subprocess
import unittest

from HtmlTestRunner import HTMLTestRunner
from helper.TestConfigs import RIDER_CONFIG, TestConfig
# from tests.EarningsTest import EarningsTest
# from tests.HomePageTest import HomePageTest
from tests.LoginTest import LoginTest
from helper.TestConfigs import TestConfig, RIDER_CONFIG


# from tests.MyDocumentsTest import MyDocumentsTest
# from tests.MyProfileTest import MyProfileTest
# from tests.ReferAndEarnTest import ReferAndEarnTest
# from tests.SlotsTest import SlotsTest
# from tests.HelpTest import HelpTest

def add_tests_specific_to_rider_type(suite, test_case_class, rider):
    loader = unittest.TestLoader()
    test_list = loader.getTestCaseNames(test_case_class)
    for name in test_list:
        add_test = False
        # For non default rider, test to be added only if test name has string "rider_type_<rider>"
        if 'rider_type_' in name:
            if name.split('rider_type_')[1] == rider:
                add_test = True
        # If test name does not have string "rider_type", add the test only if rider is default
        else:
            if rider == 'default':
                add_test = True

        if 'rider_type_all' in name:
            add_test = True

        if add_test:
            suite.addTest(test_case_class(name))

def run_test_suite():
    # subprocess.run("adb shell pm clear in.shadowfax.gandalf.staging", shell=True)
    # skip_users = ['default', 'onb_pnd', 'btdm_upnd', 'btdm_uapr', 'fdm']
    skip_users = []
    for rider_type in RIDER_CONFIG['mobile_number'].keys():
        if rider_type in skip_users:
            continue
        TestConfig().set_type(rider_type)
        # Preparing test suite (order of tests to run)
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()

        # Add tests based on rider type
        add_tests_specific_to_rider_type(suite, LoginTest, rider_type)

        # All below tests assume login test is performed.
        # add_tests_specific_to_rider_type(suite, HomePageTest, rider_type)
        # add_tests_specific_to_rider_type(suite, EarningsTest, rider_type)
        # add_tests_specific_to_rider_type(suite, ReferAndEarnTest, rider_type)
        # add_tests_specific_to_rider_type(suite, SlotsTest, rider_type)
        # add_tests_specific_to_rider_type(suite, MyProfileTest, rider_type)
        # add_tests_specific_to_rider_type(suite, MyDocumentsTest, rider_type)
        # add_tests_specific_to_rider_type(suite, HelpTest, rider_type)

        # Configure runner and run the suite
        runner = HTMLTestRunner(combine_reports=True, open_in_browser=False, report_name=rider_type)
        runner.run(suite)


# If called from shell, execute this
if __name__ == '__main__':
    run_test_suite()
