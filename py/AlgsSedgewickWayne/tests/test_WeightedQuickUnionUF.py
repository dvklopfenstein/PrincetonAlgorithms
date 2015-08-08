#!/usr/bin/env python
"""Test WeightedQuickUnionUF."""

from AlgsSedgewickWayne.WeightedQuickUnionUF import WeightedQuickUnionUF
from AlgsSedgewickWayne.tests.utils import chk_arrays
from AlgsSedgewickWayne.tests.utils import run_unions

def test_week1_lecture(): # Lecture: Quick-Union Improvements 1:22
  """Test"""
  msg = r"""
  test_week1_lecture quick-union.
     _____6
    /    /|\
   4    0 2 5
  /|\    / \
 3 8 9  1   7
  """
  alg = WeightedQuickUnionUF(10)
  run_unions(alg, "4-3 3-8 6-5 9-4 2-1 5-0 7-2 6-1 7-3", msg, "Lec_WtUnion")
  chk_arrays(alg.ID, [6, 2, 6, 4, 6, 6, 6, 2, 4, 4])


def test_week1_exercise_Q2():
  """Test"""
  msg = """
    test_week1_exercise_Q2"
    The correct answer is: 0 0 1 0 0 0 0 1 0 7

    Here is the id[] array after each union operation:

          0 1 2 3 4 5 6 7 8 9
    1-2:  0 1 1 3 4 5 6 7 8 9
    7-9:  0 1 1 3 4 5 6 7 8 7
    0-4:  0 1 1 3 0 5 6 7 8 7
    8-0:  0 1 1 3 0 5 6 7 0 7
    4-6:  0 1 1 3 0 5 0 7 0 7
    1-9:  0 1 1 3 0 5 0 1 0 7
    3-4:  0 1 1 0 0 5 0 1 0 7
    7-0:  0 0 1 0 0 5 0 1 0 7
    0-5:  0 0 1 0 0 0 0 1 0 7
  """
  alg = WeightedQuickUnionUF(10)
  run_unions(alg, "1-2 7-9 0-4 8-0 4-6 1-9 3-4 7-0 0-5", msg)
  chk_arrays(alg.ID, [0, 0, 1, 0, 0, 0, 0, 1, 0, 7]) # Wrong Answer

def test_week1_exercise_Q2b():
  """Test"""
  alg = WeightedQuickUnionUF(10)
  run_unions(alg, "0-4 7-3 9-1 5-0 8-6 8-3 8-2 9-0 3-1", "\ntest_week1_exercise_Q2b")

def test_week1_exercise_Q2_Fall2014_a():
  """Test"""
  alg = WeightedQuickUnionUF(10)
  run_unions(alg, "0-8 9-2 2-3 6-7 5-4 5-6 0-9 4-8 9-1",
             "\nWeek 1 Exercise Question 2 seed = 114579")
  chk_arrays(alg.ID, [9, 9, 9, 9, 5, 9, 5, 6, 0, 9])

def test_week1_exercise_Q2_Fall2014_b():
  """Test"""
  alg = WeightedQuickUnionUF(10)
  run_unions(alg, "4-5 5-9 6-8 4-3 1-2 2-6 7-4 1-7 7-0",
             "\nWeek 1 Exercise Question 2 seed = 143149")

def test_week1_exercise_Q2_Fall2014_c():
  """Test"""
  alg = WeightedQuickUnionUF(10)
  run_unions(alg, "7-2 8-6 5-9 3-8 3-1 5-7 1-0 2-6 4-6", "\nWk1 Ex Q3 seed = 265981")

def test_week1_exercise_Q2_Fall2014_d():
  """Test"""
  alg = WeightedQuickUnionUF(10)
  run_unions(alg, "2-3 1-8 1-7 5-0 0-3 8-9 7-6 2-1 4-1", "\nWk1 Ex Q3 seed = 259961" )

def test_all():
  """Run all tests."""
  test_week1_lecture()
  test_week1_exercise_Q2()
  test_week1_exercise_Q2b()
  test_week1_exercise_Q2_Fall2014_a()
  test_week1_exercise_Q2_Fall2014_b()
  test_week1_exercise_Q2_Fall2014_c()
  test_week1_exercise_Q2_Fall2014_d()


if __name__ == '__main__':
  test_all()


