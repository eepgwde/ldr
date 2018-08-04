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

from datetime import datetime, timezone, timedelta, date

from collections import Counter

import unittest

from ldr import Filter, Selector, Schema

logfile = os.environ['X_LOGFILE'] if os.environ.get('X_LOGFILE') is not None else "test.log"
logging.basicConfig(filename=logfile, level=logging.DEBUG)
logger = logging.getLogger('Test')
sh = logging.StreamHandler()
logger.addHandler(sh)

media0 = os.path.join(os.path.dirname(__file__), "media")
trs0 = os.path.join(os.path.dirname(__file__), "p1.lst")

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

    ## Loaded?
    ## Is utf-8 available as a filesystemencoding()
    def test_000(self):
        self.assertIsNotNone(self.test0)
        return

    ## There was an issue with unicode

    def test_01(self):
        self.assertIsNotNone(self.test0)
        self.logger.info('test0: ' + str(self.test0))
        
        if not type(self).files:
            type(self).files = type(self).files0

        self.file0, *type(self).files = type(self).files
        test1 = self.file0.__class__.__name__
        self.logger.info('test1: ' + str(test1))

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
        unittest.main(module='Test', verbosity=3, failfast=True, exit=False)


