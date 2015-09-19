#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Shell import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory
from AlgsSedgewickWayne.InputArgs import get_seq__int_or_str

import random

def test_wk2_lec(prt=sys.stdout):
  """From Alg 1, week 2, lecture Shellsort (10:48)"""
  a = "M O L E E X A S P R T".split()
  run(a, 'SHELL SORT LEC EX')

def test_1(prt=sys.stdout):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  run(a, 'SHELL SORT')

# This test did not work as hoped, but is based on this Week 2 Exercise question:
# TBD: Make a test which demonstrates this idea...
#
# QUESTION: If two items a and b have equal keys and a appears before b
#   in the input array, then a appears before b in the array
#   after Shellsorting (with Knuth's 3x+1 increments) the array.
# ANSWER(FALSE): Consider an array with five items
#     { (B, 1), (B, 2), (B, 3), (B, 4), (A, 1) },
#   where the key is the letter A or B. After Shellsort, the array is
#     { (A, 1), (B, 2), (B, 3), (B, 4), (B, 1) }.
#   This property is known as stability. Stay tuned for the mergesort lecture.
def test_2():
  # Keys are 'A' and 'B':
  a = [  {'B':1}, {'B':2}, {'B':3}, {'B':4}, {'B':5}, {'A':1} ]
  array_history = ArrayHistory()
  Sort(a, array_history)
  array_history.show('SHELL')

def test_3():
  # Keys are 'A' and 'B':
  a = map(int, "51 99 35 60 96 18 19 64 42 10".split())
  run(a, "SHELL CUR")

def test_q3a():
  # Q: The number of compares to Shellsort (with Knuth's 3x+1 increments) 
  # an array of length N depends only on N (and not on the items in the array).
  # A: The number of compares to Shellsort the array { 1, 2, 3 } is 2; 
  # the number of compares to Shellsort the array { 3, 2, 1 } is three.
  run([1, 2, 3], "SHELL 2 COMPARES")
  run([3, 2, 1], "SHELL 3 COMPARES")


def run(a, desc=None, prt=sys.stdout):
  array_history = ArrayHistory()
  Sort(a, array_history)
  if desc is None:
    desc = "SHELL SORT" 
  prt.write("{DESC} RESULT {A}\n".format(DESC=desc, A=' '.join(str(e) for e in a)))
  array_history.prt()
  array_history.show(desc)

def run_all():
  test_1()
  test_2()
  test_3()
  test_q3a()

def cli():
  N = len(sys.argv)
  if N == 1:
    run_all()
  elif N == 2:
    run(get_seq__int_or_str(sys.argv[1]))

if __name__ == '__main__':
  cli()


