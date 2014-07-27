#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.Selection import *
from AlgsSedgewickWayne.ArrayHistory import *

class Selection_Tests(unittest.TestCase):

  def test_wk2_ex_Selections_489125(self):
    # (seed = 183182)
    # Give the array that results after the first 4 exchanges when
    # selection sorting the following array:
    a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
    array_history = []
    Sort(a, array_history)
    print "SELECTION SORT RESULT", a
    prt_array_history(array_history)
    show_array_history('SELECTION SORT', array_history)
    print

if __name__ == '__main__':
  unittest.main()


