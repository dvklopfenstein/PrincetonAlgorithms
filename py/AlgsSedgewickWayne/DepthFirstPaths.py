"""Computes a path between source vertex, s, and every other vertex in undirected graph G."""

from AlgsSedgewickWayne.Stack import Stack

class DepthFirstPaths(object):
  """This implementation uses depth-first search."""

  def __init__(self, G, s):
    self.s = s # source vertex
    self.edgeTo = [None for i in range(G.V())]     # edgeTo[v] = last edge on s-v path
    self.marked = [False for i in range(G.V())] # marked[v] = is there an s-v path?
    self._dfs(G, s)

  def _dfs(self, G, v):
    """depth first search from v"""
    self.marked[v] = True
    for w in G.adj(v):
      if not self.marked[w]:
        self.edgeTo[w] = v
        self._dfs(G, w)

  def hasPathTo(self, v):
    """Is there a path between the source vertex s and vertex v?"""
    return self.marked[v]

  def pathTo(self, v):
    """Returns a path between the source vertex s and vertex v, or None"""
    if not self.hasPathTo(v): return None
    path = Stack()
    x = v
    while x != self.s:
      path.push(x)
      x = self.edgeTo[x]
    path.push(self.s)
    return path # seq of vertices on path between vertices, s and v


# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation
