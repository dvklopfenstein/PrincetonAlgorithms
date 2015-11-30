#!/usr/bin/env python
# TBD Finish Python port

import sys
from AlgsSedgewickWayne.RabinKarp import RabinKarp

#****************************************************************************
# Compilation:  javac RabinKarp.java
# Execution:    java RabinKarp pat txt
# Dependencies: StdOut.java
#
# Reads in two strings, the pattern and the input text, and
# searches for the pattern in the input text using the
# Las Vegas version of the Rabin-Karp algorithm.
#
# % java RabinKarp abracadabra abacadabrabracabracadabrabrabracad
# pattern: abracadabra
# text:    abacadabrabracabracadabrabrabracad 
# match:                 abracadabra          
#
# % java RabinKarp rab abacadabrabracabracadabrabrabracad
# pattern: rab
# text:    abacadabrabracabracadabrabrabracad 
# match:           rab                         
#
# % java RabinKarp bcara abacadabrabracabracadabrabrabracad
# pattern: bcara
# text:         abacadabrabracabracadabrabrabracad 
#
# %  java RabinKarp rabrabracad abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad
# pattern:                        rabrabracad
#
# % java RabinKarp abacad abacadabrabracabracadabrabrabracad
# text:    abacadabrabracabracadabrabrabracad
# pattern: abacad
#
def test_0(prt=sys.stdout):
      String pat = args[0]
      String txt = args[1]

      RabinKarp searcher = new RabinKarp(pat)
      offset = searcher.search(txt)

      # print results
      prt.write("text:    " + txt)

      # from brute force search method 1
      StdOut.print("pattern: ")
      for (int i = 0; i < offset; i += 1)
          StdOut.print(" ")
      prt.write(pat)

#****************************************************************************
if __name__ == "__main__":
  test_0()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

