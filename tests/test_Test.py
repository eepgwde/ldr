"""
Test file for the ldr modules.

Don't forget to test a large file.

"""
## @file Test.py
# @author weaves
# @brief Unittest
#
# @note
#
# Relatively complete test.

import sys, logging, os

import pandas as pd

from datetime import datetime, timezone, timedelta, date

from collections import Counter

import unittest

from ldr import Filter, Selector, Schema
from ingresso import Sales0

logfile = os.environ['X_LOGFILE'] if os.environ.get('X_LOGFILE') is not None else "test.log"
logging.basicConfig(filename=logfile, level=logging.DEBUG)
logger = logging.getLogger('Test')
sh = logging.StreamHandler()
logger.addHandler(sh)

media0 = os.path.join(os.path.dirname(__file__), "media")
trs0 = os.path.join(os.path.dirname(__file__), "p1.lst")

def postprocess0(f0):
    f0.series("datetime", index=True)
    return f0.series("value")

class Test(unittest.TestCase):
    """
    A source directory dir0 is taken from the environment as SDIR or 
    is tests/media and should contain .m4a files.
    A file tests/p1.lst is also needed. It can list the files in the
    directory.
    """
    test0 = None
    dir0 = None
    files0 = []
    files = []
    logger = None

    sources = { "fx": [ "tests/media/gbp-usd.csv", Schema(desc = "fx") ],
                "fx2": [ "tests/media/gbp-usd2.csv", Schema(desc = "fx-fxcm") ],
                "sales": [ "tests/media/sales.csv", Schema(desc = "sales") ],  
                "weather": [ "tests/media/london.csv", Schema(desc = "weather") ],
                "weather2": [ "tests/media/metoffice.csv", Schema(desc = "weather-metoffice") ] }
    
    ## Sets pandas options and logging.
    @classmethod
    def setUpClass(cls):
        global logger
        cls.logger = logger
        global media0
        cls.dir0 = os.environ['SDIR'] if os.environ.get('SDIR') is not None else media0
        
        for root, dirs, files in os.walk(cls.dir0, topdown=True):
            for name in files:
                cls.files.append(os.path.join(root, name))

        cls.files.sort()
        cls.files0 = cls.files
        cls.logger.info('files: ' + '; '.join(cls.files))
    
    ## Logs out.
    @classmethod
    def tearDownClass(cls):
        pass

    ## Null setup. Create a new one.
    def setUp(self):
        self.logger.info('setup')
        if not type(self).files:
            type(self).files = type(self).files0
            
        self.file0, *type(self).files = type(self).files
        self.test0 = self.__class__.__name__
        return

    ## Null setup.
    def tearDown(self):
        self.logger.info('tearDown')
        return

    ## Build filters
    def test_00(self):
        self.filters = list(map( lambda x: Filter(x[0], x[1]), self.sources.values()))
        return

    ## Post-process.
    def test_03(self):
        self.test_00()
        self.assertIsNotNone(self.filters)

        self.series = list(map(lambda x: postprocess0(x), self.filters))
        self.assertIsNotNone(self.series)

        self.assertEqual(len(self.series), len(self.sources))

    ## Use Selector
    def test_05(self):
        self.test_03()
        self.assertIsNotNone(self.series)
        s0s = list(filter(lambda x: x.name != "weather-metoffice", self.series))
        df = pd.DataFrame(s0s).transpose()
        s0 = Selector(df)
        self.logger.info(s0)

    ## Use Sales0
    def test_07(self):
        self.test_03()
        self.assertIsNotNone(self.series)
        s0s = list(filter(lambda x: x.name != "weather-metoffice", self.series))
        s1 = list(filter(lambda x: x.name == "weather-metoffice", self.series))
        df = pd.DataFrame(s0s).transpose()
        s0 = Sales0(df, metoffice=s1)
        s0.constrain()
        s0.fx()
        self.logger.info(s0)

# The sys.argv line will complain to you if you run it with ipython
# emacs. The ipython arguments are passed to unittest.main.

if __name__ == '__main__':
    if len(sys.argv) and "ipython" not in sys.argv[0]:
        # If this is not ipython, run as usual
        unittest.main(sys.argv)
    else:
        # If not remove the command-line arguments.
        sys.argv = [sys.argv[0]]
        unittest.main(module='Test', verbosity=3, failfast=True, exit=False)


