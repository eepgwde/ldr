# -*- coding: utf-8 -*-
## @author weaves
##
## Provides utility methods for selecting across time ranges.

import logging

import glob
import os

import datetime

logger = logging.getLogger('Test')

class Selector(object):
  """
  Provides a container for a merged dataframe of the variables of interest.

  This should be sub-classed provide methods specific to a set of features.
  """

  _df = None                    # the quality0 date.

  """Takes a merged dataframe. Extra sources can be attached with kwargs."""
  def __init__(self, df, **kwargs):
    super().__init__()
    self._df = df
    for key, value in kwargs.items():
      setattr(self, key, value)

  def __str__(self):
    """text representation"""
    return "'{0:s}: {1:s}'".format(self.__class__.__name__,
                                   ", ".join(self._df.columns.values) )

