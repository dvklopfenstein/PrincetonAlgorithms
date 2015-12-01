"""Compute connected components using depth first search."""

import collections as cx

class CC(object):
  """Computes the connected components of the undirected graph G in constant time."""

  def __init__(self, G): #  O(E + V)
    self._marked = cx.OrderedDict((v, False) for v in G.keys)
    self._id = cx.OrderedDict((v, None) for v in G.keys)
    self._count = 0        # number of connected components
    self._size = [0]*G.V() # size[id] = number of vertices in given component
    for v in G.keys:
      if not self._marked[v]:
        self._dfs(G, v)
        self._count += 1

  def _dfs(self, G, v):
    """depth-first search"""
    self._marked[v] = True    # marked[v] = has vertex v been marked?
    self._id[v] = self._count # id[v] = id of connected component containing v
    self._size[self._count] += 1
    for w in G.adj(v):
      if not self._marked[w]:
        self._dfs(G, w)

  # Returns the component id of the connected component containing vertex v.
  def id(self, v): return self._id[v] 

  # Returns the number of vertices in the connected component containing vertex v.
  def size(self, v): return self._size[id[v]]

  # Returns the number of connected components in the graph G.
  def count(self): return self._count

  # Returns true if vertices v and w are in the same connected component.
  def connected(self, v, w): return self._id(v) == self._id(w)

  def prt_ids(self, prt):
    """Print Vertex names on line 1 and vertex component ids on line 2."""
    prt.write("id[v] = {}\n".format(' '.join(self._id.keys())))
    prt.write("id[v] = {}\n".format(' '.join(str(i) for i in self._id.values())))

#------------------------------------------------------------------------------
# CONNECTED COMPONENTS (18:56)

# UNION-FIND? No. Could not quite answer question "Is v and w connected" in constant time.

# CONNECTED COMPONENTS: 3:28
# The relation "is connected to" is an equivalence relation:
#  * Reflexive: v is connected to v
#  * Symmetric: if v is connected to w, the w is connected to v
#  * Transitive: if v connected to w and w connected to x, then connected to x.

# CONNECTED COMPONENTS APPLICATION: PARTICLE DETECTION
#
# PARTICLE DETECTION: Given grayscale image of particles, identify "blobs."
#   * Vertex: pixel
#   * Edge: between two adjacent pixels with grayscale value >= 70 (blk=0, wht=255)
#   * Blob: connected component of 20-30 pixels
#
# PARTICLE TRACKING: Trackmoving particles over time.

#------------------------------------------------------------------------------
# GRAPH CHALLENGES (14:29)

# HOW DIFFICULT?
#   * Any programmer could do it
#   * Typical diligent algorithms student could do it.
#   * Hire an expert
#   * Intractable
#   * No one knows
#   * Impossible

# GRAPH-PROCESSING CHALLENGE 1
# 
# PROBLEM: Is a graph bipartite?
# BIPARTITE: You can divide the vertices into two subsets with the property
#   that every edge connects a vertex in one subset to a vertex in another.
# ANSWER: Can use DFS to tell if a graph is bipartite.

# GRAPH-PROCESSING CHALLENGE 2
#
# PROBLEM: Find a cycle in a Graph.
# ANSWER: Simple with DFS (see textbook)

# BRIDGES OF KONIGSBERG
# The Seven Bridges of Konigsberg [Leonhard Euler 1736]
# Exactly cross 7 bridges exactly once
# EULER TOUR: Is there a (general) cycle that uses each edge exactly once?
# ANSWER: A connected graph is Eulerian iff all vertices have even degree.

# GRAPH-PROCESSING CHALLENGE 3
#
# PROBLEM: Find a (general) cycle that uses every edge exactly once. (Eularian Cycle)

# GRAPH-PROCESSING CHALLENGE 4
#
# PROBLEM: Find a (general) cycle that uses every vertex exactly once. 
# AKA: Traveling Sales Person Problem; Hamiltonian Cycle
# INTRACTABLE: NP-complete. Nobody knows an efficient solution for large graphs

# GRAPH-PROCESSING CHALLENGE 5
#
# PROBLEM: Are two graphs identical except for vertex names?
# AKA: Graph isomorphism problem
# NO ONE KNOWS. Don;t even know how to classify the problem

# GRAPH-PROCESSING CHALLENGE 6
#
# PROBLEM: Lay out a grpah in the plane without crossing edges?
# HIRE AN EXPERT: linear time DFS-based planarity algorithm discovered by
#   Tarjan in 1970s (too complicated for most practitioners)

# QUESTION: Which one of the following graph-processing problems is 
# unlikely to have an algorithm whose running time is E + V?
#    * determine whether a graph is bipartite
#    * determine whether a graph has a Euler cycle
# -> * determine whether a graph has a Hamilton cycle
#    * determine whether a graph can be drawn in the plane such that no 2 edges cross
# EXPLANATION: The Hamilton cycle problem is NP-complete -- it is unlikely 
# to have a polynomial-time algorithm. The other 3 problems can be solved in linear time.


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation
