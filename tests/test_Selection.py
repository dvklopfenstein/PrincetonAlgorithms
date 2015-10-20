#!/usr/bin/env python

import sys

from AlgsSedgewickWayne.Selection import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import chk 
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

def test_wk2_lec(prt=sys.stdout):
  """Example from week 2 lecture, "Selection Sort (6:59)" """
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  a = map(int, "7 10 5 3 8 4 2 9 6".split() )
  run(a, 'SELECTION SORT', prt=prt)

def test_wk2_ex_Selections_489125(prt=sys.stdout):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  run(a, 'SELECTION SORT', prt=prt)

def test_wk2_q3a(prt=sys.stdout):
  # QUESTION: Any pair of items is compared no more than once during selection sort.
  # ANSWER(FALSE): Consider the array { 2, 1, 0 }. Then, 2 and 1 are compared twice.
  run([2, 1, 0], 'SELECTION SORT', prt=prt)

def test_wk2_q3b(prt=sys.stdout):
  # QUESTION: An exchange in selection sort can decrease the number of inversions 
  #   by two (or more).
  # ANSWER(TRUE): Consider the array { 3, 2, 1 }, which has 3 inversions. The first exchange results in the array { 1, 2, 3 }, which has zero inversions.
  run([3, 2, 1], 'SELECTION SORT', prt=prt)

def test_wk2_q2a(prt=sys.stdout):
  desc = 'SELECTION SORT WORDS'
  prt.write("\n{TEST}\n".format(TEST=desc))
  exp = "BECK BUSH DEVO EVE6 HOLE JAYZ KORN MIMS VAIN RATT TOTO PINK SADE NOFX SOAD WHAM"
  a = "HOLE BUSH MIMS BECK WHAM SOAD NOFX TOTO VAIN RATT DEVO PINK SADE KORN JAYZ EVE6".split()
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  ah.show(desc)
  for idx, A in enumerate(ah):
    if chk( A[0], exp ):
      prt.write("MATCH {I}\n".format(I=idx))

def run(a, desc=None, prt=sys.stdout):
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  if desc is None:
    desc = "INSERTION SORT" 
  prt.write("{DESC} RESULT {A}\n".format(DESC=desc, A=' '.join(str(e) for e in a)))
  ah.prt()
  ah.show(desc)

def run_all():
  """Run all tests."""
  test_wk2_lec()
  test_wk2_ex_Selections_489125()
  test_wk2_q3a()
  test_wk2_q2a()

def cli():
  N = len(sys.argv)
  if N == 1:
    run_all()
  elif N == 2:
    run(cli_get_array())

if __name__ == '__main__':
  cli()


