#!/usr/bin/env python
# TBD: Finish Python port

#*****************************************************************************
 #  Compilation:  javac BellmanFordSP.java
 #  Execution:    java BellmanFordSP filename.txt s
 #  Dependencies: EdgeWeightedDigraph.java DirectedEdge.java Queue.java
 #                EdgeWeightedDirectedCycle.java
 #  Data files:   http://algs4.cs.princeton.edu/44sp/tinyEWDn.txt
 #                http://algs4.cs.princeton.edu/44sp/mediumEWDnc.txt
 #
 #  Bellman-Ford shortest path algorithm. Computes the shortest path tree in
 #  edge-weighted digraph G from vertex s, or finds a negative cost cycle
 #  reachable from s.
 #
 #  % java BellmanFordSP tinyEWDn.txt 0
 #  0 to 0 ( 0.00)  
 #  0 to 1 ( 0.93)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52   6->4 -1.25   4->5  0.35   5->1  0.32
 #  0 to 2 ( 0.26)  0->2  0.26   
 #  0 to 3 ( 0.99)  0->2  0.26   2->7  0.34   7->3  0.39   
 #  0 to 4 ( 0.26)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52   6->4 -1.25   
 #  0 to 5 ( 0.61)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52   6->4 -1.25   4->5  0.35
 #  0 to 6 ( 1.51)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52   
 #  0 to 7 ( 0.60)  0->2  0.26   2->7  0.34   
 #
 #  % java BellmanFordSP tinyEWDnc.txt 0
 #  4->5  0.35
 #  5->4 -0.66
 #
 #
 #*****************************************************************************/

from AlgsSedgewickWayne.EdgeWeightedDigraph import EdgeWeightedDigraph
from AlgsSedgewickWayne.BellmanFordSP import BellmanFordSP

import sys

def main(prt=sys.stdout):
  """Unit tests the BellmanFordSP data type."""
  In in = new In(args[0])
  s = Integer.parseInt(args[1])
  EdgeWeightedDigraph G = new EdgeWeightedDigraph(in)

  BellmanFordSP sp = new BellmanFordSP(G, s)

  # print negative cycle
  if sp.hasNegativeCycle()):
    for (DirectedEdge e : sp.negativeCycle())
      prt.write(e)

  # print shortest paths
  else:
    for (int v = 0; v < G.V(); v += 1):
      if sp.hasPathTo(v)):
        prt.write("{} to {} ({:5.2f})  ".format(s, v, sp.distTo(v)))
        for e in sp.pathTo(v):
          prt.write("{}   ".format(e))
        prt.write("\n")
      else:
        prt.write("{} to {}           no path\n".format(s, v))

if __name__ == '__main__':
  main()
