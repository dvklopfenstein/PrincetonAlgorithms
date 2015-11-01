#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Graph import Graph
from AlgsSedgewickWayne.BreadthFirstPaths import BreadthFirstPaths
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin

def main(prt=sys.stdout):
  L = len(sys.argv[1:])
  g = cli_get_fin(sys.argv[1] if L != 0 else "../thirdparty/tinyCG.txt")
  G = Graph(g)
  prt.write(str(G))

  s = int(sys.argv[2]) if L > 1 else 0
  bfs = BreadthFirstPaths(G, s)

  for v in range(G.V()):
    if bfs.hasPathTo(v):
      prt.write("{} to {} ({}):  ".format(s, v, bfs.distTo(v)))
      for x in  bfs.pathTo(v):
        if x == s: prt.write(str(x))
        else:      prt.write("-{}".format(x))
      prt.write("\n")

    else:
      prt.write.printf("{} to {} (-):  not connected\n".format(s, v))

if __name__ == '__main__':
  main()
