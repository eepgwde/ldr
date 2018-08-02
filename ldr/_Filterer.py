## @file _Filterer.py
# @author weaves
# @brief A filter
#
# Holds a filter.

import logging
from cached_property import cached_property
from unidecode import unidecode

from math import floor
import datetime
from weaves import Singleton

logger = logging.getLogger('Test')

class Filter(object):
  """single audio file"""

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
