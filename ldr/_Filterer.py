## @file _Filterer.py
# @author caz
# @brief A filter
#
# Holds a filter for a data source. Takes a descriptive schema object and
# produces Pandas objects.

import logging
from cached_property import cached_property
from unidecode import unidecode

from math import floor
import datetime
from weaves import Singleton

logger = logging.getLogger('Test')

class Filter(object):
  """Single data source"""

  _window = None
  
  def __init__(self, fname):
    logger.info("Track: ctr: " + fname)
    return

  @cached_property
  def window(self):
    """get track duration in seconds"""
    _window = 0
    return _window

  def __str__(self):
    """text representation"""
    return "'{0:s}'>".format("this")
        
  def __repr__(self):
    """utf-8 formatted text representation"""
    return self.__str__()
