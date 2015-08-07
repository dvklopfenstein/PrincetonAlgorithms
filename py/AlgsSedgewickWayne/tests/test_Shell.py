#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.Shell import *
from AlgsSedgewickWayne.ArrayHistory import *

import random

class Selection_Tests(unittest.TestCase):

  def test_1(self):
    # (seed = 183182)
    # Give the array that results after the first 4 exchanges when
    # selection sorting the following array:
    desc = 'SHELL SORT'
    a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
    array_history = []
    Sort(a, array_history)
    print desc, "RESULT", a
    prt_array_history(array_history)
    show_array_history(desc, array_history)
    print

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
  def test_2(self):
    # Keys are 'A' and 'B':
    a = [  {'B':1}, {'B':2}, {'B':3}, {'B':4}, {'B':5}, {'A':1} ]
    array_history = []
    Sort(a, array_history)
    show_array_history('SHELL', array_history)

  def test_3(self):
    # Keys are 'A' and 'B':
    a = map(int, "51 99 35 60 96 18 19 64 42 10".split())
    array_history = []
    Sort(a, array_history)
    show_array_history('SHELL CUR', array_history)

if __name__ == '__main__':
  unittest.main()


