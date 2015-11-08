#!/usr/bin/env python

#*****************************************************************************
 #  Compilation:  javac LazyPrimMST.java
 #  Execution:    java LazyPrimMST filename.txt
 #  Dependencies: EdgeWeightedGraph.java Edge.java Queue.java
 #                MinPQ.java UF.java In.java StdOut.java
 #  Data files:   http://algs4.cs.princeton.edu/43mst/tinyEWG.txt
 #                http://algs4.cs.princeton.edu/43mst/mediumEWG.txt
 #                http://algs4.cs.princeton.edu/43mst/largeEWG.txt
 #
 #  Compute a minimum spanning forest using a lazy version of Prim's 
 #  algorithm.
 #
 #  %  java LazyPrimMST tinyEWG.txt 
 #  0-7 0.16000
 #  1-7 0.19000
 #  0-2 0.26000
 #  2-3 0.17000
 #  5-7 0.28000
 #  4-5 0.35000
 #  6-2 0.40000
 #  1.81000
 #
 #  % java LazyPrimMST mediumEWG.txt
 #  0-225   0.02383
 #  49-225  0.03314
 #  44-49   0.02107
 #  44-204  0.01774
 #  49-97   0.03121
 #  202-204 0.04207
 #  176-202 0.04299
 #  176-191 0.02089
 #  68-176  0.04396
 #  58-68   0.04795
 #  10.46351
 #
 #  % java LazyPrimMST largeEWG.txt
 #  ...
 #  647.66307
 #
 #*****************************************************************************/


from AlgsSedgewickWayne.EdgeWeightedGraph import EdgeWeightedGraph
from AlgsSedgewickWayne.LazyPrimMST import LazyPrimMST
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array
import sys

def main(fin_G, prt=sys.stdout):
  a = cli_get_array(fin_G)
  G = EdgeWeightedGraph(a)
  mst = LazyPrimMST(G)
  for e in mst.edges():
    prt.write(e)
  prt.write("{:.5f}\n".format(mst.weight()))

if __name__ == '__main__':
  main("../thirdparty/tinyEWG.txt")
