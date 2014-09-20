#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.Insertion import *
from AlgsSedgewickWayne.ArrayHistory import *

def run(a, desc="INSERTION SORT"):
  array_history = []
  Sort(a, array_history)
  print desc, "RESULT", a
  prt_array_history(array_history)
  show_array_history(desc, array_history)
  print

class Insertion_Tests(unittest.TestCase):

  def test_1(self):
    run(map(int, "13 16 40 60 19 70 71 47 12 67".split()), "INSERTION SORT: SEED 183182")

  def test_2(self):
    run("gold bone pink dust iris aqua rust kobi wine jade pine corn drab puce plum bark".split())

  def test_3(self):
    run(map(str, "37 41 45 60 73 52 79 19 94 32".split()), "INSERTION SORT: seed 756506")

  def test_4(self):
    run(map(str, "14 23 77 94 96 48 39 18 41 13".split()), "INSERTION SORT: seed 72847")

if __name__ == '__main__':
  #unittest.main()
  run(map(str, "34 38 69 83 93 68 37 28 85 99".split()), "INSERTION SORT: seed 329024")


