"""Compute a minimum spanning forest(for each connected comp) or tree(if 1 CC) using Kruskal's algorithm."""

from AlgsSedgewickWayne.QuickUnionUF import QuickUnionUF
from AlgsSedgewickWayne.MST_check import _check
from heapq import heappush, heappop
import sys

class KruskalMST(object):
  """Compute a minimum spanning tree (or forest) of an edge-weighted graph."""

  FLOATING_POINT_EPSILON = 1E-12

  def __init__(self, G): # t ~ O(E log E), s ~ V
    self._weight = 0.0 # weight of MST. Edge weights can be +, 0, or -, need not be distinct.
    self._mst = [] # new Queue<Edge>();  # edges in MST
    # more efficient to build heap by passing array of edges
    pq = [] # new MinPQ<Edge>()
    for item in [(e.weight(), e) for e in G.edges()]:
      heappush(pq, item) # insert(e)

    # run greedy algorithm
    uf = QuickUnionUF(G.V())
    while not pq and len(self._mst) < (G.V() - 1):
      edge_cur = heappop(pq) # .delMin()
      v, w = edge_cur.get_vw()
      if not uf.connected(v, w): # v-w does not create a cycle
        uf.union(v, w)  # merge v and w components
        self._mst.append(edge_cur) # enqueue(e);  # add edge e to mst
        self._weight += edge_cur.weight()

    #assert self._check(G) # check optimality conditions

  # Returns the edges in a minimum spanning tree (or forest).
  def edges(self): return self._mst # t ~ V

  # Returns the sum of the edge weights in a minimum spanning tree (or forest).
  def weight(self): return self._weight # t ~ K

# INTRODUCTION TO MSTS (4:04)

# MST IS FUNDAMENTAL PROBLEM WITH DIVERSE APPLICATIONS 3:33
#  * Dithering (removing the fuzziness in images)
#  * Cluster Analysis
#  * Max bottleneck paths
#  * Real-time face verification
#  * LDPC codes for error correction
#  * Image registration with Renyl entropy
#  * Find road networks in satellite and aerial imagery
#  * Reducing data storage in sequencing amino acids in a protein.
#  * Model locality of particle interactions in turbulent fluid flows.
#  * Autoconfig protocol for Ethernet bridging to avoid cycles in a network.
#  * Approximation algorithms for NP-hard problems (eg, TSP, Steiner tree)
#  * Network design (communication, electrical, hydraulic, computer, road)
  
# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
