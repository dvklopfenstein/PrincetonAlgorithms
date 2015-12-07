#!/usr/bin/env python
# TBD Finish Python port

import sys
from AlgsSedgewickWayne.NFA import NFA

#****************************************************************************
# Compilation:  javac NFA.java
# Execution:    java NFA regexp text
# Dependencies: Stack.java Bag.java Digraph.java DirectedDFS.java
#
# % java NFA "(A*B|AC)D" AAAABD
# True
#
# % java NFA "(A*B|AC)D" AAAAC
# False
#
# % java NFA "(a|(bc)*d)*" abcbcd
# True
#
# % java NFA "(a|(bc)*d)*" abcbcbcdaaaabcbcdaaaddd
# True
#
# Remarks
#  -= 1 -= 1 -= 1 -= 1 -= 1-
#   - This version does not suport the + operator or multiway-or.
#
#   - This version does not handle character classes, 
#
def test_0(prt=sys.stdout):
      String regexp = "(" + args[0] + ")"
      String txt = args[1]
      if txt.indexOf('|') >= 0):
          raise new IllegalArgumentException("| character in text is not supported")
      NFA nfa = new NFA(regexp)
      prt.write(nfa.recognizes(txt))


#****************************************************************************
if __name__ == "__main__":
  test_0()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

