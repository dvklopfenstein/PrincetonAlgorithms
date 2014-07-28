#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.Queue import *
import AlgsSedgewickWayne.ArrayHistory as H

class Queue_Tests(unittest.TestCase):
  import Queue
  """ Tests Queue."""

  def test_wk2_ex_Queues_608030(self):
    # Question 2
    # (seed = 608030)
    # Suppose that an intermixed sequence of 10 enqueue and 10
    # dequeue operations are performed on a FIFO queue. The
    # enqueues add the letters 0 through 9 in order; the dequeues
    # print out the return value. Which of the following output
    # sequence(s) could occur?
    # r = run("0 1 2 3 4 5 6 7 8 9")
    r = run("0 - 1 2 - 3 4 5 6 7 8 9")
    #self.failUnless( H.chk(r, "0 2 1 3 7 4 9 6 8 5") )

    r = run("0 1 2 - - - 3 4 5 - 6 - - 7 8 9")
    #self.failUnless( H.chk(r, "0 1 2 5 6 4 8 9 3 7") )

    r = run("0 1 2 3 4 5 6 7 8 9 - - - - - - - - - -")
    self.failUnless( H.chk(r, "0 1 2 3 4 5 6 7 8 9") )

    r = run("0 - 1 2 3 4 5 6 7 8 9")
    #self.failUnless( H.chk(r, "0 7 4 1 8 3 6 2 9 5") )

    r = run("0 - 1 2 3 4 5 6 7 8 9")
    #self.failUnless( H.chk(r, "0 4 5 1 8 6 2 3 9 7") )

  def test_wk2_ex_Queues_511394(self):
    # (seed = 511394)
    # Suppose that an intermixed sequence of 10 enqueue and 10
    # dequeue operations are performed on a FIFO queue. The
    # enqueues add the letters 0 through 9 in order; the dequeues
    # print out the return value. Which of the following output
    # sequence(s) could occur?
    r = run("0 1 - - 2 3 4 - 5 6 7 8 9")
    #self.failUnless( H.chk(r, "0 1 4 9 6 8 5 2 7 3") )
    #self.failUnless( H.chk(r, "0 1 2 3 4 5 8 9 6 7") )
    #self.failUnless( H.chk(r, "0 1 2 4 8 6 5 9 7 3") )
    #self.failUnless( H.chk(r, "0 1 2 3 4 7 6 8 5 9") )
    #self.failUnless( H.chk(r, "0 1 2 3 4 5 6 7 8 9") )

if __name__ == '__main__':
  unittest.main()


