#!/usr/bin/env python
# TBD Finish Python port

import sys
from AlgsSedgewickWayne.KMP import KMP

#****************************************************************************
# Compilation:  javac KMP.java
# Execution:    java KMP pattern text
# Dependencies: StdOut.java
#
# Reads in two strings, the pattern and the input text, and
# searches for the pattern in the input text using the
# KMP algorithm.
#
# % java KMP abracadabra abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad 
# pattern:               abracadabra          
#
# % java KMP rab abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad 
# pattern:         rab
#
# % java KMP bcara abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad 
# pattern:                                   bcara
#
# % java KMP rabrabracad abacadabrabracabracadabrabrabracad 
# text:    abacadabrabracabracadabrabrabracad
# pattern:                        rabrabracad
#
# % java KMP abacad abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad
# pattern: abacad
#
def test_0(prt=sys.stdout):
      String pat = args[0]
      String txt = args[1]
      char[] pattern = pat.toCharArray()
      char[] text    = txt.toCharArray()

      KMP kmp1 = new KMP(pat)
      offset1 = kmp1.search(txt)

      KMP kmp2 = new KMP(pattern, 256)
      offset2 = kmp2.search(text)

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

