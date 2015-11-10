"""A graph, implemented using an array of lists. Parallel edges and self-loops are permitted."""

class Digraph(object):
  
  def __init__(self, a):
    if isinstance(a, int):
      self._init_empty(a)
    elif len(a) == 1:
      self._init_empty(a[0])
    else:
      self._init(a)

  def _init_empty(self, V):
    if V < 0: raise Exception("Number of vertices in a Digraph must be nonnegative")
    self._V = V # number of vertices in self digraph
    self._E = 0 # number of edges in self digraph
    self._indegree = [0]*V # indegree[v] = indegree of vertex v
    self._adj = [set() for v in range(V)] # adj[v] = adjacency list for vertex v

  def _init(self, a):
    """Initializes a graph from an input stream."""
    # The format is the number of vertices V, followed by the number of edges E,
    # followed by E pairs of vertices, with each entry separated by whitespace.
    self._init_empty(a[0]) # init V, and the empty adj list
    self._E = a[1]
    if self._E < 0: raise Exception("Number of edges must be nonnegative")
    for v, w in a[2:]:
      self.addEdge(v, w)

  def V(self): return self._V # Returns the number of vertices in self digraph.
  def E(self): return self._E # Returns the number of edges in self digraph.

  def _validateVertex(self, v):
    """raise an IndexOutOfBoundsException unless 0 <= v < V"""
    if v < 0 or v >= self._V:
      raise Exception("vertex {} is not between 0 and {}".format(v, V-1))

  def addEdge(self, v, w):
    """Adds the directed edge v->w to self digraph."""
    self._validateVertex(v)
    self._validateVertex(w)
    self._adj[v].add(w)
    self._indegree[w] += 1
    self._E += 1

  def adj(self, v):
    """Returns the vertices adjacent from vertex v in self digraph."""
    self._validateVertex(v)
    return self._adj[v]

  def outdegree(self, v):
    """Returns the number of directed edges incident from vertex v."""
    self._validateVertex(v)
    return self._adj[v].size()

  def indegree(self, v):
    """Returns the number of directed edges incident to vertex v."""
    self._validateVertex(v)
    return self.indegree[v]

  def reverse(self):
    """Returns the reverse of the digraph."""
    R = Digraph(self._V)
    for v in range(self._V):
      for w in self._adj(v):
        R.addEdge(w, v)
    return R

  def __str__(self):
    s = ["{V} vertices, {E} edges \n".format(V=self._V, E=self._E)]
    for v in range(self._V):
      s.append("{}: ".format(v))
      for w in self._adj[v]:
        s.append("{} ".format(w))
      s.append("\n")
    return ''.join(s)

 #  % java Digraph tinyDG.txt
 #  13 vertices, 22 edges
 #  0: 5 1 
 #  1: 
 #  2: 0 3 
 #  3: 5 2 
 #  4: 3 2 
 #  5: 4 
 #  6: 9 4 8 0 
 #  7: 6 9
 #  8: 6 
 #  9: 11 10 
 #  10: 12 
 #  11: 4 12 
 #  12: 9 

# ------------------------------------------------------------------
# INTRODUCTION TO DIGRAPHS (8:30)

# SOME DIGRAPH PROBLEMS 07:30
#
# PATH: Is there a directed path from s to t?
# SHORTEST PATH: What is the shortest directed path from s to t?
# TOPOLOGICAL SORT: Can you draw a digraph so that all edges so that all edges point upwards?
# STRONG CONNECTIVITY: Is there a directed path between all pairs of vertices?
# TRANSITIVE CLOSURE: For which vertices v and w is there a path from v to w?
# PAGERANK: What is the importance of a web page?
#
# QUESTION: How many different digraphs are there on V vertices?
# Allow self-loops but do not allow parallel edges.
# ANSWER: 2^(V^2)
# EXPLANATION: There are V^2 possible edges. Each edge is either in 
# the digrpah or not.

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2015, DV Klopfenstein, Python implementation
