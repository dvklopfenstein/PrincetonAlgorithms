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

from heapq import heappush, heappop
import collections as cx

class KruskalMST(object):
  """Compute a minimum spanning tree (or forest) of an edge-weighted graph."""

  FLOATING_POINT_EPSILON = 1E-12

  def __init__(self, G):
    self._weight = 0.0     # weight of MST
    self._mst = cx.deque() # new Queue<Edge>();  # edges in MST
    # more efficient to build heap by passing array of edges
    pq = [] # new MinPQ<Edge>()
    data = [(e.weight(), e) for e in G.edges()]
    for item in data:
      heappush(pq, item) # insert(e)

    # run greedy algorithm
    uf = new UF(G.V())
    while not pq and len(self._mst) < (G.V() - 1):
      e = heappop(pq) # .delMin()
      v = e.either()
      w = e.other(v)
      if !uf.connected(v, w)): # v-w does not create a cycle
        uf.union(v, w);  # merge v and w components
        self._mst.append(e) # enqueue(e);  # add edge e to mst
        self._weight += e.weight()

    assert self._check(G) # check optimality conditions

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
    if Math.abs(total - self.weight()) > FLOATING_POINT_EPSILON):
        System.err.printf("Weight of edges does not equal weight(): %f vs. %f\n", total, weight())
        return False

    # check that it is acyclic
    UF uf = new UF(G.V())
    for (Edge e : edges()):
        v = e.either(), w = e.other(v)
        if uf.connected(v, w)):
            System.err.println("Not a forest")
            return False
        uf.union(v, w)

    # check that it is a spanning forest
    for (Edge e : G.edges()):
        v = e.either(), w = e.other(v)
        if !uf.connected(v, w)):
            System.err.println("Not a spanning forest")
            return False

    # check that it is a minimal spanning forest (cut optimality conditions)
    for (Edge e : edges()):

        # all edges in MST except e
        uf = new UF(G.V())
        for (Edge f : mst):
            x = f.either(), y = f.other(x)
            if f != e) uf.union(x, y)
        
        # check that e is min weight edge in crossing cut
        for (Edge f : G.edges()):
            x = f.either(), y = f.other(x)
            if !uf.connected(x, y)):
                if f.weight() < e.weight()):
                    System.err.println("Edge " + f + " violates cut optimality conditions")
                    return False


      return True

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
