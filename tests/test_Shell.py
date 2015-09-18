#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Shell import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory

import random

def test_wk2_lec(prt=sys.stdout):
  """From Alg 1, week 2, lecture Shellsort (10:48)"""
  desc = 'SHELL SORT LEC EX'
  a = "M O L E E X A S P R T".split()
  array_history = ArrayHistory()
  Sort(a, array_history)
  prt.write("{DESC} RESULT: {ARRAY}\n\n".format(DESC=desc, ARRAY=' '.join(a)))
  array_history.prt()
  array_history.show(desc)

def test_1(prt=sys.stdout):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  desc = 'SHELL SORT'
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  array_history = ArrayHistory()
  Sort(a, array_history)
  prt.write("{DESC} RESULT {ARRAY}\n".format(DESC=desc, ARRAY=a))
  array_history.prt()
  array_history.show(desc)

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
  array_history = ArrayHistory()
  Sort(a, array_history)
  array_history.show('SHELL CUR')

def run_all():
  test_1()
  test_2()
  test_3()

if __name__ == '__main__':
  run_all()


