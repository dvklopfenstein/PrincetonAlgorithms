"""Compute connected components using depth first search."""

class CC(object):
  """Computes the connected components of the undirected graph G. Runs in O(E + V) time."""

  def __init__(self, G):
    self._marked = [False]*G.V() # marked[v] = has vertex v been marked?
    self._id = [0]*G.V()   # id[v] = id of connected component containing v
    self._size = [0]*G.V() # size[id] = number of vertices in given component
    self._count = 0        # number of connected components
    for v in range(G.V()):
      if not self._marked[v]:
        self._dfs(G, v)
        self._count += 1

  def _dfs(self, G, v):
    """depth-first search"""
    self._marked[v] = True
    self._id[v] = self._count
    self._size[self._count] += 1
    for w in G.adj(v):
      if not self._marked[w]:
        self._dfs(G, w)

  # Returns the component id of the connected component containing vertex <tt>v</tt>.
  def id(self, v): return self._id[v] 

  # Returns the number of vertices in the connected component containing vertex <tt>v</tt>.
  def size(self, v): return self._size[id[v]]

  # Returns the number of connected components in the graph <tt>G</tt>.
  def count(self): return self._count

  # Returns true if vertices <tt>v</tt> and <tt>w</tt> are in the same
  def connected(self, v, w): return self._id(v) == self._id(w)

  # Returns true if vertices v and w are in the same connected component.
  def areConnected(self, v, w): return self._id(v) == self._id(w)

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation
