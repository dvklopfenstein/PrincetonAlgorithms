#!/usr/bin/env python

import sys

from AlgsSedgewickWayne.MergeBU import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory

def run(a, desc, prt=sys.stdout):
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  ah.prt_intlvd() # After each merge, print the state of both a and aux
  #ah.show(desc)
  prt.write("{DESC} RESULT: {A}\n".format(DESC=desc, A=a))

def test_193860(prt=sys.stdout):
  """ seed = 193860 """
  # Give the array that results immediately after the 7th call (and return)
  # from merge() when bottom-up mergesorting the following array:
  a = map(int, "25 94 79 41 19 84 66 67 90 37".split())
  run(a, 'BOTTOM-UP MERGESORT')


def test_1(prt=sys.stdout):
  """(seed = 183182)."""
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  run(a, 'BOTTOM-UP MERGESORT')

def run_all(prt=sys.stdout):
  test_1(prt)
  test_193860(prt)

def run_seq(prt=sys.stdout):
  a = map(int, sys.argv[1].split() )
  run(a, "MERGESORT")


if __name__ == '__main__':
  if len(sys.argv) == 1:
    run_all()
  else:
    run_seq()

