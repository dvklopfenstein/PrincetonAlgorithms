#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.FlowEdge import FlowEdge

def main(prt=sys.stdout):
  """Unit tests the FlowEdge data type."""
  e = FlowEdge(12, 23, 3.14)
  prt.write("{}\n".format(e))

if __name__ == '__main__':
  main()
