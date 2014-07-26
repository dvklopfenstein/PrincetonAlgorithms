#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.Selection import *

class Selection_Tests(unittest.TestCase):

  def chk(self, a, txt):
    b = txt.split()
    return len(a)==len(b) and len(a)==sum([1 for i,j in zip(a,b) if i==j])

  def test_wk2_ex_Selections_489125(self):
    # (seed = 183182)
    # Give the array that results after the first 4 exchanges when
    # selection sorting the following array:
    a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
    Sort(a, True)
    print "RESULT", a
    print

if __name__ == '__main__':
  unittest.main()


