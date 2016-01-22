"""Compute a minimum spanning forest using Prim's algorithm."""

 #  Dependencies: EdgeWeightedGraph.java Edge.java Queue.java
 #                IndexMinPQ.java UF.java In.java StdOut.java

#*
 #  The <tt>PrimMST</tt> class represents a data type for computing a
 #  <em>minimum spanning tree</em> in an edge-weighted graph.
 #  The edge weights can be positive, zero, or negative and need not
 #  be distinct. If the graph is not connected, it computes a <em>minimum
 #  spanning forest</em>, which is the union of minimum spanning trees
 #  in each connected component. The <tt>weight()</tt> method returns the 
 #  weight of a minimum spanning tree and the <tt>edges()</tt> method
 #  returns its edges.
 #  <p>
 #  This implementation uses <em>Prim's algorithm</em> with an indexed
 #  binary heap.
 #  The constructor takes time proportional to <em>E</em> log <em>V</em>
 #  and extra space (not including the graph) proportional to <em>V</em>,
 #  where <em>V</em> is the number of vertices and <em>E</em> is the number of edges.
 #  Afterwards, the <tt>weight()</tt> method takes constant time
 #  and the <tt>edges()</tt> method takes time proportional to <em>V</em>.
 #  <p>
 #  For additional documentation,
 #  see <a href="http://algs4.cs.princeton.edu/43mst">Section 4.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #  For alternate implementations, see {@link LazyPrimMST}, {@link KruskalMST},
 #  and {@link BoruvkaMST}.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
class PrimMST(object):
  """Compute a minimum spanning tree (or forest) of an edge-weighted graph."""
  FLOATING_POINT_EPSILON = 1E-12

  def __init__(self, G): # G is an edge-weighted graph
      self._edgeTo = new Edge[G.V()] # edgeTo[v] = shortest edge from tree vertex to non-tree vertex
      self._distTo = new double[G.V()] # distTo[v] = weight of shortest such edge
      self._marked = [False for i in range(G.V())] # marked[v] = True if v on tree, False otherwise
      self._pq = IndexMinPQ(G.V())
      for v in range(G.V()):
        self._distTo[v] = float('Inf')

      for v in range(G.V()):              # run from each vertex to find
        if not self._marked[v]: self._prim(G, v)      # minimum spanning forest

      # check optimality conditions
      assert _check(G)

  def _prim(self, G, s):
    """run Prim's algorithm in graph G, starting from vertex s"""
    self._distTo[s] = 0.0
    pq.insert(s, self._distTo[s])
    while pq:
      v = pq.delMin()
      self._scan(G, v)

  def _scan(self, G, v):
    """scan vertex v"""
    self._marked[v] = True
    for e in G.adj(v):
      w = e.other(v)
      if self._marked[w]: continue;         # v-w is obsolete edge
      if e.weight() < distTo[w]:
        self._distTo[w] = e.weight()
        self._edgeTo[w] = e
        if pq.contains(w): pq.decrease(w, distTo[w])
        else               pq.insert(w, distTo[w])

  def edges(self):
    """Returns the edges in a minimum spanning tree (or forest)."""
    mst = [] # new Queue<Edge>()
    for v in len(self._edgeTo):
      e = self._edgeTo[v]
      if e is not None:
          mst.append(e) # .enqueue(e)
    return mst

  def weight(self):
    """Returns the sum of the edge weights in a minimum spanning tree (or forest)."""
    weight = 0.0
    for e in self.edges():
      weight += e.weight()
    return weight


  # check optimality conditions (takes time proportional to E V lg* V)
  def _check(EdgeWeightedGraph G):

      # check weight
      double totalWeight = 0.0
      for (Edge e : edges()):
          totalWeight += e.weight()
      if Math.abs(totalWeight - weight()) > FLOATING_POINT_EPSILON):
          System.err.printf("Weight of edges does not equal weight(): %f vs. %f\n", totalWeight, weight())
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
          for (Edge f : edges()):
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

# PRIM'S ALGORITHM (33:15)

# PRIM'S ALGORITHM EAGER IMPLEMENTATION 20:01
#
# CHALLENGE: Find min weight edge with exactly one endpoint in T.
#
# EAGER SOLUTION: Maintain a PQ of **vertices** connected by an edge to T,
# where priority of vertex v = weight of shortest edge connecting v to T.
#  * Delete min vertex v and add its associated edge e = v-w to T.
#  * Update PQ by considering all edges e = v-x incident to v
#    - ignore if x is already in T
#    - add x to PQ if not already on it
#    - decrease priority of x if v-x becomes shortest edge connecting x to T

# EXPLANATION: For each non-tree vertex v, the eadter version of Prim's algorithm
# maintains at most one entry in the priority queue (with key equal to the 
# weight og the cheapet edge from v to the tree 20:15

# QUESTION: What is the order of growth of the worst-case running time of
# Prim's algorithm using a binary heap?
# ANSWER: E log V

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port.
