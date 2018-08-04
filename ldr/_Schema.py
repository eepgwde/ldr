## @file _Schema.py
# @author caz
# @brief A description for a type of file.
#
# Holds a schema for a data source.

import logging
from cached_property import cached_property
from unidecode import unidecode

from math import floor
import datetime
from weaves import Singleton

logger = logging.getLogger('Test')

class Schema(object):
  """
  Description of a data source.

  This base class takes a dictionary that it assigns the elements as members.
  """

  _months = ( "Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" )


  def __init__(self, **kwargs):
    for key, value in kwargs.items():
      logger.info("{0:s} = {1:s}".format(key, value))
      setattr(self, key, value)
    return

  def __str__(self):
    """text representation"""
    return "{0:s}".format(self.__class__.__name__)

