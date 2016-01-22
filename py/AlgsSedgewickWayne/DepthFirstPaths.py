"""Computes a path between source vertex, s, and every other vertex in undirected graph G."""

import collections as cx

class DepthFirstPaths(object):
  """This implementation uses depth-first search."""

  def __init__(self, G, s, prt=None):
    self.s = s # source vertex
    self.edgeTo = cx.OrderedDict([(v, None)  for v in G.keys]) # edgeTo[v] = last edge on s-v path
    self.marked = cx.OrderedDict([(v, False) for v in G.keys]) # marked[v] = is there an s-v path?
    self.prt = prt
    self._dfs(G, s)

  def _dfs(self, G, v):
    """depth first search from v"""
    self._set_mark(v, G)
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
    path = [] # Stack()
    x = v
    while x != self.s:
      path.append(x) # push(x)
      x = self.edgeTo[x]
    path.append(self.s) # push(self.s)
    return path # seq of vertices on path between vertices, s and v

  def _set_mark(self, v, G):
    """Set mark and print which mark was set, if desired."""
    self.marked[v] = True 
    if self.prt is not None: 
      self.prt.write("{} ".format(v))

# DEPTH-FIRST SEARCH PROPERTIES
#
# PROPOSITION: DFS marks all vertices connected to s in time proportional to 
# the sum of their degrees.
# 
# PROPOSITION: After DFS, can find vertices connected to s in constant time
# and can find a path to s (if one exists) in time proportional to its length.

# QUESTION: In a Graph G represented using the adjacency-lists representation,
# depth-first search marks all vertices connected to s in time proportional to
# ANSWER: The sum of the degrees of the vertices in the connected component
# containing s

# QUESTION: The critical data structures used in depth-first search and
# breadth-first search are _____ and ____, respectively.
# ANSWER: DFS->Stack BFS->Queue
# EXPLANATION: With DFS, it is either an explicit stack(w/ nonrecursive version)
# or the function-call stack (w/a recursive version)

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation
