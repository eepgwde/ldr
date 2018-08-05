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

from ldr import Schema, Filter

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
        schema = Schema(desc = "fx")
        self.assertIsNotNone(schema)
        self.logger.info("schema: {0:s}".format(str(schema)))
        self._schema = schema
        self.logger.info("schema: desc: {0:s}".format(str(schema.desc)))
        return

    ## Build a schema by calling the previous test for the schema.
    def test_005(self):
        self.test_003()

        self._filter = Filter("tests/media/gbp-usd.csv", self._schema)
        self.assertIsNotNone(self._filter._data)
        return

    ## And check the names of the date index and the value.
    def test_007(self):
        self.test_005()

        d0 = self._filter.series("datetime", index=True)
        self.assertIsNotNone(d0)
        self.logger.info("filter: datetime: {0:s} {1:s}".
                         format(str(type(d0)), d0.dtype.kind) )

        d0 = self._filter.series("value")
        self.assertIsNotNone(d0)
        self.assertEqual(d0.name, "fx")
        self.assertEqual(d0.index.name, "dt0")
        self.logger.info("filter: datetime: {0:s} {1:s}".
                         format(str(type(d0)), d0.dtype.kind) )


        return

    def test_009(self):
        schema = Schema(desc = "fx-datahub")
        self.assertIsNotNone(schema)
        self.logger.info("schema: {0:s}".format(str(schema)))
        self._schema = schema
        self.logger.info("schema: desc: {0:s}".format(str(schema.desc)))
        return

    ## Build a schema by calling the previous test for the schema.
    def test_011(self):
        self.test_009()

        self._filter = Filter("tests/media/usd-gbp.csv", self._schema)
        self.assertIsNotNone(self._filter._data)
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
