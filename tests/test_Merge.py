#!/usr/bin/env python
"""Test Merge."""

import sys

from AlgsSedgewickWayne.Merge import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory

import random


def test_1(prt=sys.stdout):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  desc = 'MERGESORT'
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  array_history = ArrayHistory()
  Sort(a, array_history)
  prt.write("{DESC} RESULT: {A}\n".format(DESC=desc, A=a))
  # TBD: Implement array history visualization
  # prt_array_history(array_history)
  # show_array_history(desc, array_history)

if __name__ == '__main__':
  test_1()


