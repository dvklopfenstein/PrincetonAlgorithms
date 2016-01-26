#!/usr/bin/env python
"""Tests for QuickUnion."""

from AlgsSedgewickWayne.WeightedQuickUnionUF import WeightedQuickUnionUF
from AlgsSedgewickWayne.testcode.utils import chk_arrays
from AlgsSedgewickWayne.testcode.utils import run_unions

def test_week1_lecture():
  """From Quick-Union Improvements (13:02) Lecture Example."""
  alg = WeightedQuickUnionUF(10)
  run_unions(alg, "4-3 3-8 6-5 9-4 2-1 8-9 5-0 7-2 6-1 7-3", "\nwk1_lec quick-union", "WQU_demo")
  chk_arrays(alg.ID, [6, 2, 6, 4, 6, 6, 6, 2, 4, 4])

def test_wk1_ex_455127():
  """Week 1 Exercise."""
  alg = WeightedQuickUnionUF(10)
  run_unions(alg, "8-7 7-0 9-6 5-4 4-6 8-3 1-0 7-6 7-2", "\nwk1 Ex", "work/Ex_wk1_455127")

def run_all():
  """Run all tests."""
  test_week1_lecture()
  test_wk1_ex_455127()

if __name__ == '__main__':
  test_week1_lecture()

