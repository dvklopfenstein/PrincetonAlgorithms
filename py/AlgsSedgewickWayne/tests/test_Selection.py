#!/usr/bin/env python

from   AlgsSedgewickWayne.Selection    import Sort
from   AlgsSedgewickWayne.ArrayHistory import chk, show_array_history, prt_array_history

def test_wk2_ex_Selections_489125():
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  desc = 'SELECTION SORT'
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  array_history = []
  Sort(a, array_history)
  prt_array_history(array_history)
  show_array_history(desc, array_history)
  print

def test_wk2_q3():
  # QUESTION: Any pair of items is compared no more than once during selection sort.
  # ANSWER(FALSE): Consider the array { 2, 1, 0 }. Then, 2 and 1 are compared twice.
  desc = 'SELECTION SORT'
  a = [2, 1, 0]
  array_history = []
  Sort(a, array_history)
  show_array_history(desc, array_history)
  print

def test_wk2_q2a():
  desc = 'SELECTION SORT WORDS'
  exp = "BECK BUSH DEVO EVE6 HOLE JAYZ KORN MIMS VAIN RATT TOTO PINK SADE NOFX SOAD WHAM"
  a = "HOLE BUSH MIMS BECK WHAM SOAD NOFX TOTO VAIN RATT DEVO PINK SADE KORN JAYZ EVE6".split()
  array_history = []
  Sort(a, array_history)
  show_array_history(desc, array_history)
  for idx, A in enumerate(array_history):
    if chk( A[0], exp ):
      print "MATCH", idx
  print

def run_all():
  """Run all tests."""
  test_wk2_q2a()
  test_wk2_q3()
  test_wk2_ex_Selections_489125()

if __name__ == '__main__':
  run_all()


