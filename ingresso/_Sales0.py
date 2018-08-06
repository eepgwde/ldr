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
  """Provides a container for a merged dataframe of the variables of interest.

  These methods assume all the data is daily and performs some corrections.

  Eventually, we want to provide monthly metrics.

  Sales are every day of the week, but fx is only work-days, but the two FX
  sources have bald spots.

  These methods need to correct the data in the following ways.

  """

  _df = None                    # the source frame
  _cdf = None                   # the constrained frame

  def __init__(self, df, **kwargs):
    """
    Takes a merged dataframe and optional items.

    See fx(), you can add an fx_op="merge" to coalesce the two FX series.
    By default, it is set to "single" and uses fx-fxcm.
    """
    super().__init__(df, **kwargs)

  def constrain(self, sname="sales"):
    """Restrict the dataframe to the range of one series and force to daily quotes."""
    x0 = self._df[sname]
    x1 = x0[x0.notna()].index
    self._cdf = self._df[(self._df.index >= x1[0]) & (self._df.index <= x1[-1]) ]
    self._cdf = self._cdf.resample("D").mean()
    return

  def fx(self):
    """
    fx sources are combined.

    Issue with overwriting columns means that assign has to be used - ignoring
    indices.
    """

    if getattr(self, 'fx_op', 'single') == 'merge':
      fx = self._cdf['fx']
      fx1 = self._cdf['fx-fxcm']
      fx0 = self.coalesce(fx, fx1)
      self._cdf = self._cdf.assign(fx0=fx0.values)
    else:
      self._cdf = self._cdf.assign(fx0=self._cdf['fx-fxcm'])
    return 

  def resample(self, sname, period0="M"):
    """
    Resample a series by name over a period.

    This changes the index to a PeriodIndex and not a DatetimeIndex.
    """
    w0 = self._cdf[sname].resample(period0).mean()
    w0.index = w0.index.to_period(period0)
    return w0

  def __str__(self):
    """text representation"""
    s0 = ""

    if type(self._cdf) == type(None):
      pass
    elif self._cdf.empty:
      pass
    else:
      s0 = ", ".join(self._cdf.columns.values)

    return "'{0:s}: ({1:s})'".format(self.__class__.__name__, s0)



