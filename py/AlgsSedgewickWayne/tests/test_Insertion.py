#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.Insertion import *
from AlgsSedgewickWayne.ArrayHistory import *

class Insertion_Tests(unittest.TestCase):

  def test_1(self):
    # (seed = 183182) in Selection sort question
    desc = 'INSERTION SORT'
    a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
    array_history = []
    Sort(a, array_history)
    print desc, "RESULT", a
    prt_array_history(array_history)
    show_array_history(desc, array_history)
    print

  def test_2(self):
    desc = 'INSERTION SORT'
    a = "gold bone pink dust iris aqua rust kobi wine jade pine corn drab puce plum bark".split()
    array_history = []
    Sort(a, array_history)
    print desc, "RESULT", a
    prt_array_history(array_history)
    show_array_history(desc, array_history)
    print

if __name__ == '__main__':
  unittest.main()


