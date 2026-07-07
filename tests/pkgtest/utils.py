"""Utilities for running tests"""

import os.path as op
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array


REPO = op.normpath(op.abspath(op.join(op.dirname(__file__), "../..")))

def get_filename(filename):
    """Get absolute filename with 'home' as the repo base"""
    return op.join(REPO, filename)

def get_array(filename):
    """Get an array given a filename that contains a graph"""
    fnam = get_filename(filename)
    assert op.exists(fnam)
    return cli_get_array(fnam)
