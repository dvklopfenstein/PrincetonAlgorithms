#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.MaxPQ import *

class MaxPQ_Tests(unittest.TestCase):

  def test_week4_lec_8_2_m11_29(self): # Lecture 8 - 2 12:18
    print "\nTEST_WEEK4_LEC_8_2_m11_29"
    o = MaxPQ(11); o
    o.insert_array(['T','P','R','N','H','O','A','E','I','G']);
    print                "Init         ", o
    o.insert('S');  print "o.insert('S')", o
    X = o.delMax(); print "o.delMax()   ", o, "Removed", X # 12:55
    X = o.delMax(); print "o.delMax()   ", o, "Removed", X # 13:49
    o.insert('S');  print "o.insert('S')", o # 14:26
    #o.draw()

  def test_week4_quiz_Q1(self):
    print "\nTEST_WEEK4_QUIZ_Q1"
    o = MaxPQ(13); o
    o.insert_array([86,82,77,75,70,35,68,31,45,30])
    o.insert(25); print "o.insert(25)", o
    o.insert(16); print "o.insert(16)", o
    o.insert(12); print "o.insert(12)", o

  def test_week4_quiz_Q2(self):
    print "\nTEST_WEEK4_QUIZ_Q2"
    o = MaxPQ(10); o
    o.insert_array([95,84,67,66,81,15,52,18,57,24])
    X = o.delMax(); print "o.delMax()   ", o, "Removed", X
    X = o.delMax(); print "o.delMax()   ", o, "Removed", X
    X = o.delMax(); print "o.delMax()   ", o, "Removed", X

  def test_week4_quiz_Q1b(self): # seed 201303
    print "\nTEST_WEEK4_QUIZ_Q1b"
    o = MaxPQ(13); o
    o.insert_array([87,83,79,41,66,24,71,30,13,63])
    print               "INIT        ", o
    o.insert(55); print "o.insert(55)", o
    o.insert(27); print "o.insert(27)", o
    o.insert(40); print "o.insert(40)", o

  def test_week4_quiz_Q2b(self):
    print "\nTEST_WEEK4_QUIZ_Q2b"
    o = MaxPQ(10); o
    o.insert_array([98,97,91,56,78,69,51,44,46,72])
    print                 "INIT         ", o
    X = o.delMax(); print "o.delMax()   ", o, "Removed", X
    X = o.delMax(); print "o.delMax()   ", o, "Removed", X
    X = o.delMax(); print "o.delMax()   ", o, "Removed", X

if __name__ == '__main__':
  unittest.main()

