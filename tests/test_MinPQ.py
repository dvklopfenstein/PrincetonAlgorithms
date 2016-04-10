#!/usr/bin/env python
#TBD: Finish Python port

import sys
from AlgsSedgewickWayne.MinPQ import MinPQ
import fileinput

def main(prt=sys.stdout):
  """Unit tests the MinPQ data type."""
  pq = MinPQ()
  """Read stdin until ctrl-D is seen."""
  for item in fileinput.input():
    item = item.rstrip("\n\r")
    if item != "-": 
      pq.insert(item)
    elif not pq.isEmpty(): 
      prt.write("{} ".format(pq.delMin()))
  prt.write("({SZ}) left on pq)".format(SZ=pq.size()))

if __name__ == '__main__':
  main()
