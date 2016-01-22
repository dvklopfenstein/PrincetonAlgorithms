"""Computes a path between source vertex, s, and every other vertex in undirected graph G."""

class DepthFirstDirectedPaths(object):
  """This implementation uses depth-first search."""

  def __init__(self, G, s):
    self.s = s # source vertex
    self.edgeTo = [None for i in range(G.V())] # edgeTo[v] = last edge on s-v path
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
    path = [] # Stack()
    x = v
    while x != self.s:
      path.append(x) # push(x)
      x = self.edgeTo[x]
    path.append(self.s) # push(self.s)
    return path # seq of vertices on path between vertices, s and v

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

# QUESTION: Suppose that during an execution of depth-first search in a digraph G,
# dfs(v) is called after dfs(w) is called but before dfs(w) returns. Which 
# of the following must be true of graph G?
# ANSWER: There exists a directed path from w to v.
# EXPLANATION: The function call stack bwtween when w and v are called contains a 
# directed path from w to v.

# QUESTION from Topological Sort (12:54): 
# Let G be a directed acyclic graph (DAG) containing an edge v->w.
# Suppose that dfs(v) is called during an execution of depth-first search.
# Which one of the following is impossible?
#     dfs(w) has not yet been called.
#     dfs(w) will be the next recursive call after dfs(v)
# --> dfs(w) has already been called but not yet returned
#     dfs(w) has already been called and returned
# EXPLANATION: If dfs(v) is called before dfs(w) returns, then the function
# call-stack contains a directed path from w to v (as in the previous in-video
# quiz). Combining this path with the edge v->w yeilds a directed cycle, which 
# is impossible since G is acylic.

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation
