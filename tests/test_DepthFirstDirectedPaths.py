#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.DepthFirstDirectedPaths import DepthFirstDirectedPaths
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

def main(prt=sys.stdout):
  a = cli_get_array()
  G = Digraph(a)
  s = 0
  dfs = DepthFirstDirectedPaths(G, s)

  prt.write("{}\n".format(G))

  for v in range(G.V()):
    if dfs.hasPathTo(v):
      prt.write("{SRC} to {V}:  ".format(SRC=s, V=v))
      for x in dfs.pathTo(v):
        if x == s: prt.write(str(x))
        else:      prt.write("-{X}".format(X=x))
      prt.write("\n")

    else:
      prt.write("{SRC} to {V}:  not connected\n".format(SRC=s, V=v))

if __name__ == '__main__':
  main()
