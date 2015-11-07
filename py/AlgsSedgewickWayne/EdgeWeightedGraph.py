"""An edge-weighted undirected graph, implemented using adjacency lists."""
# Parallel edges and self-loops are permitted.
# TBD FINISH PYTHON PORT

class EdgeWeightedGraph(object):

  def __init__(self, V, E=None):
    self._init_V(V)
    if E is not None:
      self._init_VE(V, E)

  def _init_V(self, V):
    if V < 0: raise Exception("Number of vertices must be nonnegative")
    self._V = V
    self._E = 0
    self._adj = [set() for v in range(V)]

  def _init_VE(self, V, E):
    if E < 0: raise Exception("Number of edges must be nonnegative")
    for i in range(E):
      v = StdRandom.uniform(V)
      w = StdRandom.uniform(V)
      weight = Math.round(100 * StdRandom.uniform()) / 100.0
      e = Edge(v, w, weight)
      self.addEdge(e)

  public EdgeWeightedGraph(In in):
      self(in.readInt())
      E = in.readInt()
      if E < 0) raise new IllegalArgumentException("Number of edges must be nonnegative")
      for (int i = 0; i < E; i += 1):
          v = in.readInt()
          w = in.readInt()
          double weight = in.readDouble()
          Edge e = new Edge(v, w, weight)
          addEdge(e)

  def _init_G(self, G):
    self._init_V(G.V())
    self._E in G.
    for v in range(G.V()):
      # reverse so that adjacency list is in same order as original
      Stack<Edge> reverse = new Stack<Edge>()
      for e in G.adj[v]:
        reverse.push(e)
      for e in reverse:
        adj[v].add(e)


  def V(self): return self._V #number of vertices in this edge-weighted graph.
  def E(self): return self._E # number of edges in this edge-weighted graph.

  def _validateVertex(self, v):
    """raise an IndexOutOfBoundsException unless 0 <= v < V"""
    if v < 0 or v >= self._V)
      raise Exception("vertex {} is not between 0 and {}".format(v, (V-1))

  def addEdge(self, e):
    """Adds the undirected edge <tt>e</tt> to this edge-weighted graph."""
    v = e.either()
    w = e.other(v)
    self._validateVertex(v)
    self._validateVertex(w)
    self._adj[v].add(e)
    self._adj[w].add(e)
    self._E += 1

  def adj(self, v):
    """Returns the edges incident on vertex v."""
    self._validateVertex(v)
    return self._adj[v]

  def degree(int v):
    """Returns the degree of vertex v."""
    self._validateVertex(v)
    return self._adj[v].size()

  def edges(self):
    """Returns all edges in this edge-weighted graph."""
    bag = set()
    for v in range(self._V):
      selfLoops = 0
      for e in self._adj(v):
        if e.other(v) > self._v:
          bag.add(e)
        # only add one copy of each self loop (self loops will be consecutive)
        elif e.other(v) == self._v:
          if selfLoops % 2 == 0: bag.add(e)
          selfLoops += 1
    return bag

  def __str__(self):
    s = ["{} {}\n".format(self._V, self._E)]
    for v in range(self._V):
      s.append("{}: ".format(v))
      for e in self._adj[v]:
        s.append("{}  ".format(e))
      s.append("\n")
    return ''.join(s)

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
