#!/usr/bin/env python
# TBD Finish Python port

import sys
from AlgsSedgewickWayne.GREP import GREP

#****************************************************************************
# Compilation:  javac GREP.java
# Execution:    java GREP regexp < input.txt
# Dependencies: NFA.java StdOut.java
# Data files:   http:#algs4.cs.princeton.edu/54regexp/tinyL.txt
#
# This program takes an RE as a command-line argument and prints
# the lines from standard input having some substring that
# is in the language described by the RE. 
#
# % more tinyL.txt
# AC
# AD
# AAA
# ABD
# ADD
# BCD
# ABCCBD
# BABAAA
# BABBAAA
#
# %  java GREP "(A*B|AC)D" < tinyL.txt
# ABD
# ABCCBD
#
def test_0(prt=sys.stdout):
      String regexp = "(.*" + args[0] + ".*)"
      NFA nfa = new NFA(regexp)
      while (StdIn.hasNextLine()): 
          String line = StdIn.readLine()
          if nfa.recognizes(line)):
              prt.write(line)

#****************************************************************************
if __name__ == "__main__":
  test_0()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

