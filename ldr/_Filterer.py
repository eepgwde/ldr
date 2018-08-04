## @file _Filterer.py
# @author caz
# @brief A filter
#
# Holds a filter for a data source. Takes a descriptive schema object and
# produces Pandas objects.

import logging

import numpy as np
import pandas as pd

from math import floor
import datetime
from weaves import Singleton

logger = logging.getLogger('Test')

class Filter(object):
  """
  Pass a URL and a schema object.

  This is only a prototype base class. It applies filtering operations to change the
  underlying data based on the Schema.
  """

  _fname = None
  _schema = None
  _data = None
  
  def __init__(self, fname, schema):
    logger.info("Track: ctr: " + fname)
    self._schema = schema
    self._fname = fname
    self._data = pd.read_csv(fname)
    return

  def __str__(self):
    """text representation"""
    return "'{0:s}'>".format("this")

  def series(self, desc):
    """Return a colum from the data source as a Panda Series."""
    r0 = None
    if desc == "datetime":
      if self._schema.desc == "fx":
        ## Convert to month of year. It may have already been converted.
        if self._data.Month.dtype.kind == 'O':
          m0 = self._data.Month
          self._data.Month = pd.Series(list(
            map( lambda x: 1 + self._schema._months.index(x), m0)))
        
        r0 = pd.to_datetime(self._data[['Year', 'Month', 'Day']])

      if self._schema.desc == "sales":
        r0 = pd.to_datetime(self._data.Date)

    return r0
        
  def __repr__(self):
    """utf-8 formatted text representation"""
    return self.__str__()
