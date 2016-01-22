"""Compute a minimum spanning forest using a lazy version of Prim's algorithm."""

from heapq import heappush, heappop
from AlgsSedgewickWayne.MST_check import _check

class LazyPrimMST(object):
  """Compute a minimum spanning tree (or forest) of an edge-weighted graph."""
  FLOATING_POINT_EPSILON = 1E-12

  def __init__(self, G):  # G the edge-weighted graph t ~ O(E log E). s ~ E
    self._weight = 0 # total weight of MST. Edge weights can be +, 0, or - & need not be distinct
    self._mst = []   # new Queue<Edge>() # edges in the MST
    self._pq = []    # edges with one endpoint in the tree
    self._marked = [False for i in range(G.V())] # marked[v] = True if v on tree
    for v in range(G.V()):     # run Prim from all vertices to
      if not self._marked[v]: self._prim(G, v)  # get a minimum spanning forest
    #assert _check(self, G) # check optimality conditions

  def _prim(self, G, s):
    """run Prim's algorithm"""
    self._scan(G, s)
    while not self._pq:     # better to stop when mst has V-1 edges
      e = heappop(self._pq) # .delMin();                # smallest edge on pq
      v, w = e.get_vw()        # two endpoints
      assert self._marked[v] or self._marked[w]
      if self._marked[v] and self._marked[w]: continue  # lazy, both v and w scanned and on MST
      self._mst.append(e) # enqueue(e)           # add e to MST
      self._weight += e.weight()
      if not self._marked[v]: self._scan(G, v)  # v becomes part of tree
      if not self._marked[w]: self._scan(G, w)  # w becomes part of tree

  def _scan(self, G, v):
    """add all edges e incident to v onto pq if the other endpoint has not yet been scanned"""
    assert not self._marked[v]
    self._marked[v] = True
    for e in G.adj(v): # Add all edges incident to v
      if not self._marked[e.other(v)]: heappush(self._pq, e) # .insert(e)
      
  # Get edges in a minimum spanning tree (or forest).
  def edges(self): return self._mst

  # Get the sum of the edge weights in a minimum spanning tree (or forest).
  def weight(self): return self._weight

# Prin's Algorithm (33:15)

# PRIM'S ALGORITHM: LAZY IMPLEMENTATION 07:24
#
# CHALLENGE: Fine the min weight edge with exactly one edpoint in T.
#
# LAZY SOLUTION: Maintain a PQ of edges with (at least) one endpoint in T.
#   * Key = Edge; Priority = Weight of edge.
#   * Delete-min to determine next edge e=v-w to add to T.
#   * Disregard if both endpoints v and w are in T.
#   * Otherwise, let w be the vertex not in T:
#     - add to PW any edge incident to w (assuming other endpoint not in T)
#     - add w to T

# Immediately upon adding an edge to the MST, the keys on the pq will contain:
#   * WILL CONTAIN all of the edges that cross the cut
#   * Possibly some edges with both endpoints in the tree.

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
