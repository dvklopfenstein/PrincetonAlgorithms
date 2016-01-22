"""Solve single-source shortest paths problem in edge-weighted DAG"""
# TBD: Finish Python port

from AlgsSedgewickWayne.DirectedEdge import DirectedEdge
from AlgsSedgewickWayne.Topological import Topological

class AcyclicSP(object):
  """Computes a shortest paths tree from s to every other vertex in the DAG G."""
  Inf = float('Inf')

  def __init__(self, G, s): # G=DAG, v=source vertex O(V+E)
    self._distTo = [self.Inf for i in range(G.V())]  # distance  of shortest s->v path
    self._edgeTo = [None for i in range(G.V())] # last edge on shortest s->v path
    self._distTo[s] = 0.0

    # visit vertices in toplogical order
    topological = Topological(G)
    if not topological.hasOrder():
      raise Exception("Digraph is not acyclic.")
    for v in topological.order():
      for e in G.adj(v):
        self.relax(e)

  def _relax(self, e):
    """Relax an edge e from v to w"""
    v, w = e.get_from_to()
    if self._distTo[w] > (self._distTo[v] + e.weight()):
       self._distTo[w] =  self._distTo[v] + e.weight() # New shorter dist
       self._edgeTo[w] = e # Set better way to get to w

  def distTo(self, v): # O(K)
    """Returns the length of a shortest path from the source vertex s to vertex v."""
    return self._distTo[v]

  def hasPathTo(self, v): # O(K)
    """Is there a path from the source vertex s to vertex v?"""
    return self._distTo[v] < self.Inf

  def pathTo(self, v): # O(E in shortest path)
    """Returns a shortest path from the source vertex s to vertex v."""
    if not self.hasPathTo(v): return None
    path = [] # new Stack<DirectedEdge>()
    e = self._edgeTo[v] 
    while e is not None: 
      path.append(e) # push(e)
      e = self._edgeTo[e.get_from()]
    return path

# Shortest Paths APIs (10:51)
#
# QUESTION: Which version of the shortest path problem does the SP API represent?
#     Single-source and single-sink: find the shortest path from s to t
#  -> Single-source: find the shortest paths from s to every vertex
#     Single-sink: find the shortest paths from every vertex to t
#     All-pairs: find the shortest paths between every ordered pair of vertices.
# EXPLANATION: The API requires the algorithm to compute the shortest path 
# from s to every other vertex.
# The single-source single-sink problem is a special case. If you reverse the
# digraph, you can solve the single-sink version of the problem (by interchanging
# the roles of s and t). The all-pairs problem is a generalization where you solve
# the single-source version of the problem for every vertex.

# Shortest Path Properties (14:46)
# 
# SHORTEST-PATHS OPTIMALITY CONDITIONS
# To prove shortest paths are found, prove S-P OPT. COND. hold
#
# QUESTION: Let e = v->w be an edge with weight 17.0. Suppose that during the 
# generic shortest paths algorithm, distTo[v] = Inf and distTo[w] = 15.0. 
# What will distTo[w] be after calling relax(e)?
# ANSWER: 15
# EXPLANATION: If distTo[v] is Inf, then relaxing any edge pointing from v
# will have no effect since in Java (and IEEE floating point), Inf + x = Inf
# unless x is -Inf or Nan.

# QUESTION: The topological sort algorithm computes the shortest-paths tree in 
# an edge-weighted DAG in time proportional to ...
# ANSWER: E + V
# EXPLANATION: It process the V vertices in topological order;
# It relaxes each of teh E edges exactly once.

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
