#!/usr/bin/env python

import unittest
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#from .. import Queue
import Queue


class Queue_Tests(unittest.TestCase):
  import Queue
  """ Tests Queue."""

  def chk(self, a, txt):
    b = txt.split()
    return len(a)==len(b) and len(a)==sum([1 for i,j in zip(a,b) if i==j])

  def test_wk2_ex_Queues_608030(self):
    # Question 2
    # (seed = 608030)
    # Suppose that an intermixed sequence of 10 enqueue and 10
    # dequeue operations are performed on a FIFO queue. The
    # enqueues add the letters 0 through 9 in order; the dequeues
    # print out the return value. Which of the following output
    # sequence(s) could occur?
    # r = Queue.run("0 1 2 3 4 5 6 7 8 9")
    r = Queue.run("0 - 1 2 - 3 4 5 6 7 8 9")
    #self.failUnless( self.chk(r, "0 2 1 3 7 4 9 6 8 5") )

    r = Queue.run("0 1 2 - - - 3 4 5 - 6 - - 7 8 9")
    #self.failUnless( self.chk(r, "0 1 2 5 6 4 8 9 3 7") )

    r = Queue.run("0 1 2 3 4 5 6 7 8 9 - - - - - - - - - -")
    self.failUnless( self.chk(r, "0 1 2 3 4 5 6 7 8 9") )

    r = Queue.run("0 - 1 2 3 4 5 6 7 8 9")
    #self.failUnless( self.chk(r, "0 7 4 1 8 3 6 2 9 5") )

    r = Queue.run("0 - 1 2 3 4 5 6 7 8 9")
    #self.failUnless( self.chk(r, "0 4 5 1 8 6 2 3 9 7") )

  def test_wk2_ex_Queues_511394(self):
    # (seed = 511394)
    # Suppose that an intermixed sequence of 10 enqueue and 10
    # dequeue operations are performed on a FIFO queue. The
    # enqueues add the letters 0 through 9 in order; the dequeues
    # print out the return value. Which of the following output
    # sequence(s) could occur?
    r = Queue.run("0 1 - - 2 3 4 - 5 6 7 8 9")
    #self.failUnless( self.chk(r, "0 1 4 9 6 8 5 2 7 3") )
    #self.failUnless( self.chk(r, "0 1 2 3 4 5 8 9 6 7") )
    #self.failUnless( self.chk(r, "0 1 2 4 8 6 5 9 7 3") )
    #self.failUnless( self.chk(r, "0 1 2 3 4 7 6 8 5 9") )
    #self.failUnless( self.chk(r, "0 1 2 3 4 5 6 7 8 9") )

if __name__ == '__main__':
  print 'PATH', sys.path
  print 'PATH', os.path.dirname(__file__)
  unittest.main()


