#!/usr/bin/env python
"""Tests using a Stack"""

import sys

from AlgsSedgewickWayne.Stack import Stack
from AlgsSedgewickWayne.testcode.ArrayHistory import run

def test_Stack_lec_quiz(prt=sys.stdout):
  """Run the quiz in Stats 1, Week 2 lecture, 'Stacks (16:24)'"""
  expected = "5 4 3 2 1"
  run(Stack(), "1 2 3 4 5 - - - - -", expected, details=None)
  run(Stack(), "1 2 5 - 3 4 - - - -", expected, details=None)
  run(Stack(), "5 - 1 2 3 - 4 - - -", expected, details=None)
  run(Stack(), "5 - 4 - 3 - 2 - 1 -", expected, details=None)

def test_wk2_ex_Stacks_489125(prt=sys.stdout):
  """(seed = 489125)"""
  # Suppose that an intermixed sequence of 10 push and 10 pop
  # operations are performed on a LIFO stack. The pushes push
  # the letters 0 through 9 in order; the pops print out the
  # return value. Which of the following output sequence(s)
  # could occur?
  # result = run(Stack(), "0 1 2 3 4 5 6 7 8 9")
  prt.write("\n489125 DONE\n")
  #exp = "0 1 3 2 4 6 8 5 7 9"
  result = run(Stack(), "0 - 1 - 2 3 - - 4 - 5 6 - 7 8 - - 9 -")

  exp = "6 5 4 3 2 1 0 7 8 9"
  result = run(Stack(), "0 1 2 3 4 5 6 - - - - - - - 7 - 8 - 9 -")

  exp = "3 4 5 8 9 7 6 2 1 0"
  result = run(Stack(), "0 1 2 3 - 4 - 5 - 6 7 8 - 9 - - - - - -")

  exp = "0 3 7 6 5 4 2 9 8 1"
  result = run(Stack(), "0 - 1 2 3 - 4 5 6 7 - - - - - 8 9 - - -")

  # exp = "1 0 3 5 2 7 6 8 9 4"
  result = run(Stack(), "0 1 - - 2 3 - 4 5 - 6 7 8 9")

def test_wk2_ex_Stacks_634506(prt=sys.stdout):
  """(seed = 634506)"""
  # Suppose that an intermixed sequence of 10 push and 10 pop
  # operations are performed on a LIFO stack. The pushes push
  # the letters 0 through 9 in order; the pops print out the
  # return value. Which of the following output sequence(s)
  # could occur?
  prt.write("\n634506 DONE\n")
  result = run(Stack(), "0 1 2 3 - - - 4 5 - 6 7 8 9")
  #exp = "3 2 1 5 0 6 7 8 9 4"
  exp = "2 1 0 3 4 5 6 7 8 9"
  result = run(Stack(), "0 1 2 - - - 3 - 4 - 5 - 6 - 7 - 8 - 9 -", exp)
  exp = "0 1 3 2 4 5 6 8 7 9"
  result = run(Stack(), "0 - 1 - 2 3 - - 4 - 5 - 6 - 7 8 - - 9 -", exp)
  result = run(Stack(), "0 1 2 3 - 4 5 - - 6 7 8 9")
  #exp = "3 5 2 4 6 1 0 8 7 9"
  exp = "2 1 6 5 4 7 3 8 0 9"
  result = run(Stack(), "0 1 2 - - 3 4 5 6 - - - 7 - - 8 - - 9 -", exp)


def test_wk2_ex_Stacks_634506b(prt=sys.stdout):
  """(seed = 634506)"""
  prt.write("\n634506b DONE\n")
  result = run(Stack(), "0 1 2 3 - - - 4 5 - - 6 7 8 9")
  #exp = "3 2 1 5 0 6 7 8 9 4"
  exp = "2 1 0 3 4 5 6 7 8 9"
  result = run(Stack(), "0 1 2 - - - 3 - 4 - 5 - 6 - 7 - 8 - 9 -", exp)
  exp = "0 1 3 2 4 5 6 8 7 9"
  result = run(Stack(), "0 - 1 - 2 3 - - 4 - 5 - 6 - 7 8 - - 9 -", exp)
  result = run(Stack(), "0 1 2 3 - 4 5 - - 6 7 8 9")
  #exp = "3 5 2 4 6 1 0 8 7 9"
  exp = "2 1 6 5 4 7 3 8 0 9"
  result = run(Stack(), "0 1 2 - - 3 4 5 6 - - - 7 - - 8 - - 9 -", exp)

def test_wk2_ex_Stacks_489125b(prt=sys.stdout):
  """(seed = 489125)"""
  prt.write("\n489125b\n")
  #result = run(Stack(), "0 1 2 3 4 5 6 7 8 9")
  result = run(Stack(), "0 - 1 - 2 3 - - 4 - 5 6 - 7 8 - - 9")
  #exp = "0 1 3 2 4 6 8 5 7 9")
  exp = "6 5 4 3 2 1 0 7 8 9"
  result = run(Stack(), "0 1 2 3 4 5 6 - - - - - - - 7 - 8 - 9 -", exp)
  exp = "3 4 5 8 9 7 6 2 1 0"
  result = run(Stack(), "0 1 2 3 - 4 - 5 - 6 7 8 - 9 - - - - - -", exp)
  exp = "0 3 7 6 5 4 2 9 8 1"
  result = run(Stack(), "0 - 1 2 3 - 4 5 6 7 - - - - - 8 9 - - -", exp)
  result = run(Stack(), "0 1 - - 2 3 - 4 5 - - 6 7 8 9")
  #exp = "1 0 3 5 2 7 6 8 9 4")

def simple_test():
  """Simple sanity check test."""
  # (seed = 353020)
  run(Stack(), "0 1 2 3 4 5 6 7 8 9")
  run(Stack(), "0 1 - - 2 3 4 5 6 7 - 8 - - 9 - - - - -")

def default_examples():
  """Example from lecture."""
  run(Stack(), "to be or not to be - - - - - -")
  # Slide 6 Week 2 Lecture 4-1-Stacks(16-24)
  run(Stack(), "to be or not to - be - - that - - - is")

def run_all():
  """Run all tests."""
  test_wk2_ex_Stacks_489125b()
  test_wk2_ex_Stacks_634506b()
  test_wk2_ex_Stacks_634506()
  test_wk2_ex_Stacks_489125()
  simple_test()
  default_examples()

if __name__ == '__main__':
  if len(sys.argv) == 1:
    run_all()
  else:
    run(Stack(), sys.argv[1])


