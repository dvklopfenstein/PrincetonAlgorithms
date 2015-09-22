#!/usr/bin/env python
"""Test Merge."""

import sys

from AlgsSedgewickWayne.Merge import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory

import random


def run(a, desc, prt=sys.stdout):
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  prt.write("{DESC} RESULT: {A}\n".format(DESC=desc, A=a))
  # TBD: Implement array history visualization
  # prt_array_history(array_history)
  # show_array_history(desc, array_history)

def test_1(prt=sys.stdout):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  run(a, "MERGESORT 183182")

def test_2(prt=sys.stdout):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  a = "S O R T E X A M P L E".split()
  run(a, "MERGESORT SORTEXAMPLE")

def run_all():
  test_1()
  test_2()


if __name__ == '__main__':
  run_all()


