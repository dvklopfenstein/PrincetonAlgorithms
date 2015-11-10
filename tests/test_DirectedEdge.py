#!/usr/bin/env python

from AlgsSedgewickWayne.DirectedEdge import DirectedEdge
import sys

def main(prt=sys.stdout):
  e = DirectedEdge(12, 34, 5.67)
  prt.write("{}\n".format(str(e)))

if __name__ == '__main__':
  main()
