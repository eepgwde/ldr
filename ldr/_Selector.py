# -*- coding: utf-8 -*-
## @author weaves
##
## Container class for Track.

import logging

import glob
import os

import datetime

from cached_property import cached_property

from collections import UserList
from operator import attrgetter

from weaves import singledispatch1, Singleton

from ldr._Filterer import Filter

logger = logging.getLogger('Test')

class Selector(UserList):

  _dt = None                    # the quality0 date.

  """List of audio"""
  def __init__(self, **kwargs):
    super().__init__()

  def __repr__(self):
    """utf-8 formatted text representation"""
    return "string"

