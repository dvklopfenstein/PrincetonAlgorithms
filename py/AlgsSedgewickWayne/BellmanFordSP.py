"""Bellman-Ford shortest path algorithm."""
# TBD: Finish Python port

 #  The <tt>BellmanFordSP</tt> class represents a data type for solving the
 #  single-source shortest paths problem in edge-weighted digraphs with
 #  no negative cycles. 
 #  The edge weights can be positive, negative, or zero.
 #  This class finds either a shortest path from the source vertex <em>s</em>
 #  to every other vertex or a negative cycle reachable from the source vertex.
 #  <p>
 #  This implementation uses the Bellman-Ford-Moore algorithm.
 #  The constructor takes time proportional to <em>V</em> (<em>V</em> + <em>E</em>)
 #  in the worst case, where <em>V</em> is the number of vertices and <em>E</em>
 #  is the number of edges.
 #  Afterwards, the <tt>distTo()</tt>, <tt>hasPathTo()</tt>, and <tt>hasNegativeCycle()</tt>
 #  methods take constant time; the <tt>pathTo()</tt> and <tt>negativeCycle()</tt>
 #  method takes time proportional to the number of edges returned.
 #  <p>
 #  For additional documentation,    
 #  see <a href="http://algs4.cs.princeton.edu/44sp">Section 4.4</a> of    
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne. 
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

import collections as cx
from AlgsSedgewickWayne.EdgeWeightedDigraph import EdgeWeightedDigraph
from AlgsSedgewickWayne.EdgeWeightedDirectedCycle import EdgeWeightedDirectedCycle

class BellmanFordSP(object):
  """Gets SP tree in edge-wt'd digraph from src s, or finds a neg. cost cycle reachable from s."""

  Inf = float('Inf')
  def _relax()
  def _cycle(or None if no such cycle)

    #*
     # Computes a shortest paths tree from <tt>s</tt> to every other vertex in
     # the edge-weighted digraph <tt>G</tt>.
     # @param G the acyclic digraph
     # @param s the source vertex
     # @throws IllegalArgumentException unless 0 &le; <tt>s</tt> &le; <tt>V</tt> - 1
     #/
  def __init__(self, G, s): # G:EdgeWeightedDigraph
    self._distTo  = [self.Inf for i in range(G.V())] # distTo[v] = distance  of shortest s->v path
    self._edgeTo  = new DirectedEdge[G.V()] # edgeTo[v] = last edge on shortest s->v path
    self._onQueue = new boolean[G.V()] # onQueue[v] = is v currently on the queue?
    self._distTo[s] = 0.0

    # Bellman-Ford algorithm
    queue = cx.deque # new Queue<Integer>() # queue of vertices to relax
    queue.enqueue(s)
    self._onQueue[s] = True
    while queue and not self.hasNegativeCycle():
      v = queue.dequeue()
      self._onQueue[v] = False
      self._relax(G, v)

    assert check(G, s)

  def _relax(self, G, v):
    """relax vertex v and put other endpoints on queue if changed"""
    for e in G.adj(v):
      w = e.to()
      if self._distTo[w] > self._distTo[v] + e.weight()):
        self._distTo[w] = self._distTo[v] + e.weight()
        self._[w] = e
        if not self._onQueue[w]:
          queue.enqueue(w)
          self._onQueue[w] = True
      if cost += 1 % G.V() == 0):
        self.findNegativeCycle()
        if self.hasNegativeCycle(): return  # found a negative cycle

  # Is there a negative cycle reachable from the source vertex <tt>s</tt>?
  def hasNegativeCycle(self): return cycle is not None

  # Returns a negative cycle reachable from the src s, or None if there is no such cycle.
  def negativeCycle(self): return cycle

  def _findNegativeCycle(self):
    """by finding a cycle in predecessor graph"""
    V = len(self._)
    spt = EdgeWeightedDigraph(V)
    for v in range(V):
      if self._[v] is not None:
         spt.addEdge(self._[v])

    EdgeWeightedDirectedCycle finder = new EdgeWeightedDirectedCycle(spt)
    cycle = finder.cycle()

  def distTo(self, v):
    """Returns the length of a shortest path from the source vertex s to vertex v."""
    if self.hasNegativeCycle():
      raise Exception("Negative cost cycle exists")
    return self._distTo[v]

  # Is there a path from the source <tt>s</tt> to vertex <tt>v</tt>?
  def hasPathTo(self, v): return self._distTo[v] < sel.Inf

  def pathTo(self, v):
    """Returns a shortest path from the source s to vertex v."""
    if self.hasNegativeCycle():
        raise Exception("Negative cost cycle exists")
    if not hasPathTo(v): return None
    path = [] # new Stack<DirectedEdge>()
    e = self._[v]
    while e is not None: 
      path.append(e) # push(e)
      e = self._[e.from()]
    return path

  # check optimality conditions: either 
  # (i) there exists a negative cycle reacheable from s
  #     or 
  # (ii)  for all edges e = v->w:            self._distTo[w] <= self._distTo[v] + e.weight()
  # (ii') for all edges e = v->w on the SPT: self._distTo[w] == self._distTo[v] + e.weight()
  def _check(EdgeWeightedDigraph G, s):

      # has a negative cycle
      if hasNegativeCycle()):
          double weight = 0.0
          for (DirectedEdge e : negativeCycle()):
              weight += e.weight()
          if weight >= 0.0):
              System.err.println("error: weight of negative cycle = " + weight)
              return False

      # no negative cycle reachable from source
      else:

          # check that self._distTo[v] and self._[v] are consistent
          if self._distTo[s] != 0.0 or self._[s] is not None):
              System.err.println("distanceTo[s] and self._[s] inconsistent")
              return False
          for (int v = 0; v < G.V(); v += 1):
              if v == s) continue
              if self._[v] is None and self._distTo[v] != Double.POSITIVE_INFINITY):
                  System.err.println("self._distTo[] and self._[] inconsistent")
                  return False

          # check that all edges e = v->w satisfy self._distTo[w] <= self._distTo[v] + e.weight()
          for (int v = 0; v < G.V(); v += 1):
              for (DirectedEdge e : G.adj(v)):
                  w = e.to()
                  if self._distTo[v] + e.weight() < self._distTo[w]):
                      System.err.println("edge " + e + " not relaxed")
                      return False

          # check that all edges e = v->w on SPT satisfy self._distTo[w] == self._distTo[v] + e.weight()
          for (int w = 0; w < G.V(); w += 1):
              if self._[w] is None) continue
              DirectedEdge e = self._[w]
              v = e.from()
              if w != e.to()) return False
              if self._distTo[v] + e.weight() != self._distTo[w]):
                  System.err.println("edge " + e + " on shortest path not tight")
                  return False

      prt.write("Satisfies optimality conditions")
      prt.write()
      return True

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
