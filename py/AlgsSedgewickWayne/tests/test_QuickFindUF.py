#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.QuickFindUF import *

def run_unions(qty, union_txt, msg):
  print msg
  o = QuickFindUF(qty); print o
  for U_str in union_txt.split():
    I = map(int, U_str.split('-'))
    o.union(I[0], I[1])
    print o, "union({}) {}".format(U_str, o.get_connected_components())
  return o

class QuickFindUF_Tests(unittest.TestCase):

  #def test_1(self):
  #  o = run_unions(10, "4-3 3-8 6-5 9-4 2-1 8-9 5-0 7-2 6-1", "\ntest_1")
  #  self.failUnless( o.ID == [1,1,1,8,8,1,1,1,8,8] )

  #def test_week1_quiz_Q1(self):
  #  o = run_unions(10, "6-3 6-5 9-5 7-0 3-1 9-4", "\ntest_week1_quiz_Q1 seed=686930")
  #  self.failUnless( o.ID == [0,4,2,4,4,4,4,0,8,4] )

  #def test_week1_quiz_Q1b(self):
  #  o = run_unions(10, "4-7 7-8 9-7 6-5 8-6 2-0", "\ntest_week1_quiz_Q1b seed=686930")
  #  self.failUnless( o.ID == [0,1,0,3,5,5,5,5,5,5])

  #def test_week1_quiz_Q1_567561(self):
  #  run_unions(10, "0-2 3-0 5-9 5-2 7-9 7-8", "\nWeek 1 Exercise Question 1 seed = 567561")

  #def test_week1_quiz_Q1_838874(self):
  #  run_unions(10, "9-1 8-0 6-1 4-0 6-0 1-7", "\nWeek 1 Exercise Question 1 seed = 838874")

  #def test_week1_quiz_Q1_533243(self):
  #  run_unions(10, "5-2 0-2 5-9 2-1 3-9 4-6", "\nWeek 1 Exercise Question 1 seed = 533243")


  def test_week1_quiz_Q1_489602(self):
    run_unions(10, "2-7 9-6 8-1 5-9 0-8 9-1", "\nWeek 1 Exercise Question 1 seed = 489602")


if __name__ == '__main__':
  unittest.main()

