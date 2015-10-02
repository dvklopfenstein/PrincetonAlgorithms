#!/usr/bin/env python
"""Test Merge."""

import sys

from AlgsSedgewickWayne.Merge import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory

import random


def run(a, desc, prt=sys.stdout):
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  ah.prt_intlvd() # After each merge, print the state of both a and aux
  #ah.show(desc)
  prt.write("{DESC} RESULT: {A}\n".format(DESC=desc, A=a))

def test_14238(prt=sys.stdout):
  a = map(int, "80 97 50 29 23 83 66 67 43 47 41 42".split())
  run(a, "14238")

def test_3(prt=sys.stdout):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  run(a, "MERGESORT 183182")

def test_2(prt=sys.stdout):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  a = "M E R G E S O R T E X A M P L E".split()
  run(a, "MERGE SORT EXAMPLE")

def test_1(prt=sys.stdout):
  """Mergesort (23:54) Example at 02:19."""
  a = "E E G M R A C R T".split()
  run(a, "MERGE 1st Lec Ex")

def run_all(prt=sys.stdout):
  test_1(prt)
  test_2(prt)
  test_14238(prt)

def run_seq(prt=sys.stdout):
  a = map(int, sys.argv[1].split() )
  run(a, "MERGESORT")


if __name__ == '__main__':
  if len(sys.argv) == 1:
    run_all()
  else:
    run_seq()


