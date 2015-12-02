#!/usr/bin/env python
# TBD Finish Python port

import sys
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

  kmp = KMP(pat)
  kmp.prt_dfa(prt)
  offset = kmp.search(txt)

  # print results
  ret = ["text:    {}\n".format(txt)]

  ret.append("pattern: ")
  for i in range(offset):
    ret.append(" ")
  ret.append("{}\n".format(pat))
  prt.write("{}\n".format(''.join(ret)))
  return ''.join(ret)


def cli():
  N = len(sys.argv)
  if N == 3:
    test_0(pat=sys.argv[1], txt=sys.argv[2], prt=sys.stdout)
  else:
    test_0(pat="ababac", txt="aabdacaababacdaa", prt=sys.stdout)

#****************************************************************************
if __name__ == "__main__":
  cli()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

