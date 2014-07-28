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

  def test_3(self):
    # (seed = 756506) ) in Selection sort question after 6 exchanges
    desc = 'INSERTION SORT'
    a = map(int, "37 41 45 60 73 52 79 19 94 32".split() )
    array_history = []
    Sort(a, array_history)
    print desc, "RESULT", a
    prt_array_history(array_history)
    show_array_history(desc, array_history)
    print

  def test_4(self):
    # (seed = 72847) ) in Selection sort question after 6 exchanges
    desc = 'INSERTION SORT XX'
    a = map(int, "14 23 77 94 96 48 39 18 41 13".split() )
    array_history = []
    Sort(a, array_history)
    print desc, "RESULT", a
    prt_array_history(array_history)
    show_array_history(desc, array_history)
    print

if __name__ == '__main__':
  unittest.main()


