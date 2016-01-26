#!/usr/bin/env python
"""Tests for QuickUnion."""

from AlgsSedgewickWayne.QuickUnionUF import QuickUnionUF
from AlgsSedgewickWayne.testcode.utils import chk_arrays
from AlgsSedgewickWayne.testcode.utils import run_unions

def test_week1_lecture_print():
  """Print."""
  #  -0
  #  -1
  #  -6
  #  --5
  #  -7
  #  -8
  #  -9
  #  --2
  #  --4
  #  ---3
  print "\ntest_week1_lecture quick-union print 00:51"
  alg = QuickUnionUF(10)
  print alg
  alg.ID = [0, 1, 9, 4, 9, 6, 6, 7, 8, 9]
  print alg.ID

def test_week1_lecture():
  """From Quick Union (7:50) Lecture Example."""
  alg = QuickUnionUF(10)
  run_unions(alg, "4-3 3-8 6-5 9-4 2-1 8-9 5-0 7-2 6-1 7-3", "\nwk1_lec quick-union", "QU_demo")
  chk_arrays(alg.ID, [1, 8, 1, 8, 3, 0, 5, 1, 8, 8])

def test_week1_exercise_Q2():
  """Test 2."""
  alg = QuickUnionUF(10)
  run_unions(alg, "1-2 7-9 0-4 8-0 4-6 1-9 3-4 7-0 0-5", "\ntest_week1_exercise_Q2")
  chk_arrays(alg.ID, [4, 2, 9, 6, 6, 5, 5, 9, 4, 6])

def test_all():
  """Test All."""
  test_week1_lecture()
  test_week1_exercise_Q2()

if __name__ == '__main__':
  test_all()

