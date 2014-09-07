#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.WeightedQuickUnionUF import *

def run_unions(qty, union_txt, msg):
  print msg
  o = WeightedQuickUnionUF(qty); print o
  for U_str in union_txt.split():
    I = map(int, U_str.split('-'))
    o.union(I[0], I[1])
    print o, "weighted union({})".format(U_str)
  return o



class WeightedQuickUnionUF_Tests(unittest.TestCase):

  def test_week1_lecture(self): # Lecture: Quick-Union Improvements 1:22
    msg = """
    test_week1_lecture quick-union.
       _____6
      /    /|\ 
     4    0 2 5
    /|\    / \ 
   3 8 9  1   7
    """
    o = run_unions(10, "4-3 3-8 6-5 9-4 2-1 5-0 7-2 6-1 7-3", msg)
    self.failUnless( np.array_equal(o.ID, [6,2,6,4,6,6,6,2,4,4] ))


  def test_week1_exercise_Q2(self):
    msg = """
      test_week1_exercise_Q2"
      The correct answer is: 0 0 1 0 0 0 0 1 0 7
      
      Here is the id[] array after each union operation:
      
            0 1 2 3 4 5 6 7 8 9 
      1-2:  0 1 1 3 4 5 6 7 8 9 
      7-9:  0 1 1 3 4 5 6 7 8 7 
      0-4:  0 1 1 3 0 5 6 7 8 7 
      8-0:  0 1 1 3 0 5 6 7 0 7 
      4-6:  0 1 1 3 0 5 0 7 0 7 
      1-9:  0 1 1 3 0 5 0 1 0 7 
      3-4:  0 1 1 0 0 5 0 1 0 7 
      7-0:  0 0 1 0 0 5 0 1 0 7 
      0-5:  0 0 1 0 0 0 0 1 0 7 
    """
    o = run_unions(10, "1-2 7-9 0-4 8-0 4-6 1-9 3-4 7-0 0-5", msg)
    print "ANSWER WEEK 1 Q2:", ' '.join(map(str,o.ID))
    self.failUnless( np.array_equal( o.ID, [0, 0, 1, 0, 0, 0, 0, 1, 0, 7] )) # Wrong Answer


  def test_week1_exercise_Q2b(self):
    o = run_unions(10, "0-4 7-3 9-1 5-0 8-6 8-3 8-2 9-0 3-1", "\ntest_week1_exercise_Q2b")
    print "ANSWER WEEK 1 Q2b:", ' '.join(map(str,o.ID))
    #self.failUnless( np.array_equal( o.ID, [0, 0, 1, 0, 0, 0, 0, 1, 0, 7] )) # Wrong Answer


  def test_week1_exercise_Q2_Fall2014(self):
    run_unions(10, "0-8 9-2 2-3 6-7 5-4 5-6 0-9 4-8 9-1", 
      "\nWeek 1 Exercise Question 2 seed = 114579")


if __name__ == '__main__':
  unittest.main()


