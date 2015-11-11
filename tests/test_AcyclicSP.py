#!/usr/bin/env python
"""Test AcyclicSP"""

#*****************************************************************************
 #  Compilation:  javac AcyclicSP.java
 #  Execution:    java AcyclicSP V E
 #  Dependencies: EdgeWeightedDigraph.java DirectedEdge.java Topological.java
 #  Data files:   http://algs4.cs.princeton.edu/44sp/tinyEWDAG.txt
 #
 #  Computes shortest paths in an edge-weighted acyclic digraph.
 #
 #  % java AcyclicSP tinyEWDAG.txt 5
 #  5 to 0 (0.73)  5->4  0.35   4->0  0.38   
 #  5 to 1 (0.32)  5->1  0.32   
 #  5 to 2 (0.62)  5->7  0.28   7->2  0.34   
 #  5 to 3 (0.61)  5->1  0.32   1->3  0.29   
 #  5 to 4 (0.35)  5->4  0.35   
 #  5 to 5 (0.00)  
 #  5 to 6 (1.13)  5->1  0.32   1->3  0.29   3->6  0.52   
 #  5 to 7 (0.28)  5->7  0.28   
 #
 #*****************************************************************************/

import sys
from AlgsSedgewickWayne.AcyclicSP import AcyclicSP
from AlgsSedgewickWayne.EdgeWeightedDigraph import EdgeWeightedDigraph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

def main(s=0, prt=sys.stdout):
  a = cli_get_array()
  G = EdgeWeightedGraph(a)
  prt.write(str(G))

  # find shortest path from s to each other vertex in DAG
  sp = AcyclicSP(G, s)
  for v in range(G.V()):
    if sp.hasPathTo(v):
      prt.write("{} to {} ({:.2f})  ".format(s, v, sp.distTo(v)))
      for e in sp.pathTo(v):
        prt.write("{}   ".format(e))
      prt.write("\n")
    else:
      prt.write("{} to {}         no path\n".format(s, v))

if __name__ == '__main__':
  main()
