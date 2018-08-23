import unittest

from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover(start_dir='githubcommit', pattern='*_test.py')
    if is_running_under_teamcity():
        TeamcityTestRunner().run(all_tests)
    else:
        unittest.TextTestRunner().run(all_tests)