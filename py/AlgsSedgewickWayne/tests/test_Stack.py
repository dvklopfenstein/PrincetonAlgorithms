#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.Stack import *
import AlgsSedgewickWayne.ArrayHistory as H

class Stack_Tests(unittest.TestCase):

  def test_wk2_ex_Stacks_489125(self):
    # (seed = 489125)
    # Suppose that an intermixed sequence of 10 push and 10 pop
    # operations are performed on a LIFO stack. The pushes push
    # the letters 0 through 9 in order; the pops print out the
    # return value. Which of the following output sequence(s)
    # could occur?
    # o, stk = run("0 1 2 3 4 5 6 7 8 9")
    print "\n489125 DONE"
    o, stk = run("0 - 1 - 2 3 - - 4 - 5 6 - 7 8 - - 9 -")
    #self.failUnless( H.chk(o, "0 1 3 2 4 6 8 5 7 9") )

    o, stk = run("0 1 2 3 4 5 6 - - - - - - - 7 - 8 - 9 -")
    self.failUnless( H.chk(o, "6 5 4 3 2 1 0 7 8 9") )

    o, stk = run("0 1 2 3 - 4 - 5 - 6 7 8 - 9 - - - - - -")
    self.failUnless( H.chk(o, "3 4 5 8 9 7 6 2 1 0") )

    o, stk = run("0 - 1 2 3 - 4 5 6 7 - - - - - 8 9 - - -")
    self.failUnless( H.chk(o, "0 3 7 6 5 4 2 9 8 1") )

    o, stk = run("0 1 - - 2 3 - 4 5 - 6 7 8 9")
    # self.failUnless( H.chk(o, "1 0 3 5 2 7 6 8 9 4") )
    print

  def test_wk2_ex_Stacks_634506(self):
    # (seed = 634506)
    # Suppose that an intermixed sequence of 10 push and 10 pop
    # operations are performed on a LIFO stack. The pushes push
    # the letters 0 through 9 in order; the pops print out the
    # return value. Which of the following output sequence(s)
    # could occur?
    print "\n634506 DONE"
    o, stk = run("0 1 2 3 - - - 4 5 - 6 7 8 9")
    #self.failUnless( H.chk(o, "3 2 1 5 0 6 7 8 9 4") )
    o, stk = run("0 1 2 - - - 3 - 4 - 5 - 6 - 7 - 8 - 9 -")
    self.failUnless( H.chk(o, "2 1 0 3 4 5 6 7 8 9") )
    o, stk = run("0 - 1 - 2 3 - - 4 - 5 - 6 - 7 8 - - 9 -")
    self.failUnless( H.chk(o, "0 1 3 2 4 5 6 8 7 9") )
    o, stk = run("0 1 2 3 - 4 5 - - 6 7 8 9")
    #self.failUnless( H.chk(o, "3 5 2 4 6 1 0 8 7 9") )
    o, stk = run("0 1 2 - - 3 4 5 6 - - - 7 - - 8 - - 9 -")
    self.failUnless( H.chk(o, "2 1 6 5 4 7 3 8 0 9") )


  def test_wk2_ex_Stacks_634506b(self):
    # (seed = 634506)
    print "\n634506b DONE"
    o, stk = run("0 1 2 3 - - - 4 5 - - 6 7 8 9")
    #self.failUnless( H.chk(o, "3 2 1 5 0 6 7 8 9 4") )
    o, stk = run("0 1 2 - - - 3 - 4 - 5 - 6 - 7 - 8 - 9 -")
    self.failUnless( H.chk(o, "2 1 0 3 4 5 6 7 8 9") )
    o, stk = run("0 - 1 - 2 3 - - 4 - 5 - 6 - 7 8 - - 9 -")
    self.failUnless( H.chk(o, "0 1 3 2 4 5 6 8 7 9") )
    o, stk = run("0 1 2 3 - 4 5 - - 6 7 8 9")
    #self.failUnless( H.chk(o, "3 5 2 4 6 1 0 8 7 9") )
    o, stk = run("0 1 2 - - 3 4 5 6 - - - 7 - - 8 - - 9 -")
    self.failUnless( H.chk(o, "2 1 6 5 4 7 3 8 0 9") )

  def test_wk2_ex_Stacks_489125b(self):
    # (seed = 489125)
    print "\n489125b"
    #o, stk = run("0 1 2 3 4 5 6 7 8 9")
    o, stk = run("0 - 1 - 2 3 - - 4 - 5 6 - 7 8 - - 9")
    #self.failUnless( H.chk(o, "0 1 3 2 4 6 8 5 7 9"))
    o, stk = run("0 1 2 3 4 5 6 - - - - - - - 7 - 8 - 9 -")
    self.failUnless( H.chk(o, "6 5 4 3 2 1 0 7 8 9"))
    o, stk = run("0 1 2 3 - 4 - 5 - 6 7 8 - 9 - - - - - -")
    self.failUnless( H.chk(o, "3 4 5 8 9 7 6 2 1 0"))
    o, stk = run("0 - 1 2 3 - 4 5 6 7 - - - - - 8 9 - - -")
    self.failUnless( H.chk(o, "0 3 7 6 5 4 2 9 8 1"))
    o, stk = run("0 1 - - 2 3 - 4 5 - - 6 7 8 9")
    #self.failUnless( H.chk(o, "1 0 3 5 2 7 6 8 9 4"))

if __name__ == '__main__':
  #unittest.main()
  # (seed = 353020)
  o, stk = run("0 1 2 3 4 5 6 7 8 9"); print o
  o, stk = run("0 1 - - 2 3 4 5 6 7 - 8 - - 9 - - - - -"); print o
