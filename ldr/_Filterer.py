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
    logger.info("file: " + fname)
    self._schema = schema
    self._fname = fname
    self._data = pd.read_csv(fname)
    return

  def __str__(self):
    """text representation"""
    return "'{0:s}: {1:s}'".format(self.__class__.__name__, self._schema.desc)

  def series(self, desc, **kwargs):
    """Process columns from the data source as Panda Series."""

    r0 = None
    idx0 = "idx"

    if desc == "datetime":
      idx0 = "dt0"

      if self._schema.desc == "fx":
        ## Convert to month of year. It may have already been converted.
        if self._data.Month.dtype.kind == 'O':
          m0 = self._data.Month
          self._data.Month = pd.Series(list(
            map( lambda x: 1 + self._schema._months.index(x), m0)))
        r0 = pd.to_datetime(self._data[['Year', 'Month', 'Day']])
      elif self._schema.desc == "fx-fxcm":
        r0 = pd.to_datetime(self._data['date'])
      elif self._schema.desc == "sales":
        r0 = pd.to_datetime(self._data.Date)
      elif self._schema.desc == "weather":
        r0 = pd.to_datetime(self._data.DATE)
      elif self._schema.desc == "weather-metoffice":
        x0 = self._data
        x0['day'] = 1
        x1 = x0.rename(index=str, columns={"yyyy":"year", "mm":"month"})
        r0 = pd.to_datetime(x1[['year', 'month', 'day']])
        r0 = r0.dt.to_period('M')

      r0.rename(idx0, inplace=True)

      if "index" in kwargs:
        if kwargs["index"]:
          self._data = self._data.set_index(r0)
      return r0

    if desc == "value":
      name0 = self._schema.desc
      if "name" in kwargs:
        name0 = kwargs['name']

      name1 = None
      if "sname" in kwargs:
        name1 = kwargs[sname]

      if self._schema.desc == "fx":
        if name1 == None:
          name1 = "Price"
      if self._schema.desc == "fx-fxcm":
        if name1 == None:
          name1 = "bidclose"
      elif self._schema.desc == "sales":
        if name1 == None:
          name1 = "Tickets Sold"
      elif self._schema.desc == "weather":
        if name1 == None:
          name1 = "TAVG"
      elif self._schema.desc == "weather-metoffice":
        if name1 == None:
          name1 = "tmin"

      r0 = self._data[name1]
      r0.rename(name0, inplace=True)
    return r0
        
  def __repr__(self):
    """utf-8 formatted text representation"""
    return self.__str__()

