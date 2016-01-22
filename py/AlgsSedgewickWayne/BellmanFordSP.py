"""Bellman-Ford shortest path algorithm in Graphs w/no neg. cycles."""
# TBD: Finish Python port

import collections as cx
from AlgsSedgewickWayne.EdgeWeightedDigraph import EdgeWeightedDigraph
from AlgsSedgewickWayne.EdgeWeightedDirectedCycle import EdgeWeightedDirectedCycle

class BellmanFordSP(object):
  """Gets SP tree in edge-wt'd digraph from src s, or finds a neg. cost cycle reachable from s."""
  Inf = float('Inf')

  def __init__(self, G, s): # G:EdgeWeightedDigraph O(V+E) wc
    self._distTo  = [self.Inf for i in range(G.V())] # distTo[v] = distance  of shortest s->v path
    self._distTo[s] = 0.0
    self._edgeTo  = [None for i in range(G.V())] # edgeTo[v] = last edge on shortest s->v path
    self._onQueue = [False for i in range(G.V())] # onQueue[v] = is v currently on the queue?
    self._cost = 0    # number of calls to relax()
    self._cycle = None # Iterable<DirectedEdge> negative cycle (or null if no such cycle)

    # Bellman-Ford algorithm
    self._queue = cx.deque() # new Queue<Integer>() # queue of vertices to relax
    self._queue.append(s) # enqueue(s)
    self._onQueue[s] = True
    while self._queue and not self.hasNegativeCycle():
      v = self._queue.popleft() # dequeue()
      self._onQueue[v] = False
      self._relax(G, v)
    assert _check(G, s)

  def _relax(self, G, v):
    """relax vertex v and put other endpoints on queue if changed"""
    for e in G.adj(v):
      w = e.get_to()
      if self._distTo[w] > self._distTo[v] + e.weight()):
         self._distTo[w] = self._distTo[v] + e.weight()
         self._edgeTo[w] = e
         if not self._onQueue[w]:
           self_queue.append(w) # enqueue(w)
           self._onQueue[w] = True
      if self._cost%G.V() == 0:
        self.findNegativeCycle()
        if self.hasNegativeCycle(): return  # found a negative cycle
      self._cost += 1

  # Is there a negative cycle reachable from the source vertex <tt>s</tt>?
  def hasNegativeCycle(self): return self._cycle is not None # O(k)

  # Returns a negative cycle reachable from the src s, or None if there is no such cycle.
  def negativeCycle(self): return self._cycle # O(# edges returned)

  def _findNegativeCycle(self):
    """by finding a cycle in predecessor graph"""
    V = len(self._edgeTo)
    spt = EdgeWeightedDigraph(V)
    for v in range(V):
      if self._edgeTo[v] is not None:
         spt.addEdge(self._edgeTo[v])

    finder = EdgeWeightedDirectedCycle(spt)
    self._cycle = finder.cycle()

  def distTo(self, v): # O(k)
    """Returns the length of a shortest path from the source vertex s to vertex v."""
    if self.hasNegativeCycle():
      raise Exception("Negative cost cycle exists")
    return self._distTo[v]

  # Is there a path from the source <tt>s</tt> to vertex <tt>v</tt>?
  def hasPathTo(self, v): return self._distTo[v] < sel.Inf # O(k)

  def pathTo(self, v): # O(# edges returned)
    """Returns a shortest path from the source s to vertex v."""
    if self.hasNegativeCycle():
        raise Exception("Negative cost cycle exists")
    if not self.hasPathTo(v): return None
    path = [] # new Stack<DirectedEdge>()
    e = self._edgeTo[v]
    while e is not None: 
      path.append(e) # push(e)
      e = self._edgeTo[e.get_from()]
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

# NEGATIVE WEIGHTS (21:01)

# PROPOSITION: Dynamic programming algorithm computes SPT in any 
# edge-weighted digraph with no negative cycles in time proportional to E*V
#
# PROOF IDEA: After pass, i, found shortest path containing at most i edges. (In book)

# OBSERVATION: If distTo[v] does not change during pass i, no need to relax any 
# edge pointing from v in pass i+1.
#
# FIFO IMPLEMENTATION: Maintain QUEUE of vertices whose distTo[] changed
# ***Be careful to keep at most one copy of each vertex on queue (why?)
#
# OVERALL EFFECT:
#  * The running time is still proportional to E*V in worst case
#  * But much faster than that in practice

# QUESTION: The dynamic programming algorithm computes a shortest-paths tree in
# edge-weighter digraph with no negative cycles in time proportional to ...
# ANSWER: EV
# EXPLANATION: There are V passes; each passes relaxes each of teh E edges.

# BELLMAN-FORD is NOT a greedy algorithm (so can do negative edges)
#
# FUNDAMENTAL IDEA BEHIND BELLMAN-FORD:
#  * THERE CAN BE AT MOST |V|-1 edges in a path starting from the starting node
#    to any other node in the graph.
#  * |V| or more edges in a path -> repeated vertex -> cycle


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
