# -*- coding: utf-8 -*-
## @author caz
##
## Provides domain specific data selection.

import logging

import glob
import os

from ldr import Selector

import datetime

logger = logging.getLogger('Test')

class Sales0(Selector):
  """
  Provides a container for a merged dataframe of the variables of interest.

  These methods assume all the data is daily and performs some corrections.
  """

  _df = None                    # the source frame
  _cdf = None                   # the constrained frame

  """Takes a merged dataframe"""
  def __init__(self, df, **kwargs):
    super().__init__(df, **kwargs)

  """Restrict the dataframe to the range of one series."""
  def constrain(self, sname="sales"):
    x0 = self._df[sname]
    x1 = x0[x0.notna()].index
    self._cdf = self._df[(self._df.index >= x1[0]) & (self._df.index <= x1[-1]) ]
    return

  """Weather """
  def weather(self, period0="M"):
    self.weather = self._df['weather'].resample(period0).mean()


