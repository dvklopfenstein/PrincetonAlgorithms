"""An edge-weighted undirected graph, implemented using adjacency lists."""

from AlgsSedgewickWayne.Edge import Edge
import random
                                                  
class EdgeWeightedGraph(object):
  """Undirected weighter graph. Parallel edges and self-loops are permitted."""
                                                  
  def __init__(self, V, E=None):                  
    if isinstance(V, int):
      self._init_int(V, E)
    else:
      self._init_arr(V)

  def _init_V(self, V):
    """Graph with V vertices and no Edges."""
    if V < 0: raise Exception("Number of vertices must be nonnegative")
    self._V = V
    self._E = 0
    self._adj = [set() for v in range(V)]

  def _init_int(self, V, E):
    """Graph with V vertices, randomly connected w/random weights."""
    self._init_V(V)
    if E < 0: raise Exception("Number of edges must be nonnegative")
    for i in range(E):
      v = random.randint(0, V) # get random int in [0, V)
      w = random.randint(0, V)
      weight = round(100 * random.uniform()) / 100.0
      e = Edge(v, w, weight)
      self.addEdge(e)

  def _init_arr(self, arr):
    self._init_V(arr[0])
    self._E = arr[1]
    if self._E < 0: raise Exception("Number of edges must be nonnegative")
    for E in arr[2:]:
      v = E[0]
      w = E[1]
      weight = E[2]
      e = Edge(v, w, weight)
      self.addEdge(e)

  def __copy__(self, G):
    self._init_V(G.V())
    self._E in G.E()
    for v in range(G.V()):
      # reverse so that adjacency list is in same order as original
      reverse = [] # Stack<Edge>()
      for e in G._adj[v]:
        reverse.append(e) # push(e)
      for e in reverse:
        self._adj[v].add(e)

  def V(self): return self._V #number of vertices in this edge-weighted graph.
  def E(self): return self._E # number of edges in this edge-weighted graph.

  def _validateVertex(self, v):
    """raise an IndexOutOfBoundsException unless 0 <= v < V"""
    if v < 0 or v >= self._V:
      raise Exception("vertex {} is not between 0 and {}".format(v, (self._V-1)))

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

  def degree(self, v):
    """Returns the degree of vertex v."""
    self._validateVertex(v)
    return self._adj[v].size()

  def edges(self):
    """Returns all edges in this edge-weighted graph."""
    bag = set()
    for v in range(self._V):
      selfLoops = 0
      for e in self._adj[v]:
        if e.other(v) > v:
          bag.add(e)
        # only add one copy of each self loop (self loops will be consecutive)
        elif e.other(v) == v:
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

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
