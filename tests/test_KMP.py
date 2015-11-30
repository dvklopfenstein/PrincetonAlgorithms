#!/usr/bin/env python
# TBD Finish Python port

import sys
import collections as cx
from AlgsSedgewickWayne.KMP import KMP

def test_0(pat, txt, prt=sys.stdout):
  """Searches for the pattern in the text; prints the 1st occurrence.
  Execution:    test_KMP.py pattern text
  
  Reads in two strings, the pattern and the input text, and
  searches for the pattern in the input text using the
  KMP algorithm.
  
  >>> test_0("abracadabra", "abacadabrabracabracadabrabrabracad")
  text:    abacadabrabracabracadabrabrabracad 
  pattern:               abracadabra          
  
  >>> test_0("rab", "abacadabrabracabracadabrabrabracad")
  text:    abacadabrabracabracadabrabrabracad 
  pattern:         rab
  
  >>> test_0("bcara", "abacadabrabracabracadabrabrabracad")
  text:    abacadabrabracabracadabrabrabracad 
  pattern:                                   bcara
  
  >>> test_0("rabrabracad", "abacadabrabracabracadabrabrabracad ")
  text:    abacadabrabracabracadabrabrabracad
  pattern:                        rabrabracad
  
  >>> test_0("abacad", "abacadabrabracabracadabrabrabracad")
  text:    abacadabrabracabracadabrabrabracad
  pattern: abacad
  """

  ctr = cx.Counter(txt+pat) # Ex: 5 letters: a b c d r
  kmp = KMP(pat, len(ctr))
  kmp.prt_dfa(prt)
  offset = kmp.search(txt)

  # print results
  prt.write("text:    {}\n".format(txt))

  prt.write("pattern: ")
  for i in range(offset):
    prt.write(" ")
  prt.write(pat)


#****************************************************************************
if __name__ == "__main__":
  N = len(sys.argv)
  pat = sys.argv[1] if N > 3 else "ababac"
  txt = sys.argv[2] if N > 3 else "aabdacaababacdaa"
  test_0(pat, txt)

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

