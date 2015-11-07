"""Compute a minimum spanning forest using Kruskal's algorithm."""

#*
 #  The <tt>KruskalMST</tt> class represents a data type for computing a
 #  <em>minimum spanning tree</em> in an edge-weighted graph.
 #  The edge weights can be positive, zero, or negative and need not
 #  be distinct. If the graph is not connected, it computes a <em>minimum
 #  spanning forest</em>, which is the union of minimum spanning trees
 #  in each connected component. The <tt>weight()</tt> method returns the 
 #  weight of a minimum spanning tree and the <tt>edges()</tt> method
 #  returns its edges.
 #  <p>
 #  This implementation uses <em>Krusal's algorithm</em> and the
 #  union-find data type.
 #  The constructor takes time proportional to <em>E</em> log <em>E</em>
 #  and extra space (not including the graph) proportional to <em>V</em>,
 #  where <em>V</em> is the number of vertices and <em>E</em> is the number of edges.
 #  Afterwards, the <tt>weight()</tt> method takes constant time
 #  and the <tt>edges()</tt> method takes time proportional to <em>V</em>.
 #  <p>
 #  For additional documentation,
 #  see <a href="http://algs4.cs.princeton.edu/43mst">Section 4.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #  For alternate implementations, see {@link LazyPrimMST}, {@link PrimMST},
 #  and {@link BoruvkaMST}.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

from AlgsSedgewickWayne.QuickUnionUF import QuickUnionUF
from heapq import heappush, heappop
import sys

class KruskalMST(object):
  """Compute a minimum spanning tree (or forest) of an edge-weighted graph."""

  FLOATING_POINT_EPSILON = 1E-12

  def __init__(self, G):
    self._weight = 0.0     # weight of MST
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
  def edges(self): return self._mst

  # Returns the sum of the edge weights in a minimum spanning tree (or forest).
  def weight(self): return self._weight
  
  # check optimality conditions (takes time proportional to E V lg* V)
  def _check(self, G):

    # check total weight
    total = 0.0
    for e in self.edges():
      total += e.weight()
    if abs(total - self.weight()) > self.FLOATING_POINT_EPSILON:
      sys.stderr.write("Weight of edges does not equal weight(): {} vs. {}\n".format(
        total, weight()))
      return False

    # check that it is acyclic
    uf = QuickUnionUF(G.V())
    for e in self.edges():
      v, w = e.get_vw() 
      if uf.connected(v, w):
        sys.stderr.write("Not a forest\n")
        return False
      uf.union(v, w)

    # check that it is a spanning forest
    for e in G.edges():
      v, w = e.get_vw() 
      if not uf.connected(v, w):
        sys.stderr.write("Not a spanning forest\n")
        return False

    # check that it is a minimal spanning forest (cut optimality conditions)
    for e in edges():
      # all edges in MST except e
      uf = QuickUnionUF(G.V())
      for f in self._mst:
        v, w = e.get_vw() 
        if f != e: uf.union(x, y)
      
      # check that e is min weight edge in crossing cut
      for f in G.edges():
        x, y = f.get_vw() 
        if not uf.connected(x, y):
          if f.weight() < e.weight():
            sys.stderr.write("Edge {} violates cut optimality conditions\n".format(f))
            return False
      return True

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
