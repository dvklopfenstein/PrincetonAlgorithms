#!/usr/bin/env python
# TBD Finish Python port


#*****************************************************************************
 #  Compilation:  javac FordFulkerson.java
 #  Execution:    java FordFulkerson V E
 #  Dependencies: FlowNetwork.java FlowEdge.java Queue.java
 #
 #  Ford-Fulkerson algorithm for computing a max flow and 
 #  a min cut using shortest augmenting path rule.
 #
 #*****************************************************************************/

import sys
from AlgsSedgewickWayne.FlowNetwork import FlowNetwork
from AlgsSedgewickWayne.FordFulkerson import FordFulkerson

def main(prt=sys.stdout):
  """Unit tests the FordFulkerson data type."""

  # create flow network with V vertices and E edges
  V = int(sys.argv[1])
  E = int(sys.argv[2])
  s = 0 
  t = V-1
  G = FlowNetwork(V, E)
  prt.write("{}\n".format(G))

  # compute maximum flow and minimum cut
  maxflow = FordFulkerson(G, s, t)
  prt.write("Max flow from {} tp {}\n".format(s,  t))
  for v in range(G.V()):
    for e in G.adj(v):
      if (v == e.from()) and e.flow() > 0)
        prt.write("{}   \n".format(e))

  # print min-cut
  prt.write("Min cut: \n")
  for v in range(G.V()):
    if maxflow.inCut(v): prt.write("{} ".format(v))
  prt.write("\n")

  prt.write("Max flow value = {}\n".format(maxflow.value()))

if __name__ == '__main__':
  main()
