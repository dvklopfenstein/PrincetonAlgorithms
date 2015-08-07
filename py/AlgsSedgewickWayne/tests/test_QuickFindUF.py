#!/usr/bin/env python
"""Test QuickFind."""

# Writtein by DV Klopfenstein

import sys

#---------------------------------------------------------------
# Sub-routines
from AlgsSedgewickWayne.QuickFindUF import QuickFindUF

def run_unions(qty, union_txt, msg, prt=sys.stdout):
  """Test user-created sets of union instructions."""
  prt.write("{MSG}\n".format(MSG=msg))
  o = QuickFindUF(qty)
  prt.write("{NODES}\n".format(NODES=o))
  for U_str in union_txt.split():
    I = [int(intstr) for intstr in U_str.split('-')]
    o.union(I[0], I[1])
    set_str = ["{L}".format(L=list(s)) for s in o.get_connected_components()]
    prt.write("{NODES} union({STR}) {SETS}\n".format(
        NODES=o, STR=U_str, SETS=' '.join(set_str)))
  return o

def failUnless(actual, expected):
  """Test to see if QuickFind passed."""
  if actual == expected:
    return
  raise Exception("TEST FAILED.")

#---------------------------------------------------------------
# Tests
def test_1():
  """Test 1."""
  o = run_unions(10, "4-3 3-8 6-5 9-4 2-1 8-9 5-0 7-2 6-1", "\ntest_1")
  failUnless(o.ID, [1, 1, 1, 8, 8, 1, 1, 1, 8, 8])

def test_week1_quiz_Q1():
  """Test 2."""
  o = run_unions(10, "6-3 6-5 9-5 7-0 3-1 9-4", "\ntest_week1_quiz_Q1 seed=686930")
  failUnless(o.ID, [0, 4, 2, 4, 4, 4, 4, 0, 8, 4])

def test_week1_quiz_Q1b():
  """Test 3."""
  o = run_unions(10, "4-7 7-8 9-7 6-5 8-6 2-0", "\ntest_week1_quiz_Q1b seed=686930")
  failUnless(o.ID, [0, 1, 0, 3, 5, 5, 5, 5, 5, 5])

def test_week1_quiz_Q1_567561():
  """Test 4."""
  run_unions(10, "0-2 3-0 5-9 5-2 7-9 7-8", "\nWeek 1 Exercise Question 1 seed = 567561")

def test_week1_quiz_Q1_838874():
  """Test 5."""
  run_unions(10, "9-1 8-0 6-1 4-0 6-0 1-7", "\nWeek 1 Exercise Question 1 seed = 838874")

def test_week1_quiz_Q1_533243():
  """Test 6."""
  run_unions(10, "5-2 0-2 5-9 2-1 3-9 4-6", "\nWeek 1 Exercise Question 1 seed = 533243")


def test_week1_quiz_Q1_489602():
  """Test 7."""
  run_unions(10, "2-7 9-6 8-1 5-9 0-8 9-1", "\nWeek 1 Exercise Question 1 seed = 489602")

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

