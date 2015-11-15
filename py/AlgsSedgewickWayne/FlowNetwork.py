"""A capacitated flow network, implemented using adjacency lists."""
# TBD Finish Python port

 #  The <tt>FlowNetwork</tt> class represents a capacitated network
 #  with vertices named 0 through <em>V</em> - 1, where each directed
 #  edge is of type {@link FlowEdge} and has a real-valued capacity
 #  and flow.
 #  It supports the following two primary operations: add an edge to the network,
 #  iterate over all of the edges incident to or from a vertex. It also provides
 #  methods for returning the number of vertices <em>V</em> and the number
 #  of edges <em>E</em>. Parallel edges and self-loops are permitted.
 #  <p>
 #  This implementation uses an adjacency-lists representation, which 
 #  is a vertex-indexed array of @link{Bag} objects.
 #  All operations take constant time (in the worst case) except
 #  iterating over the edges incident to a given vertex, which takes
 #  time proportional to the number of such edges.
class FlowNetwork(object):
  private static final String NEWLINE = System.getProperty("line.separator")

  private final V
  private E
  private Bag<FlowEdge>[] adj
  
     # Initializes an empty flow network with <tt>V</tt> vertices and 0 edges.
     # param V the number of vertices
  public FlowNetwork(int V):
      if V < 0) raise new IllegalArgumentException("Number of vertices in a Graph must be nonnegative")
      self.V = V
      self.E = 0
      adj = (Bag<FlowEdge>[]) new Bag[V]
      for (int v = 0; v < V; v += 1)
          adj[v] = new Bag<FlowEdge>()

     # Initializes a random flow network with <tt>V</tt> vertices and <em>E</em> edges.
     # The capacities are integers between 0 and 99 and the flow values are zero.
     # param V the number of vertices
     # param E the number of edges
  public FlowNetwork(int V, E):
      self(V)
      if E < 0) raise new IllegalArgumentException("Number of edges must be nonnegative")
      for (int i = 0; i < E; i += 1):
          v = StdRandom.uniform(V)
          w = StdRandom.uniform(V)
          double capacity = StdRandom.uniform(100)
          addEdge(new FlowEdge(v, w, capacity))

     # Initializes a flow network from an input stream.
     # The format is the number of vertices <em>V</em>,
     # followed by the number of edges <em>E</em>,
     # followed by <em>E</em> pairs of vertices and edge capacities,
     # with each entry separated by whitespace.
     # @param in the input stream
  public FlowNetwork(In in):
      self(in.readInt())
      E = in.readInt()
      if E < 0) raise new IllegalArgumentException("Number of edges must be nonnegative")
      for (int i = 0; i < E; i += 1):
          v = in.readInt()
          w = in.readInt()
          if v < 0 or v >= V) raise new IndexOutOfBoundsException("vertex " + v + " is not between 0 and " + (V-1))
          if w < 0 or w >= V) raise new IndexOutOfBoundsException("vertex " + w + " is not between 0 and " + (V-1))
          double capacity = in.readDouble()
          addEdge(new FlowEdge(v, w, capacity))


  def V(self): return self._V # Returns the number of vertices in the edge-weighted graph.
  def E(self): return self._E # Returns the number of edges in the edge-weighted graph.

  def _validateVertex(self, v):
    """raise an IndexOutOfBoundsException unless 0 <= v < V"""
    if v < 0 or v >= self._V:
      raise Exception("vertex {} is not between 0 and {}".format(v, (V-1)))

  def addEdge(self, e):
    """Adds the edge e to the network."""
    v = e.get_from()
    w = e.get_to()
    self._validateVertex(v)
    self._validateVertex(w)
    self._adj[v].add(e)
    self._adj[w].add(e)
    self._E += 1

  def adj(self, v):
    """Returns the edges incident on vertex v (includes both edges pointing to and from v."""
    self._validateVertex(v)
    return self._adj[v]

  def edges(self):
    """return list of all edges - excludes self loops"""
    bag = set()
    for v in range(V):
      for e in self._adj(v):
        if e.get_to() != v:
          bag.add(e)
    return bag


  def __str__(self):
    s = ["{} {}\n".format(self._V, self_E)]
    for v in range(self._V):
      s.append("{}:  ".format(v))
      for e in self._adj[v]:
        if e.get_to() != v: s.append("{}  ".format(e))
      s.append("\n")
    return ''.join(s)

    #*
     # Unit tests the <tt>FlowNetwork</tt> data type.
     #/
  def main(String[] args):
      In in = new In(args[0])
      FlowNetwork G = new FlowNetwork(in)
      prt.write(G)

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
