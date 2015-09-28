#!/usr/bin/env python

import fileinput
import sys
from AlgsSedgewickWayne.Heap import Sort

def main(prt=sys.stdout):
  """$ echo "9 3 6 1 7 3 0" | test_Heap.py
     0 1 3 3 6 7 9

     $ test_Heap.py
     3
     2
     1
     <ctrl-d> <ctrl-d>
     1 2 3
  """
  a = [w.rstrip("\n\r") for t in fileinput.input() for w in t.split(" ")]
  Sort(a)
  prt.write("{}\n".format(' '.join([str(e) for e in a])))

if __name__ == '__main__':
  main()
