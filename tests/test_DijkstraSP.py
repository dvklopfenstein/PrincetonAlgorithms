#!/usr/bin/env python

#*****************************************************************************
 #  Compilation:  javac DijkstraSP.java
 #  Execution:    java DijkstraSP input.txt s
 #  Dependencies: EdgeWeightedDigraph.java IndexMinPQ.java Stack.java DirectedEdge.java
 #  Data files:   http://algs4.cs.princeton.edu/44sp/tinyEWD.txt
 #                http://algs4.cs.princeton.edu/44sp/mediumEWD.txt
 #                http://algs4.cs.princeton.edu/44sp/largeEWD.txt
 #
 #  Dijkstra's algorithm. Computes the shortest path tree.
 #  Assumes all weights are nonnegative.
 #
 #  % java DijkstraSP tinyEWD.txt 0
 #  0 to 0 (0.00)  
 #  0 to 1 (1.05)  0->4  0.38   4->5  0.35   5->1  0.32   
 #  0 to 2 (0.26)  0->2  0.26   
 #  0 to 3 (0.99)  0->2  0.26   2->7  0.34   7->3  0.39   
 #  0 to 4 (0.38)  0->4  0.38   
 #  0 to 5 (0.73)  0->4  0.38   4->5  0.35   
 #  0 to 6 (1.51)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52   
 #  0 to 7 (0.60)  0->2  0.26   2->7  0.34   
 #
 #  % java DijkstraSP mediumEWD.txt 0
 #  0 to 0 (0.00)  
 #  0 to 1 (0.71)  0->44  0.06   44->93  0.07   ...  107->1  0.07   
 #  0 to 2 (0.65)  0->44  0.06   44->231  0.10  ...  42->2  0.11   
 #  0 to 3 (0.46)  0->97  0.08   97->248  0.09  ...  45->3  0.12   
 #  0 to 4 (0.42)  0->44  0.06   44->93  0.07   ...  77->4  0.11   
 #  ...
 #
 #*****************************************************************************/

 
def main(String[] args):
    In in = new In(args[0])
    EdgeWeightedDigraph G = new EdgeWeightedDigraph(in)
    s = Integer.parseInt(args[1])

    # compute shortest paths
    DijkstraSP sp = new DijkstraSP(G, s)


    # print shortest path
    for (int t = 0; t < G.V(); t += 1):
        if sp.hasPathTo(t)):
            StdOut.printf("%d to %d (%.2f)  ", s, t, sp.distTo(t))
            for (DirectedEdge e : sp.pathTo(t)):
                StdOut.print(e + "   ")
            prt.write()
        else:
            StdOut.printf("%d to %d         no path\n", s, t)

if __name__ == '__main__':
  main()
