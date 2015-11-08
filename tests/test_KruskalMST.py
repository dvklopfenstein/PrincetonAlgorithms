#!/usr/bin/env python

#*****************************************************************************
 #  Compilation:  javac KruskalMST.java
 #  Execution:    java  KruskalMST filename.txt
 #  Dependencies: EdgeWeightedGraph.java Edge.java Queue.java
 #                UF.java In.java StdOut.java
 #  Data files:   http://algs4.cs.princeton.edu/43mst/tinyEWG.txt
 #                http://algs4.cs.princeton.edu/43mst/mediumEWG.txt
 #                http://algs4.cs.princeton.edu/43mst/largeEWG.txt
 #
 #  Compute a minimum spanning forest using Kruskal's algorithm.
 #
 #  %  java KruskalMST tinyEWG.txt
 #  0-7 0.16000
 #  2-3 0.17000
 #  1-7 0.19000
 #  0-2 0.26000
 #  5-7 0.28000
 #  4-5 0.35000
 #  6-2 0.40000
 #  1.81000
 #
 #  % java KruskalMST mediumEWG.txt
 #  168-231 0.00268
 #  151-208 0.00391
 #  7-157   0.00516
 #  122-205 0.00647
 #  8-152   0.00702
 #  156-219 0.00745
 #  28-198  0.00775
 #  38-126  0.00845
 #  10-123  0.00886
 #  ...
 #  10.46351

from AlgsSedgewickWayne.EdgeWeightedGraph import EdgeWeightedGraph
from AlgsSedgewickWayne.KruskalMST import KruskalMST
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array
import sys

def main(prt=sys.stdout):
  a = cli_get_array()
  G = EdgeWeightedGraph(a)
  mst = KruskalMST(G)
  for e in mst.edges():
    prt.write(e)
  prt.write("{:.5f}\n".format(mst.weight()))

if __name__ == '__main__':
  main()
