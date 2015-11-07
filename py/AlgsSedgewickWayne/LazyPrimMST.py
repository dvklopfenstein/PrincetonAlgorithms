"""Compute a minimum spanning forest using a lazy version of Prim's algorithm."""
#*
 #  The <tt>LazyPrimMST</tt> class represents a data type for computing a
 #  <em>minimum spanning tree</em> in an edge-weighted graph.
 #  The edge weights can be positive, zero, or negative and need not
 #  be distinct. If the graph is not connected, it computes a <em>minimum
 #  spanning forest</em>, which is the union of minimum spanning trees
 #  in each connected component. The <tt>weight()</tt> method returns the 
 #  weight of a minimum spanning tree and the <tt>edges()</tt> method
 #  returns its edges.
 #  <p>
 #  This implementation uses a lazy version of <em>Prim's algorithm</em>
 #  with a binary heap of edges.
 #  The constructor takes time proportional to <em>E</em> log <em>E</em>
 #  and extra space (not including the graph) proportional to <em>E</em>,
 #  where <em>V</em> is the number of vertices and <em>E</em> is the number of edges.
 #  Afterwards, the <tt>weight()</tt> method takes constant time
 #  and the <tt>edges()</tt> method takes time proportional to <em>V</em>.
 #  <p>
 #  For additional documentation,
 #  see <a href="http://algs4.cs.princeton.edu/43mst">Section 4.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #  For alternate implementations, see {@link PrimMST}, {@link KruskalMST},
 #  and {@link BoruvkaMST}.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
public class LazyPrimMST:
  private static final double FLOATING_POINT_EPSILON = 1E-12

  private double weight;       # total weight of MST
  private Queue<Edge> mst;     # edges in the MST
  private boolean[] marked;    # marked[v] = True if v on tree
  private MinPQ<Edge> pq;      # edges with one endpoint in tree

    #*
     # Compute a minimum spanning tree (or forest) of an edge-weighted graph.
     # @param G the edge-weighted graph
     #/
  def __init__(G):
      self._mst = new Queue<Edge>()
      self._pq = new MinPQ<Edge>()
      self._marked = new boolean[G.V()]
      for v in range(G.V()):     # run Prim from all vertices to
        if not self._marked[v]: self._prim(G, v)  # get a minimum spanning forest

      # check optimality conditions
      assert self._check(G)

  # run Prim's algorithm
  def _prim(EdgeWeightedGraph G, s):
      scan(G, s)
      while (!pq.isEmpty()):                        # better to stop when mst has V-1 edges
          Edge e = pq.delMin();                      # smallest edge on pq
          v = e.either(), w = e.other(v);        # two endpoints
          assert marked[v] or marked[w]
          if marked[v] and marked[w]) continue;      # lazy, both v and w already scanned
          mst.enqueue(e);                            # add e to MST
          weight += e.weight()
          if !marked[v]) scan(G, v);               # v becomes part of tree
          if !marked[w]) scan(G, w);               # w becomes part of tree

  # add all edges e incident to v onto pq if the other endpoint has not yet been scanned
  def _scan(EdgeWeightedGraph G, v):
      assert !marked[v]
      marked[v] = True
      for (Edge e : G.adj(v))
          if !marked[e.other(v)]) pq.insert(e)
      
  # Returns the edges in a minimum spanning tree (or forest).
  def edges(self): return self._mst

  # Returns the sum of the edge weights in a minimum spanning tree (or forest).
  def weight(self): return self._weight

  # check optimality conditions (takes time proportional to E V lg* V)
  def _check(self, G):

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
