import unittest

from HtmlTestRunner import HTMLTestRunner
from helper.TestConfigs import RIDER_CONFIG, TestConfig
from tests.LoginTest import LoginTest

# Uncomment to enable additional test suites
# from tests.EarningsTest        import EarningsTest
# from tests.HomePageTest        import HomePageTest
# from tests.ReferAndEarnTest    import ReferAndEarnTest
# from tests.SlotsTest           import SlotsTest
# from tests.MyProfileTest       import MyProfileTest
# from tests.MyDocumentsTest     import MyDocumentsTest
# from tests.HelpTest            import HelpTest


# ── Test Filter ───────────────────────────────────────────────────────────────
def add_tests_for_rider(suite, test_case_class, rider):
    """
    Adds tests to the suite based on rider type naming convention:
      - 'rider_type_all'    → always added
      - 'rider_type_<name>' → added only if <name> matches rider
      - no 'rider_type_'    → added only for 'default' rider
    """
    loader     = unittest.TestLoader()
    test_names = loader.getTestCaseNames(test_case_class)

    for name in test_names:
        if 'rider_type_all' in name:
            suite.addTest(test_case_class(name))
        elif 'rider_type_' in name:
            if name.split('rider_type_')[1] == rider:
                suite.addTest(test_case_class(name))
        elif rider == 'default':
            suite.addTest(test_case_class(name))


# ── Test Runner ───────────────────────────────────────────────────────────────
def run_test_suite():
    skip_users = []  # add rider types here to skip e.g. ['onb_pnd', 'fdm']

    for rider_type in RIDER_CONFIG['mobile_number'].keys():
        if rider_type in skip_users:
            continue

        TestConfig().set_type(rider_type)
        suite = unittest.TestSuite()

        # ── Active Tests ──────────────────────────────────────────────────────
        add_tests_for_rider(suite, LoginTest, rider_type)

        # ── Inactive Tests (uncomment to enable) ──────────────────────────────
        # add_tests_for_rider(suite, HomePageTest,     rider_type)
        # add_tests_for_rider(suite, EarningsTest,     rider_type)
        # add_tests_for_rider(suite, ReferAndEarnTest, rider_type)
        # add_tests_for_rider(suite, SlotsTest,        rider_type)
        # add_tests_for_rider(suite, MyProfileTest,    rider_type)
        # add_tests_for_rider(suite, MyDocumentsTest,  rider_type)
        # add_tests_for_rider(suite, HelpTest,         rider_type)

        runner = HTMLTestRunner(
            combine_reports  = True,
            open_in_browser  = False,
            report_name      = rider_type
        )
        runner.run(suite)


# ── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == '__main__':
    run_test_suite()