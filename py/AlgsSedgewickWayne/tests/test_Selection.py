#!/usr/bin/env python

import sys

from   AlgsSedgewickWayne.Selection    import Sort
from   AlgsSedgewickWayne.ArrayHistory import chk 
from   AlgsSedgewickWayne.ArrayHistory import ArrayHistory

def test_wk2_ex_Selections_489125(prt=sys.stdout):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  desc = 'SELECTION SORT'
  prt.write("\n{TEST}\n".format(TEST=desc))
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  array_history = ArrayHistory()
  Sort(a, array_history)
  array_history.prt()
  array_history.show(desc)

def test_wk2_q3(prt=sys.stdout):
  # QUESTION: Any pair of items is compared no more than once during selection sort.
  # ANSWER(FALSE): Consider the array { 2, 1, 0 }. Then, 2 and 1 are compared twice.
  desc = 'SELECTION SORT'
  prt.write("\n{TEST}\n".format(TEST=desc))
  a = [2, 1, 0]
  array_history = ArrayHistory()
  Sort(a, array_history)
  array_history.show(desc)

def test_wk2_q2a(prt=sys.stdout):
  desc = 'SELECTION SORT WORDS'
  prt.write("\n{TEST}\n".format(TEST=desc))
  exp = "BECK BUSH DEVO EVE6 HOLE JAYZ KORN MIMS VAIN RATT TOTO PINK SADE NOFX SOAD WHAM"
  a = "HOLE BUSH MIMS BECK WHAM SOAD NOFX TOTO VAIN RATT DEVO PINK SADE KORN JAYZ EVE6".split()
  array_history = ArrayHistory()
  Sort(a, array_history)
  array_history.show(desc)
  for idx, A in enumerate(array_history):
    if chk( A[0], exp ):
      prt.write("MATCH {I}\n".format(I=idx))

def run_all():
  """Run all tests."""
  test_wk2_ex_Selections_489125()
  test_wk2_q3()
  test_wk2_q2a()

if __name__ == '__main__':
  run_all()


