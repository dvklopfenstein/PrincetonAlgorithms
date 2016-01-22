"""An edge-weighted digraph, implemented using adjacency lists."""
# TBD: Finish Python port

from AlgsSedgewickWayne.DirectedEdge import DirectedEdge
import random

class EdgeWeightedDigraph(object):
  
  def __init__(self, V, E=None):
    if isinstance(V, int):
      self._init_VE(V, E)
    else:
      self._init_arr(V)

  def _init_V(self, V):
    if V < 0: raise Exception("Number of vertices in a Digraph must be nonnegative")
    self._V = V # number of vertices in self digraph
    self._E = 0 # number of edges in self digraph
    self._indegree = new int[V] # adj[v] = adjacency list for vertex v
    self._adj = [set() for for v in range(V)] # indegree[v] = indegree of vertex v

  def _init_VE(self, V, E):
    """Initializes a random edge-weighted digraph with V vertices and E edges."""
    self._init_V(V)
    if E is not None:
      if E < 0: raise Exception("Number of edges in a Digraph must be nonnegative")
      for i in E:
        v = random.randint(0, V) # get random int in [0, V)
        w = random.randint(0, V)
        weight = .01 * random.uniform(100)
        e = DirectedEdge(v, w, weight)
        self.addEdge(e)

  def _init_arr(arr):
    """Initializes a random edge-weighted digraph with V vertices and E edges."""
    self._init_V(arr[0])
    self._E = arr[1]
    if E < 0: raise Exception("Number of edges must be nonnegative")
    for v, w, weight in a[2:]:
      if v < 0 or v >= self._V: raise Exception("vertex {} is not between 0 and {}".format(v, (V-1)))
      if w < 0 or w >= self._V: raise Exception("vertex {} is not between 0 and {}".format(w, (V-1)))
      self.addEdge(DirectedEdge(v, w, weight))

  def __copy__(self, G):
    """Initializes a new edge-weighted digraph that is a deep copy of G."""
    self._init_V(G.V())
    self._E = G.E()
    for v in range(G.V()):
      self._indegree[v] = G.indegree(v)
    for v in range(G.V()):
      # reverse so that adjacency list is in same order as original
      reverse = [] # new Stack<DirectedEdge>()
      for e in G._adj[v]:
        reverse.push(e)
      for e in reverse:
        self._adj[v].add(e)

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
    v = e.get_from()
    w = e.get_to()
    self._validateVertex(v)
    self._validateVertex(w)
    self._adj[v].add(e)
    self._E += 1

  def adj(self, v):
    """Returns the directed edges incident from vertex v."""
    self._validateVertex(v)
    return self._adj[v]

  def outdegree(self, v):
    """Returns the number of directed edges incident from vertex v."""
    self._validateVertex(v)
    return self._adj[v].size()

  def indegree(self, v):
    """Returns the number of directed edges incident to vertex v."""
    self._validateVertex(v)
    return self._indegree[v]

  def edges(self):
    """Returns all directed edges in this edge-weighted digraph."""
    lst = set()
    for v in range(V):
      for e in self._adj(v):
        lst.add(e)
    return lst

  def __str__(self):
    s = ["{V} {E}\n".format(V=self._V, E=self._E)]
    for v in range(V):
      s.append("{v}: ".format(v=v))
      for e in self._adj[v]:
        s.append("{e} ".format(e=e))
      s.append("\n")
    return "".join(s)

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
