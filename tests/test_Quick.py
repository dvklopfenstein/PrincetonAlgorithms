#!/usr/bin/env python3
"""Test Quick sort"""
# pylint: disable=invalid-name

from AlgsSedgewickWayne.Quick import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

def test_quicksort():
    """Test Quick sort"""
    _run(cli_get_array("13 16 40 60 19 70 71 47 12 67"))

def _run(arr):
    """Test Quick sort"""
    desc = 'QUICKSORT'
    ahist = ArrayHistory()
    Sort(arr, array_history=ahist)
    ahist.prt()
    ahist.show(desc)
    print(desc, "RESULT:", arr)


if __name__ == '__main__':
    test_quicksort()
