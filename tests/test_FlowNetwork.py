#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.FlowNetwork import FlowNetwork

def main(prt=sys.stdout):
  """Unit tests the FlowNetwork data type."""
  a = new In(args[0])
  G = FlowNetwork(a)
  prt.write(G)

if __name__ == '__main__':
  main()
