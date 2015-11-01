#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.CC import CC
from AlgsSedgewickWayne.Graph import Graph
import collections as cx
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin

def main(prt=sys.stdout):
  L = len(sys.argv[1:])
  g = cli_get_fin(sys.argv[1] if L != 0 else "../thirdparty/tinyG.txt")
  G = Graph(g)
  cc = CC(G)

  # number of connected components
  M = cc.count()
  prt.write("{M} components\n".format(M=M))

  # compute list of vertices in each connected component
  components = [cx.deque() for i in range(M)]
  for v in range(G.V()):
    components[cc.id(v)].append(v) # enqueue(v)

  # print results
  for i in range(M):
    for v in components[i]:
      prt.write("{v} ".format(v=v))
    prt.write("\n")

if __name__ == '__main__':
  main()
