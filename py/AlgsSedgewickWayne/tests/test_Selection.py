#!/usr/bin/env python

import unittest
from   AlgsSedgewickWayne.Selection    import *
from   AlgsSedgewickWayne.ArrayHistory import *
import AlgsSedgewickWayne.ArrayHistory as H

class Selection_Tests(unittest.TestCase):

  def test_wk2_ex_Selections_489125(self):
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

  def test_wk2_q3(self):
    # QUESTION: Any pair of items is compared no more than once during selection sort.
    # ANSWER(FALSE): Consider the array { 2, 1, 0 }. Then, 2 and 1 are compared twice.
    desc = 'SELECTION SORT'
    a = [2, 1, 0]
    array_history = []
    Sort(a, array_history)
    show_array_history(desc, array_history)
    print

  def test_wk2_q2a(self):
    desc = 'SELECTION SORT WORDS'
    exp = "BECK BUSH DEVO EVE6 HOLE JAYZ KORN MIMS VAIN RATT TOTO PINK SADE NOFX SOAD WHAM"
    a = "HOLE BUSH MIMS BECK WHAM SOAD NOFX TOTO VAIN RATT DEVO PINK SADE KORN JAYZ EVE6".split()
    array_history = []
    Sort(a, array_history)
    show_array_history(desc, array_history)
    for idx, A in enumerate(array_history):
      if H.chk( A[0], exp ):
        print "MATCH", idx
    print

if __name__ == '__main__':
  unittest.main()


