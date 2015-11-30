#!/usr/bin/env python
# TBD Finish Python port

import sys
from AlgsSedgewickWayne.BoyerMoore import BoyerMoore

#****************************************************************************
# Compilation:  javac BoyerMoore.java
# Execution:    java BoyerMoore pattern text
# Dependencies: StdOut.java
#
# Reads in two strings, the pattern and the input text, and
# searches for the pattern in the input text using the
# bad-character rule part of the Boyer-Moore algorithm.
# (does not implement the strong good suffix rule)
#
# % java BoyerMoore abracadabra abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad 
# pattern:               abracadabra
#
# % java BoyerMoore rab abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad 
# pattern:         rab
#
# % java BoyerMoore bcara abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad 
# pattern:                                   bcara
#
# % java BoyerMoore rabrabracad abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad
# pattern:                        rabrabracad
#
# % java BoyerMoore abacad abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad
# pattern: abacad
#
def test_0(prt=sys.stdout):
      String pat = args[0]
      String txt = args[1]
      char[] pattern = pat.toCharArray()
      char[] text    = txt.toCharArray()

      BoyerMoore boyermoore1 = new BoyerMoore(pat)
      BoyerMoore boyermoore2 = new BoyerMoore(pattern, 256)
      offset1 = boyermoore1.search(txt)
      offset2 = boyermoore2.search(text)

      # print results
      prt.write("text:    " + txt)

      StdOut.print("pattern: ")
      for (int i = 0; i < offset1; i += 1)
          StdOut.print(" ")
      prt.write(pat)

      StdOut.print("pattern: ")
      for (int i = 0; i < offset2; i += 1)
          StdOut.print(" ")
      prt.write(pat)

#****************************************************************************
if __name__ == "__main__":
  test_0()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

