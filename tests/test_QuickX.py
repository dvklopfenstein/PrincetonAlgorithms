#!/usr/bin/env python3
"""Test sort using Bentley-McIlroy 3-way partitioning scheme choosing w/Tukey's #"""
# pylint: disable=invalid-name

from AlgsSedgewickWayne.QuickX import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory


def test_quickx():
    """Test sort using Bentley-McIlroy 3-way partitioning scheme choosing w/Tukey's #"""
    # (seed = 183182)
    # Give the array that results after the first 4 exchanges when
    # selection sorting the following array:
    desc = 'QUICKX'
    arr = [int(i) for i in "13 16 40 60 19 70 71 47 12 67".split()]
    arrhist = ArrayHistory()
    Sort(arr, array_history=arrhist)
    print(desc, "RESULT", arr)
    # TBD: Implement array history visualization
    # prt_array_history(array_history)
    # show_array_history(desc, array_history)
    print('')

if __name__ == '__main__':
    test_quickx()
