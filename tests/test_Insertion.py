#!/usr/bin/env python
"""Test Insertion sort"""

import sys

from AlgsSedgewickWayne.Insertion import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

def _run(arr, desc=None, prt=sys.stdout):
    exp = sorted(arr)
    ahistobj = ArrayHistory()
    Sort(arr, array_history=ahistobj)
    if desc is None:
        desc = "INSERTION SORT"
    prt.write(f"{desc} RESULT {' '.join(str(e) for e in arr)}\n")
    ahistobj.prt()
    ahistobj.show(desc)
    assert arr == exp

def test_wk2_lec():
    """Test week 2 lecture insertion sort"""
    arr = [int(e) for e in "7 10 5 3 8 4 2 9 6".split()]
    _run(arr, "INSERTION SORT: SEED 183182")

def test_wk2_lec_best():
    """Best-case runtime is when array is already sorted."""
    arr = "A E E L M O P R S T X".split()
    _run(arr, "INSERTION BEST SORT:")

def test_wk2_lec_worst():
    """Best-case runtime is when array is already sorted."""
    arr = "X T S R P O M L E E A".split()
    _run(arr, "INSERTION WORST SORT:")

def test_wk2_lec_partial():
    """Array is partially sorted ad contains inversions."""
    # 6 inversions T-R  T-P  T-S  R-P  X-P  X-S
    arr = "A E E L M O T R X P S".split()
    _run(arr, "INSERTION PARTIAL SORT:")

def test_1():
    """Test inserttion sort"""
    arr = [int(e) for e in  "13 16 40 60 19 70 71 47 12 67".split()]
    _run(arr, "INSERTION SORT: SEED 183182")

def test_2():
    """Test inserttion sort"""
    # pylint: disable=line-too-long
    arr = "gold bone pink dust iris aqua rust kobi wine jade pine corn drab puce plum bark".split()
    _run(arr)

def test_3():
    """Test inserttion sort"""
    arr = [int(e) for e in  "37 41 45 60 73 52 79 19 94 32".split()]
    _run(arr, "INSERTION SORT: seed 756506")

def test_4():
    """Test inserttion sort"""
    arr = [int(e) for e in  "14 23 77 94 96 48 39 18 41 13".split()]
    _run(arr, "INSERTION SORT: seed 72847")

def test_5():
    """Test inserttion sort"""
    arr = [int(e) for e in  "34 38 69 83 93 68 37 28 85 99".split()]
    _run(arr, "INSERTION SORT: seed 329024")

def test_half01a():
    """Test inserttion sort"""
    arr = [int(e) for e in  "0 1 0 1 0 1 0 1 0 1 0 1 0 1".split()]
    _run(arr, "INSERTION SORT: 01010101...")

def test_half01b():
    """Test inserttion sort"""
    arr = [int(e) for e in  "1 1 1 1 1 1 1 0 0 0 0 0 0 0".split()]
    _run(arr, "INSERTION SORT: 11110000")

def test_half01c():
    """Test inserttion sort"""
    arr = [int(e) for e in  "0 0 0 0 0 0 0 1 1 1 1 1 1 1".split()]
    _run(arr, "INSERTION SORT: 00001111")

def run_all():
    """Run all tests."""
    test_wk2_lec()
    test_wk2_lec_best()
    test_wk2_lec_worst()
    test_wk2_lec_partial()
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_half01a()
    test_half01b()
    test_half01c()

def _cli():
    len_array = len(sys.argv)
    if len_array == 1:
        run_all()
    elif len_array == 2:
        _run(cli_get_array())

if __name__ == '__main__':
    _cli()
