#!/usr/bin/env python

from AlgsSedgewickWayne.Quick import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

import random
import fileinput
import sys
import os
import re

def test_1(self):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  desc = 'QUICKSORT'
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  print desc, "RESULT", a
  # TBD: Implement array history visualization
  # prt_array_history(array_history)
  # show_array_history(desc, array_history)
  print


def test_stdin():
  """echo "a b c d e f" | test_Quick.py"""
  a = cli_get_array()
  print a[:3]
  print len(a)

if __name__ == '__main__':
  test_stdin()


