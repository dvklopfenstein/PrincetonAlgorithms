#!/usr/bin/env python

# TBD: Finish 

import sys
import os

def run_tinyST():
 #  % java RedBlackBST < tinyST.txt
 #  A 8
 #  C 4
 #  E 12
 #  H 5
 #  L 11
 #  M 9
 #  P 10
 #  R 3
 #  S 0
 #  X 7
  pass

def run_all():
  pass

if __name__ == '__main__':
  N = len(sys.argv)
  if N == 1:
    run_all()
  else:
    for arg in sys.argv[1:]:
      if os.isfile(arg):
        pass
        
 
