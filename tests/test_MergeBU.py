#!/usr/bin/env python

import sys

from AlgsSedgewickWayne.MergeBU import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory

def run(a, desc, prt=sys.stdout):
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  prt.write("{DESC} RESULT: {A}\n".format(DESC=desc, A=a))
  ah.prt_intlvd() # After each merge, print the state of both a and aux
  #ah.show(desc)

def test_1(prt=sys.stdout):
  """(seed = 183182)."""
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  run(a, 'BOTTOM-UP MERGESORT')

def run_all(prt=sys.stdout):
  test_1(prt)

if __name__ == '__main__':
  run_all()


