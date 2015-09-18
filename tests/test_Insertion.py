#!/usr/bin/env python

import sys

from   AlgsSedgewickWayne.Insertion    import Sort
from   AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory

def run(a, desc="INSERTION SORT", prt=sys.stdout):
  array_history = ArrayHistory()
  Sort(a, array_history)
  prt.write("{DESC} RESULT {A}\n".format(DESC=desc, A=' '.join(str(e) for e in a)))
  array_history.prt()
  array_history.show(desc)

def test_wk2_lec():
  run(map(int, "7 10 5 3 8 4 2 9 6".split()), "INSERTION SORT: SEED 183182")

def test_wk2_lec_best():
  """Best-case runtime is when array is already sorted."""
  run("A E E L M O P R S T X".split(), "INSERTION BEST SORT:")

def test_wk2_lec_worst():
  """Best-case runtime is when array is already sorted."""
  run("X T S R P O M L E E A".split(), "INSERTION WORST SORT:")

def test_1():
  run(map(int, "13 16 40 60 19 70 71 47 12 67".split()), "INSERTION SORT: SEED 183182")

def test_2():
  run("gold bone pink dust iris aqua rust kobi wine jade pine corn drab puce plum bark".split())

def test_3():
  run(map(int, "37 41 45 60 73 52 79 19 94 32".split()), "INSERTION SORT: seed 756506")

def test_4():
  run(map(int, "14 23 77 94 96 48 39 18 41 13".split()), "INSERTION SORT: seed 72847")

def test_5():
  run(map(int, "34 38 69 83 93 68 37 28 85 99".split()), "INSERTION SORT: seed 329024")

if __name__ == '__main__':
  run(map(int, "34 38 69 83 93 68 37 28 85 99".split()), "INSERTION SORT: seed 329024")

def run_all():
  """Run all tests."""
  test_1()
  test_2()
  test_3()
  test_4()
  test_5()

if __name__ == '__main__':
  run_all()
