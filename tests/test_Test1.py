## @file Test1.py
# @author weaves
# @brief Unittest of modules
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

from ldr import Schema

## A test driver for modules
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
    def test_000(self):
        self.assertIsNotNone(self.test0)
        return

    _schema = None

    ## Test we can create a Schema object.
    def test_003(self):
        schema = Schema(desc = "sales")
        self.assertIsNotNone(schema)
        self.logger.info("schema: {0:s}".format(str(schema)))
        self._schema = schema
        self.logger.info("schema: desc: {0:s}".format(str(schema.desc)))
        return

    ## Build a schema by calling the prior test and check it.
    def test_005(self):
        self.test_003()
        self.assertIsNotNone(self._schema)
        self.logger.info("schema: {0:s}".format(str(self._schema)))
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
