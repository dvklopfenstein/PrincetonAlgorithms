#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Shell import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

import random

def test_wk2_lec_a(prt=sys.stdout):
  """From Alg 1, week 2, lecture Shellsort (10:48) at 1:48"""
  a = "S H E L L S O R T E X A M P L E".split()
  run(a, 'SHELL SORT LEC EX')

def test_wk2_lec_b(prt=sys.stdout):
  """From Alg 1, week 2, lecture Shellsort (10:48) at 2:02"""
  a = "M O L E E X A S P R T".split()
  run(a, 'SHELL SORT LEC EX', sort_seq=[1, 3, 7])

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
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  ah.show('SHELL')

def test_3():
  # Keys are 'A' and 'B':
  a = map(int, "51 99 35 60 96 18 19 64 42 10".split())
  run(a, "SHELL CUR")

def test_q3a():
  # Q: The number of compares to Shellsort (with Knuth's 3x+1 increments) 
  # an array of length N depends only on N (and not on the items in the array).
  # A: The number of compares to Shellsort the array { 1, 2, 3 } is 2; 
  # the number of compares to Shellsort the array { 3, 2, 1 } is three.
  run([1, 2, 3], "SHELL N=3 => 2 COMPARES")
  run([3, 2, 1], "SHELL N=3 => 3 COMPARES")

def test_q3b():
  """Wk2 Ex Sorts Q3"""
  # An array of N distinct keys that is both 2-sorted and 3-sorted 
  # can be 1-sorted in one insertion-sort pass, using only N compares.
  a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  run(a, 'SHELL EX', sort_seq=[1, 2, 3])


def run(a, desc=None, sort_seq=None, prt=sys.stdout):
  ah = ArrayHistory()
  Sort(a, array_history=ah, sort_seq=sort_seq)
  if desc is None:
    desc = "SHELL SORT" 
  prt.write("{DESC} RESULT {A}\n".format(DESC=desc, A=' '.join(str(e) for e in a)))
  ah.prt()
  ah.show(desc)

def run_all(prt=sys.stdout):
  test_wk2_lec_a(prt)
  test_wk2_lec_b(prt)
  test_1(prt)
  test_2()
  test_3()
  test_q3a()

def cli():
  N = len(sys.argv)
  if N == 1:
    run_all()
  elif N == 2:
    run(cli_get_array())

if __name__ == '__main__':
  cli()


