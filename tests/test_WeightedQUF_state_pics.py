#!/usr/bin/env python
"""Tests for QuickUnion."""

from AlgsSedgewickWayne.WeightedQuickUnionUF import WeightedQuickUnionUF
from AlgsSedgewickWayne.testcode.utils import run_unions

def test_wk1_ex_166199():
  """Week 1 Q3 Exercise Seed 166199."""
  alg = WeightedQuickUnionUF(10)
  alg.wr_png_tree_statestr("6 1 6 6 0 6 1 5 0 5 ", "./work/Wk1_Ex_Q3_166199_0.png")
  alg.wr_png_tree_statestr("4 4 4 4 4 9 4 4 7 7 ", "./work/Wk1_Ex_Q3_166199_1.png")
  alg.wr_png_tree_statestr("7 1 8 2 2 9 4 2 8 7 ", "./work/Wk1_Ex_Q3_166199_2.png")
  alg.wr_png_tree_statestr("6 6 6 5 6 7 3 6 7 7 ", "./work/Wk1_Ex_Q3_166199_3.png")
  alg.wr_png_tree_statestr("0 3 2 3 4 5 9 9 8 9 ", "./work/Wk1_Ex_Q3_166199_4.png")

def test_wk1_ex_166199b():
  """Try to create this state: 4 4 4 4 4 9 4 4 7 7"""
  alg = WeightedQuickUnionUF(10)
  unions = [(9, 5), (7, 8), (7, 9), (4, 0), (1, 4), (2, 4), (3, 4), (6, 4), (7, 4)]
  try_unions(alg, 166199, unions)

def test_wk1_ex_686557x():
  """Try to create this state: 2 2 2 1 5 1 2 6 5 1"""
  alg = WeightedQuickUnionUF(10)
  unions = [(5, 4), (5, 8), (1, 3), (1, 9), (2, 0), (6, 7), (2, 6), (1, 5), (1, 2)]
  try_unions(alg, 166199, unions)

def test_wk1_ex_x1():
  """Try to create this state: 2 2 2 1 5 1 2 6 5 1"""
  alg = WeightedQuickUnionUF(10)
  unions = [(7, 9), (2, 8), (2, 1), (5, 6), (1, 4), (9, 6), (4, 9), (3, 4), (9, 0)]
  try_unions(alg, "x", unions)


def try_unions(alg, seed, unions):
  """Try various unions to determine if we can create a specific state."""
  png_base = "./work/s{SEED}_".format(SEED=seed)
  alg.union_pngs(unions, png_base)

def run_all():
  """Run all tests."""
  test_wk1_ex_166199()
  test_wk1_ex_166199b()

if __name__ == '__main__':
  run_all()

