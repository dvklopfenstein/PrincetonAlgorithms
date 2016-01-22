#!/usr/bin/env python
"""Test QuickFind."""

# Writtein by DV Klopfenstein

from AlgsSedgewickWayne.QuickFindUF import QuickFindUF
from AlgsSedgewickWayne.testcode.utils import chk_arrays
from AlgsSedgewickWayne.testcode.utils import run_unions

def test_1():
  """Test 1."""
  alg = QuickFindUF(10)
  run_unions(alg, "4-3 3-8 6-5 9-4 2-1 8-9 5-0 7-2 6-1", "\ntest_1")
  chk_arrays(alg.ID, [1, 1, 1, 8, 8, 1, 1, 1, 8, 8])

def test_week1_quiz_Q1():
  """Test 2."""
  alg = QuickFindUF(10)
  run_unions(alg, "6-3 6-5 9-5 7-0 3-1 9-4", "\ntest_week1_quiz_Q1")
  chk_arrays(alg.ID, [0, 4, 2, 4, 4, 4, 4, 0, 8, 4])

def test_week1_quiz_Q1b():
  """Test 3."""
  alg = QuickFindUF(10)
  run_unions(alg, "4-7 7-8 9-7 6-5 8-6 2-0", "\ntest_week1_quiz_Q1b")
  chk_arrays(alg.ID, [0, 1, 0, 3, 5, 5, 5, 5, 5, 5])

def test_week1_quiz_Q1_567561():
  """Test 4."""
  alg = QuickFindUF(10)
  run_unions(alg, "0-2 3-0 5-9 5-2 7-9 7-8", "\nWeek 1 Exercise Question 1")

def test_week1_quiz_Q1_838874():
  """Test 5."""
  alg = QuickFindUF(10)
  run_unions(alg, "9-1 8-0 6-1 4-0 6-0 1-7", "\nWeek 1 Exercise Question 1")

def test_week1_quiz_Q1_533243():
  """Test 6."""
  alg = QuickFindUF(10)
  run_unions(alg, "5-2 0-2 5-9 2-1 3-9 4-6", "\nWeek 1 Exercise Question 1")

def test_week1_quiz_Q1_489602():
  """Test 7."""
  alg = QuickFindUF(10)
  run_unions(alg, "2-7 9-6 8-1 5-9 0-8 9-1", "\nWeek 1 Exercise Question 1")

def test_week1_quiz_Q1_126228():
  """Test 126228."""
  alg = QuickFindUF(10)
  run_unions(alg, "8-9 4-0 8-5 2-6 1-7 0-3", "\nWeek 1 Exercise Question 1")

def test_all():
  """Test All."""
  test_1()
  test_week1_quiz_Q1()
  test_week1_quiz_Q1b()
  test_week1_quiz_Q1_567561()
  test_week1_quiz_Q1_838874()
  test_week1_quiz_Q1_533243()
  test_week1_quiz_Q1_489602()

if __name__ == '__main__':
  test_all()
  #test_week1_quiz_Q1_489602()

