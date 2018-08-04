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

  _df = None                    # the quality0 date.

  """List of audio"""
  def __init__(self, df):
    super().__init__()
    self._df = df

  def __str__(self):
    """text representation"""
    return "'{0:s}: {1:s}'".format(self.__class__.__name__,
                                   ", ".join(self._df.columns.values) )

