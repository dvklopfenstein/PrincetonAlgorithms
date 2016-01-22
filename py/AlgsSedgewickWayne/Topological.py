"""Compute topological ordering(w DFS) of a DAG or edge-weighted DAG. Runs in O(E + V) time."""
# TBD Finish Python port


from AlgsSedgewickWayne.DirectedCycle import DirectedCycle
from AlgsSedgewickWayne.DepthFirstOrder import DepthFirstOrder
from AlgsSedgewickWayne.EdgeWeightedDigraph import EdgeWeightedDigraph
from AlgsSedgewickWayne.EdgeWeightedDirectedCycle import EdgeWeightedDirectedCycle

class Topological(object):
  """Determines if digraph G has a topological order and, if so, finds topological order."""

  def __init__(self, G): # G is Digraph O(V+E) wc
    finder = DirectedCycle(G)
    if not finder.hasCycle():
      dfs = DepthFirstOrder(G)
      self._order = dfs.reversePost() # topological order
      self._rank = [] # rank[v] = position of vertex v in topological order
      i = 0
      for v in self. order:
        self._rank[v] = i 
        i += 1

  def Topological(EdgeWeightedDigraph G): # EdgeWeightedDigraph
    """Determines if digraph G has a topological order and, if so, finds topological order."""
    EdgeWeightedDirectedCycle finder = new EdgeWeightedDirectedCycle(G)
    if not finder.hasCycle():
      dfs = DepthFirstOrder(G)
      order = dfs.reversePost()

  # Returns a topological order if the digraph has a topologial order, None otherwise
  def order(self): return self._order # O(V)

  # Does the digraph have a topological order?
  def hasOrder(self): return self._order is not None # O(k)

  def rank(self, v): # O(k)
    """The the rank of vertex v in the topological order; -1 if the digraph is not a DAG."""
    self._validateVertex(v)
    if self.hasOrder(): return self._rank[v]
    else:               return -1

  def _validateVertex(self, v):
    """raise an IndexOutOfBoundsException unless 0 <= v < V."""
    V = len(self._rank)
    if v < 0 or v >= V:
      raise Exception("vertex {} is not between 0 and {}".format(v, (V-1))

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2002-2016, DV Klopfenstein, Python port
