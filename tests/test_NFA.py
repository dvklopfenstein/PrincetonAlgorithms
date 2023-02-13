#!/usr/bin/env python

from sys import stdout
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
def test_NFA(prt=stdout):
    assert _run("(A*B|AC)D", "AAAABD") == True
    assert _run("(A*B|AC)D", "AAAAC") == False
    assert _run("(a|(bc)*d)*", "abcbcd") == True
    assert _run("(a|(bc)*d)*", "abcbcbcdaaaabcbcdaaaddd") == True
    assert _run("([ACGTUN][-+]([a-z]+|[0-9]+)[.?]?(,[0-9]+)*;)*", "") == True  #False
    #String regexp = "(" + args[0] + ")"
    #String txt = args[1]
    #if txt.indexOf('|') >= 0):
    #    raise new IllegalArgumentException("| character in text is not supported")

def _run(regexp, txt):
    nfa = NFA(regexp)
    return nfa.recognizes(txt)


#****************************************************************************
if __name__ == "__main__":
    test_NFA()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-present, DV Klopfenstein, PhD, Python implementation.
