#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.UnorderedArrayMaxPQ import UnorderedArrayMaxPQ

def main(prt=sys.stdout):
  pq = UnorderedArrayMaxPQ(10)
  pq.insert("this")
  pq.insert("is")
  pq.insert("a")
  pq.insert("test")
  while not pq.isEmpty(): 
    prt.write("{}\n".format(pq.delMax()))

if __name__ == '__main__':
  main()
