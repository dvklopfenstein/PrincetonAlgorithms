"""An edge-weighted digraph, implemented using adjacency lists."""

#*****************************************************************************
 #  Compilation:  javac EdgeWeightedDigraph.java
 #  Execution:    java EdgeWeightedDigraph V E
 #  Dependencies: Bag.java DirectedEdge.java
 #
 #
 #*****************************************************************************/
 #  The <tt>EdgeWeightedDigraph</tt> class represents a edge-weighted
 #  digraph of vertices named 0 through <em>V</em> - 1, where each
 #  directed edge is of type {@link DirectedEdge} and has a real-valued weight.
 #  It supports the following two primary operations: add a directed edge
 #  to the digraph and iterate over all of edges incident from a given vertex.
 #  It also provides
 #  methods for returning the number of vertices <em>V</em> and the number
 #  of edges <em>E</em>. Parallel edges and self-loops are permitted.
 #  <p>
 #  This implementation uses an adjacency-lists representation, which 
 #  is a vertex-indexed array of @link{Bag} objects.
 #  All operations take constant time (in the worst case) except
 #  iterating over the edges incident from a given vertex, which takes
 #  time proportional to the number of such edges.
class EdgeWeightedDigraph(object):
  
  def __init__(self, V):
    if V < 0: raise Exception("Number of vertices in a Digraph must be nonnegative")
    self._V = V # number of vertices in self digraph
    self._E = 0 # number of edges in self digraph
    self._indegree = new int[V] # adj[v] = adjacency list for vertex v
    self._adj = [set() for for v in range(V)] # indegree[v] = indegree of vertex v

    #*
     # Initializes a random edge-weighted digraph with <tt>V</tt> vertices and <em>E</em> edges.
     #
     # @param  V the number of vertices
     # @param  E the number of edges
     # @throws IllegalArgumentException if <tt>V</tt> < 0
     # @throws IllegalArgumentException if <tt>E</tt> < 0
     #/
  public EdgeWeightedDigraph(int V, E):
      self(V)
      if E < 0) raise new IllegalArgumentException("Number of edges in a Digraph must be nonnegative")
      for (int i = 0; i < E; i += 1):
          v = StdRandom.uniform(V)
          w = StdRandom.uniform(V)
          double weight = .01 * StdRandom.uniform(100)
          DirectedEdge e = new DirectedEdge(v, w, weight)
          addEdge(e)

    #*  
     # Initializes an edge-weighted digraph from the specified input stream.
     # The format is the number of vertices <em>V</em>,
     # followed by the number of edges <em>E</em>,
     # followed by <em>E</em> pairs of vertices and edge weights,
     # with each entry separated by whitespace.
     #
     # @param  in the input stream
     # @throws IndexOutOfBoundsException if the endpoints of any edge are not in prescribed range
     # @throws IllegalArgumentException if the number of vertices or edges is negative
     #/
  public EdgeWeightedDigraph(In in):
      self(in.readInt())
      E = in.readInt()
      if E < 0) raise new IllegalArgumentException("Number of edges must be nonnegative")
      for (int i = 0; i < E; i += 1):
          v = in.readInt()
          w = in.readInt()
          if v < 0 or v >= V) raise new IndexOutOfBoundsException("vertex " + v + " is not between 0 and " + (V-1))
          if w < 0 or w >= V) raise new IndexOutOfBoundsException("vertex " + w + " is not between 0 and " + (V-1))
          double weight = in.readDouble()
          addEdge(new DirectedEdge(v, w, weight))

    #*
     # Initializes a new edge-weighted digraph that is a deep copy of <tt>G</tt>.
     #
     # @param  G the edge-weighted digraph to copy
     #/
  public EdgeWeightedDigraph(EdgeWeightedDigraph G):
      self(G.V())
      self.E = G.E()
      for (int v = 0; v < G.V(); v += 1)
          self.indegree[v] = G.indegree(v)
      for (int v = 0; v < G.V(); v += 1):
          # reverse so that adjacency list is in same order as original
          Stack<DirectedEdge> reverse = new Stack<DirectedEdge>()
          for (DirectedEdge e : G.adj[v]):
              reverse.push(e)
          for (DirectedEdge e : reverse):
              adj[v].add(e)

  # number of vertices in this edge-weighted digraph.
  def V(self): return self._V

  # number of edges in this edge-weighted digraph.
  def E(self): return self._E

  # raise an IndexOutOfBoundsException unless 0 <= v < V
  def _validateVertex(self, v):
    if v < 0 or v >= self._V:
      raise Exception("vertex {} is not between 0 and {}".format(v, V-1))

  def addEdge(self, e):
    """Adds the directed edge <tt>e</tt> to this edge-weighted digraph."""
    v = e.from()
    w = e.to()
    validateVertex(v)
    validateVertex(w)
    adj[v].add(e)
    E += 1


    #*
     # Returns the directed edges incident from vertex <tt>v</tt>.
     #
     # @param  v the vertex
     # @return the directed edges incident from vertex <tt>v</tt> as an Iterable
     # @throws IndexOutOfBoundsException unless 0 <= v < V
     #/
  def adj(int v):
      validateVertex(v)
      return adj[v]

    #*
     # Returns the number of directed edges incident from vertex <tt>v</tt>.
     # This is known as the <em>outdegree</em> of vertex <tt>v</tt>.
     #
     # @param  v the vertex
     # @return the outdegree of vertex <tt>v</tt>
     # @throws IndexOutOfBoundsException unless 0 <= v < V
     #/
  def outdegree(int v):
      validateVertex(v)
      return adj[v].size()

    #*
     # Returns the number of directed edges incident to vertex <tt>v</tt>.
     # This is known as the <em>indegree</em> of vertex <tt>v</tt>.
     #
     # @param  v the vertex
     # @return the indegree of vertex <tt>v</tt>
     # @throws IndexOutOfBoundsException unless 0 <= v < V
     #/
  def indegree(int v):
      validateVertex(v)
      return indegree[v]

    #*
     # Returns all directed edges in this edge-weighted digraph.
     # To iterate over the edges in this edge-weighted digraph, use foreach notation:
     # <tt>for (DirectedEdge e : G.edges())</tt>.
     #
     # @return all edges in this edge-weighted digraph, as an iterable
     #/
  def edges():
      Bag<DirectedEdge> list = new Bag<DirectedEdge>()
      for (int v = 0; v < V; v += 1):
          for (DirectedEdge e : adj(v)):
              list.add(e)
      return list

  def __str__(self):
    StringBuilder s = new StringBuilder()
    s = ["{V} {E}\n".format(V=self._V, E=self._E)]
    for v in range(V):
      s.append("{v}: ".format(v=v))
      for e in self._adj[v]:
        s.append("{e} ".format(e=e))
      s.append("\n")
    return "".join(s)

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
