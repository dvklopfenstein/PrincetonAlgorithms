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
public class PrimMST:
  private static final double FLOATING_POINT_EPSILON = 1E-12

  private Edge[] edgeTo;        # edgeTo[v] = shortest edge from tree vertex to non-tree vertex
  private double[] distTo;      # distTo[v] = weight of shortest such edge
  private boolean[] marked;     # marked[v] = True if v on tree, False otherwise
  private IndexMinPQ<Double> pq

    #*
     # Compute a minimum spanning tree (or forest) of an edge-weighted graph.
     # @param G the edge-weighted graph
     #/
  public PrimMST(EdgeWeightedGraph G):
      edgeTo = new Edge[G.V()]
      distTo = new double[G.V()]
      marked = new boolean[G.V()]
      pq = new IndexMinPQ<Double>(G.V())
      for (int v = 0; v < G.V(); v += 1)
          distTo[v] = Double.POSITIVE_INFINITY

      for (int v = 0; v < G.V(); v += 1)      # run from each vertex to find
          if !marked[v]) prim(G, v);      # minimum spanning forest

      # check optimality conditions
      assert check(G)

  # run Prim's algorithm in graph G, starting from vertex s
  def _prim(EdgeWeightedGraph G, s):
      distTo[s] = 0.0
      pq.insert(s, distTo[s])
      while (!pq.isEmpty()):
          v = pq.delMin()
          scan(G, v)

  # scan vertex v
  def _scan(EdgeWeightedGraph G, v):
      marked[v] = True
      for (Edge e : G.adj(v)):
          w = e.other(v)
          if marked[w]) continue;         # v-w is obsolete edge
          if e.weight() < distTo[w]):
              distTo[w] = e.weight()
              edgeTo[w] = e
              if pq.contains(w)) pq.decrease(w, distTo[w])
              else                pq.insert(w, distTo[w])

    #*
     # Returns the edges in a minimum spanning tree (or forest).
     # @return the edges in a minimum spanning tree (or forest) as
     #    an iterable of edges
     #/
  def edges():
      Queue<Edge> mst = new Queue<Edge>()
      for (int v = 0; v < len(edgeTo); v += 1):
          Edge e = edgeTo[v]
          if e is not None):
              mst.enqueue(e)
      return mst

    #*
     # Returns the sum of the edge weights in a minimum spanning tree (or forest).
     # @return the sum of the edge weights in a minimum spanning tree (or forest)
     #/
  def weight():
      double weight = 0.0
      for (Edge e : edges())
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

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port.
