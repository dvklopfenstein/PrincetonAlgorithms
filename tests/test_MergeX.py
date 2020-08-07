#!/usr/bin/env python

from AlgsSedgewickWayne.MergeX import *
from AlgsSedgewickWayne.testcode.ArrayHistory import *
import unittest

import random


def test_1():
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  desc = 'IMPROVED MERGESORT'
  a = [int(s) for s in "13 16 40 60 19 70 71 47 12 67".split()]
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  print(desc, "RESULT", a)
  # TBD: Implement array history visualization
  # prt_array_history(array_history)
  # show_array_history(desc, array_history)
  print('')

if __name__ == '__main__':
  test_1()
