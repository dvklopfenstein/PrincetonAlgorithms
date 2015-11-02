#!/usr/bin/env python

from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin
import sys

def main(prt=sys.stdout):
  g = cli_get_fin(sys.argv[1] if len(sys.argv) != 1 else "../thirdparty/tinyDG.txt")
  print "GGGGGG", g
  G = Digraph(g)
  prt.write("{}\n".format(G))

if __name__ == '__main__':
  main()
