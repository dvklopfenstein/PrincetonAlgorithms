"""Data type for determining the vertices reachable from a given src vertex(s)."""

class DirectedDFS(object):

  def __init__(self, G, s): # O ~ V + E (wc)
    if isinstance(s, int):
      self._init(G, [s])
    else:
      self._init(G, s)

  def _init(self, G, sources):
    """Computes vertices in digraph G that are connected to any src vertices, sources"""
    self.marked = [False for _ in range(G.V())] # True if v is reachable from src (or srcs)
    self._count = 0 # number of vertices reachable from s
    for v in sources:
      if not self.marked[v]: self._dfs(G, v)

  def _dfs(self, G, v): 
    self._count += 1
    self.marked[v] = True
    for w in G.adj(v):
      if not self.marked[w]: self._dfs(G, w)

  # Directed path from source vertex (or any of the source vertices) and vertex v?
  def marked(self, v): return self.marked[v]

  #Returns the number of vertices reachable from the source vertex
  def count(self): return self._count

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

