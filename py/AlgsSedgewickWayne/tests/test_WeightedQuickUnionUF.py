#!/usr/bin/env python
"""Tests for QuickUnion."""

from AlgsSedgewickWayne.WeightedQuickUnionUF import WeightedQuickUnionUF
from AlgsSedgewickWayne.tests.utils import chk_arrays
from AlgsSedgewickWayne.tests.utils import run_unions

def test_week1_lecture():
  """From Quick-Union Improvements (13:02) Lecture Example."""
  alg = WeightedQuickUnionUF(10)
  run_unions(alg, "4-3 3-8 6-5 9-4 2-1 8-9 5-0 7-2 6-1 7-3", "\nwk1_lec quick-union", "WQU_demo")
  chk_arrays(alg.ID, [6, 2, 6, 4, 6, 6, 6, 2, 4, 4])

if __name__ == '__main__':
  test_week1_lecture()

