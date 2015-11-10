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

package edu.princeton.cs.algs4


#*
 #  The <tt>DijkstraSP</tt> class represents a data type for solving the
 #  single-source shortest paths problem in edge-weighted digraphs
 #  where the edge weights are nonnegative.
 #  <p>
 #  This implementation uses Dijkstra's algorithm with a binary heap.
 #  The constructor takes time proportional to <em>E</em> log <em>V</em>,
 #  where <em>V</em> is the number of vertices and <em>E</em> is the number of edges.
 #  Afterwards, the <tt>distTo()</tt> and <tt>hasPathTo()</tt> methods take
 #  constant time and the <tt>pathTo()</tt> method takes time proportional to the
 #  number of edges in the shortest path returned.
 #  <p>
 #  For additional documentation,    
 #  see <a href="http://algs4.cs.princeton.edu/44sp">Section 4.4</a> of    
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne. 
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
class DijkstraSP(object):
  """Computes a shortest-paths tree from the src vertex s to every other vertex in the edge-weighted DAG G."""
  private double[] distTo;          # distTo[v] = distance  of shortest s->v path
  private DirectedEdge[] edgeTo;    # edgeTo[v] = last edge on shortest s->v path
  private IndexMinPQ<Double> pq;    # priority queue of vertices

    #*
     #
     # @param  G the edge-weighted digraph
     # @param  s the source vertex
     # @throws IllegalArgumentException if an edge weight is negative
     # @throws IllegalArgumentException unless 0 &le; <tt>s</tt> &le; <tt>V</tt> - 1
     #/
  public DijkstraSP(EdgeWeightedDigraph G, s):
      for (DirectedEdge e : G.edges()):
          if e.weight() < 0)
              raise new IllegalArgumentException("edge " + e + " has negative weight")

      distTo = new double[G.V()]
      edgeTo = new DirectedEdge[G.V()]
      for (int v = 0; v < G.V(); v += 1)
          distTo[v] = Double.POSITIVE_INFINITY
      distTo[s] = 0.0

      # relax vertices in order of distance from s
      pq = new IndexMinPQ<Double>(G.V())
      pq.insert(s, distTo[s])
      while (!pq.isEmpty()):
          v = pq.delMin()
          for (DirectedEdge e : G.adj(v))
              relax(e)

      # check optimality conditions
      assert check(G, s)

  def _relax(DirectedEdge e):
    """relax edge e and update pq if changed"""
    v, w = e.get_from_to()
    if self._distTo[w] > (self._distTo[v] + e.weight()):
       self._distTo[w] =  self._distTo[v] + e.weight()
       self._edgeTo[w] = e
       if pq.contains(w): pq.decrease(w, self._distTo[w])
       else               pq.insert(w, self._distTo[w])

  def distTo(self, v):
    """Returns the length of a shortest path from the source vertex s to vertex v."""
    return self._distTo[v]

  def hasPathTo(self, v):
    """Returns true if there is a path from the source vertex s to vertex v."""
    return self._distTo[v] < self.Inf

  def pathTo(self, v):
    """Returns a shortest path from the source vertex s to vertex v."""
    if not hasPathTo(v): return None
    path = [] # new Stack<DirectedEdge>()
    e = edgeTo[v]
    while e is not None: 
      path.append(e) # push(e)
      e = self.edgeTo[e.from()]
    return path


  # check optimality conditions:
  # (i) for all edges e:            distTo[e.to()] <= distTo[e.from()] + e.weight()
  # (ii) for all edge e on the SPT: distTo[e.to()] == distTo[e.from()] + e.weight()
  def _check(EdgeWeightedDigraph G, s):

      # check that edge weights are nonnegative
      for (DirectedEdge e : G.edges()):
          if e.weight() < 0):
              System.err.println("negative edge weight detected")
              return False

      # check that distTo[v] and edgeTo[v] are consistent
      if distTo[s] != 0.0 or edgeTo[s] is not None):
          System.err.println("distTo[s] and edgeTo[s] inconsistent")
          return False
      for (int v = 0; v < G.V(); v += 1):
          if v == s) continue
          if edgeTo[v] is None and distTo[v] != Double.POSITIVE_INFINITY):
              System.err.println("distTo[] and edgeTo[] inconsistent")
              return False

      # check that all edges e = v->w satisfy distTo[w] <= distTo[v] + e.weight()
      for (int v = 0; v < G.V(); v += 1):
          for (DirectedEdge e : G.adj(v)):
              w = e.to()
              if distTo[v] + e.weight() < distTo[w]):
                  System.err.println("edge " + e + " not relaxed")
                  return False

      # check that all edges e = v->w on SPT satisfy distTo[w] == distTo[v] + e.weight()
      for (int w = 0; w < G.V(); w += 1):
          if edgeTo[w] is None) continue
          DirectedEdge e = edgeTo[w]
          v = e.from()
          if w != e.to()) return False
          if distTo[v] + e.weight() != distTo[w]):
              System.err.println("edge " + e + " on shortest path not tight")
              return False
      return True


# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
