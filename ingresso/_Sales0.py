# -*- coding: utf-8 -*-
## @author weaves
##
## Provides utility methods for selecting across time ranges.

import logging

import glob
import os

from ldr import Selector

import datetime

logger = logging.getLogger('Test')

class Sales0(Selector):
  """
  Provides a container for a merged dataframe of the variables of interest.

  This should be sub-classed provide methods specific to a set of features.
  """

  _df = None                    # the quality0 date.

  """Takes a merged dataframe"""
  def __init__(self, df):
    super().__init__(df)

  """Weather: """
  def weather(self, period0="M"):
    self.weather = self._df['weather'].resample(period0).mean()


