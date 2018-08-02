#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Create an audiobook with chapters from files given as input.

Usage:
  audiobooks (-h | --help)
  audiobooks [-o FILE] [options] (--files FILE | <input>...)

Arguments:
  input                                 A directory of files or a file to update or 
                                        a glob pattern

Options:
  -h, --help                            Display help message.
  -l, --log                             Enable logging.
  -d, --dry-run                         Output options and files
  -q, --quiet                           Don't output status messages.
  --tmp DIR                             Pass this directory to use for 
                                        temporary files (otherwise use TMPDIR and then TMP)
  -o, FILE, --output FILE               Output .m4b file. Default: output.m4b
  --sort                                Sort tracks by disc and track number 
  -v, --verbose                         Output status messages.
                                        With -l,--log will display warnings.
                                        With -d,--dry-run will show parameters.
  -f FILE, --files FILE                 File containing files.
  --cover FILE                          Add a file of cover-art. Default: cover.jpg
  -c COMMAND, --command COMMAND         What to do: remove,write,cover,chapters

Patterns can be any valid Python regex patterns.

Commands:

 remove will remove any pre-existing file with the output filename
 write combines the .m4a files into one the output file using MP4Box
 cover will install the image file into the output M4B file
 chapters will install a chapter menu into the file
 quicktime will convert chapters to the QuickTime format

 chapters0 will print out the chapters entries to the console

 metadata will write details from the first track to the book as a whole.

Note:

 If you don't have MP4Box installed, you can get a chapter list with the command
 of chapters0.

Examples:

 audiobooks -o iron.m4b -f iron.lst --cover Iron.jpg -c "remove,write,cover,chapters,quicktime"

This will take files, in order, named in the file iron.lst and write them to iron.m4b. 
It will then add the cover image Iron.jpg. Generate some chapters from the files and 
their durations. Finally, it will convert those chapters from Nero format to Quicktime.

You should then be able to play this file in an iPad and see the chapters.

Notes:

The chapter titles are taken from the M4A file input's track title. 
These have to be uniquely named to give unique titles in an iPad. So use 
an MP4 tagging tool to set the title to be unique.

"""

from __future__ import print_function;

from ldr._Filterer import Filter

from unidecode import unidecode
from docopt import docopt

import csv
import os
import sys
import glob
import subprocess

from math import floor
from operator import attrgetter
from tempfile import mkstemp

import logging

QUIET = 25
logging.addLevelName(25, "QUIET")
logging.basicConfig(filename='run.log', level=QUIET)
global logger
logger = logging.getLogger('Test')

def main():
    global cli
    global logger

    argv = sys.argv
    
    cli = dict((key.lstrip("-<").rstrip(">"), value) for key, value in docopt(__doc__).items())

    enable_logging = cli['log']
    if cli['quiet']:
        logger.setLevel(QUIET)
    else:
        logger.setLevel(logging.INFO)

    if enable_logging:
        logger.setLevel(logging.DEBUG)
        if cli['verbose']:
            sh = logging.StreamHandler()
            logger.addHandler(sh)
        logger.debug('cli: ' + type(cli).__name__)

    # book = Book(**cli)
    

