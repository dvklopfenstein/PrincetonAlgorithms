#!/usr/bin/env python3
"""Test non-deterministic finate state automata (machine)"""
# pylint: disable=invalid-name

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
def test_nfa():
    """Test non-deterministic finate state automata (machine)"""
    assert     _run(1, "((A*B|AC)D)", "AAAABD")
    assert not _run(2, "((A*B|AC)D)", "AAAAC")
    assert     _run(3, "((a|(bc)*d)*)", "abcbcd")
    assert     _run(4, "((a|(bc)*d)*)", "abcbcbcdaaaabcbcdaaaddd")
    assert not _run(5, "((a|(bc)*d)*)", "ZZZZZZZZZZZZZZZZZZZZZZZ")
    assert not _run(5, "(a|(bc)*d)", "")
    #String regexp = "(" + args[0] + ")"
    #String txt = args[1]
    #if txt.indexOf('|') >= 0):
    #    raise new IllegalArgumentException("| character in text is not supported")

def _run(num, regexp, txt):
    nfa = NFA(regexp)
    matched = nfa.recognizes(txt)
    nfa.wr_png(f'test_NFA_{num}.png')
    return matched


#****************************************************************************
if __name__ == "__main__":
    test_nfa()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-present, DV Klopfenstein, PhD, Python implementation.
