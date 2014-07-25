#!/usr/bin/env python

import unittest
from WeightedQuickUnionUF import *

class WeightedQuickUnionUF_Tests(unittest.TestCase):

  def test_week1_lecture(self): # Lecture: Quick-Union Improvements 1:22
    print """test_week1_lecture quick-union.
       _____6
      /    /|\ 
     4    0 2 5
    /|\    / \ 
   3 8 9  1   7
    """
    o = WeightedQuickUnionUF(10); print o
    o.union(4,3); print o, "weighted union(4,3)", "\n"
    o.union(3,8); print o, "weighted union(3,8)", "\n"
    o.union(6,5); print o, "weighted union(6,5)", "\n"
    o.union(9,4); print o, "weighted union(9,4)", "\n"
    o.union(2,1); print o, "weighted union(2,1)", "\n"
    o.union(5,0); print o, "weighted union(5,0)", "\n"
    o.union(7,2); print o, "weighted union(7,2)", "\n"
    o.union(6,1); print o, "weighted union(6,1)", "\n"
    o.union(7,3); print o, "weighted union(7,3)", "\n"
    self.failUnless( np.array_equal(o.ID, [6,2,6,4,6,6,6,2,4,4] ))


  def test_week1_exercise_Q2(self):
    print """test_week1_exercise_Q2"
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
    o = WeightedQuickUnionUF(10); print o
    o.union(1,2); print o, "weighted union(1,2)"
    o.union(7,9); print o, "weighted union(7,9)"
    o.union(0,4); print o, "weighted union(0,4)"
    o.union(8,0); print o, "weighted union(8,0)"
    o.union(4,6); print o, "weighted union(4,6)"
    o.union(1,9); print o, "weighted union(1,9)"
    o.union(3,4); print o, "weighted union(3,4)"
    o.union(7,0); print o, "weighted union(7,0)"
    o.union(0,5); print o, "weighted union(0,5)"
    print "ANSWER WEEK 1 Q2:", ' '.join(map(str,o.ID))
    self.failUnless( np.array_equal( o.ID, [0, 0, 1, 0, 0, 0, 0, 1, 0, 7] )) # Wrong Answer

  def test_week1_exercise_Q2b(self):
    print """test_week1_exercise_Q2b"""
    o = WeightedQuickUnionUF(10); print o
    o.union(0,4); print o, "weighted union(0,4)"
    o.union(7,3); print o, "weighted union(7,3)"
    o.union(9,1); print o, "weighted union(9,1)"
    o.union(5,0); print o, "weighted union(5,0)"
    o.union(8,6); print o, "weighted union(8,6)"
    o.union(8,3); print o, "weighted union(8,3)"
    o.union(8,2); print o, "weighted union(8,2)"
    o.union(9,0); print o, "weighted union(9,0)"
    o.union(3,1); print o, "weighted union(3,1)"
    print "ANSWER WEEK 1 Q2b:", ' '.join(map(str,o.ID))
    #self.failUnless( np.array_equal( o.ID, [0, 0, 1, 0, 0, 0, 0, 1, 0, 7] )) # Wrong Answer

if __name__ == '__main__':
  unittest.main()
