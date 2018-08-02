## @file Test1.py
# @author weaves
# @brief Unittest of MInfo
#
# This module tests the ancillary operations and the 
# 
# @note
#
# Relatively complete test.

import sys, logging, os

from datetime import datetime, timezone, timedelta, date

from collections import Counter

import unittest
from tests.test_Test import Test

## A test driver for GMus0
#
# @see GMus0
class Test1(Test):
    """
    Test MInfo1
    """

    ## Null setup. Create a new one.
    def setUp(self):
        super(Test1, self).setUp()
        return

    ## Null setup.
    def tearDown(self):
        self.logger.info('tearDown')
        return

    ## Loaded?
    ## Is utf-8 available as a unittest.TestCasefilesystemencoding()
    def test_000(self):
        self.assertIsNotNone(self.test0)
        return

    def test_05(self):
        self.assertIsNotNone(self.test0)
        return

#
# The sys.argv line will complain to you if you run it with ipython
# emacs. The ipython arguments are passed to unittest.main.

if __name__ == '__main__':
    if len(sys.argv) and "ipython" not in sys.argv[0]:
        # If this is not ipython, run as usual
        unittest.main(sys.argv)
    else:
        # If not remove the command-line arguments.
        sys.argv = [sys.argv[0]]
        unittest.main(module='Test1', verbosity=3, failfast=True, exit=False)
