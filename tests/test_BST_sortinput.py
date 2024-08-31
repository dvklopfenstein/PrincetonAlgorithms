#!/usr/bin/env python
"""Test sorting of a list such that the sorted list will build a balanced BST."""

from sys import stdout
import random
from random import shuffle
import numpy as np

from AlgsSedgewickWayne.BST import BST
from AlgsSedgewickWayne.BST_utils import sort_balbst

__copyright__ = "Copyright (C) 2019, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

def _get_kv(keys):
    """Given a list of keys, assign a value. Return a list of key-vals."""
    return [(k, i) for i, k in enumerate(keys)]

def test_0(log=stdout):
    """Test using various random shuffles of a list of letters."""
    lst = ['K', 'B', 'C', 'I', 'E', 'G', 'F', 'H', 'J', 'D', 'A']
    L = len(lst)
    for i in range(10):
        shuffle(lst)
        bst = BST(sort_balbst(_get_kv(lst)))
        bst.wr_png("BST_a{I}.png".format(I=i))
        log.write("{LST}\n".format(LST=lst))
        assert bst.height() == int(np.floor(np.log2(L))), "HEIGHT VIOLATION"

def test_1(log=stdout):
    """Test using various random lists of integers."""
    for i in range(10): # Run 10 tests
        L = random.randint(1, 100)
        lst = list(range(L))
        shuffle(lst)
        bst = BST(sort_balbst(_get_kv(lst)))
        bst.wr_png("BST_i{I}.png".format(I=i))
        log.write("{LST}\n".format(LST=lst))
        assert bst.height() == int(np.floor(np.log2(L))), "HEIGHT VIOLATION"

def run_all(log=stdout):
    test_0(log)
    test_1(log)


if __name__ == '__main__':
    run_all()

# Copyright (C) 2019, DV Klopfenstein. All rights reserved.
