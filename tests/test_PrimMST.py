#!/usr/bin/env python

 #  Execution:    java PrimMST filename.txt
 #  Dependencies: EdgeWeightedGraph.java Edge.java Queue.java
 #                IndexMinPQ.java UF.java In.java StdOut.java
 #  Data files:   http://algs4.cs.princeton.edu/43mst/tinyEWG.txt
 #                http://algs4.cs.princeton.edu/43mst/mediumEWG.txt
 #                http://algs4.cs.princeton.edu/43mst/largeEWG.txt
#  Compute a minimum spanning forest using Prim's algorithm.
#
#  %  java PrimMST tinyEWG.txt 
#  1-7 0.19000
#  0-2 0.26000
#  2-3 0.17000
#  4-5 0.35000
#  5-7 0.28000
#  6-2 0.40000
#  0-7 0.16000
#  1.81000
#
#  % java PrimMST mediumEWG.txt
#  1-72   0.06506
#  2-86   0.05980
#  3-67   0.09725
#  4-55   0.06425
#  5-102  0.03834
#  6-129  0.05363
#  7-157  0.00516
#  ...
#  10.46351
#
#  % java PrimMST largeEWG.txt
#  ...
#  647.66307

    #*
     # Unit tests the <tt>PrimMST</tt> data type.
     #/
  def main(String[] args):
      In in = new In(args[0])
      EdgeWeightedGraph G = new EdgeWeightedGraph(in)
      PrimMST mst = new PrimMST(G)
      for (Edge e : mst.edges()):
          prt.write(e)
      StdOut.printf("%.5f\n", mst.weight())


if __name__ == '__main__':
  main()

