#!/usr/bin/env python3
"""Small test utilities"""

__copyright__ = "Copyright (C) 2020-present, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

from os.path import join
from os.path import dirname
from os.path import abspath
import sys
import timeit
from datetime import timedelta


DIR_TEST = dirname(abspath(__file__))
REPO = join(DIR_TEST, "..")

def prt_hms(tic, msg, prt=sys.stdout):
    """Print elapsed time and return current time"""
    toc = timeit.default_timer()
    prt.write('{HMS} {MSG}\n'.format(HMS=str(timedelta(seconds=toc-tic)), MSG=msg))
    return toc

def repo_fn(fin):
    """Get a full filename, given a local file name from repo dir root"""
    return join(REPO, fin)


# Copyright (C) 2020-present, DV Klopfenstein. All rights reserved.
