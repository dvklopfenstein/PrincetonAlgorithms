"""A undirected graph, implemented using an array of sets. Parallel edges and self-loops allowed."""

from AlgsSedgewickWayne.Bag import Bag

class Graph(object):

  def __init__(self, a):
    if isinstance(a, int):
      self._init_empty(a)
    elif len(a) == 1:
      self._init_empty(a[0])
    else:
      self._init(a)

  def _init_empty(self, V):
    if V < 0: raise Exception("Number of vertices must be nonnegative")
    self.V = V
    self.E = 0
    self.adj = [Bag() for v in range(V)]

  def _init(self, a):
    """Initializes a graph from an input stream."""
    # The format is the number of vertices V, followed by the number of edges E,
    # followed by E pairs of vertices, with each entry separated by whitespace.
    self._init_empty(a[0]) # init V, and the empty adj list
    E = a[1]
    if E < 0: raise Exception("Number of edges must be nonnegative")
    for v, w in a[2:]:
      self.addEdge(v, w)

  def V(self): return self.V # Returns the number of vertices in self graph.
  def E(self): return self.E # Returns the number of edges in self graph.

  def addEdge(self, v, w):
    """Adds the undirected edge v-w to self graph."""
    self._validateVertex(v)
    self._validateVertex(w)
    self.E += 1
    self.adj[v].add(w)
    self.adj[w].add(v)

  def adj(self, v):
    """Returns the vertices adjacent to vertex v."""
    self._validateVertex(v)
    return self.adj[v]

  def degree(self, v):
    """Returns the degree of vertex v."""
    self._validateVertex(v)
    return self.adj[v].size()

  def _validateVertex(self, v):
    """raise an IndexOutOfBoundsException unless 0 <= v < V."""
    if v < 0 or v >= self.V:
        raise Exception("vertex {} is not between 0 and {}".format(v, self.V-1))

  def __str__(self):
    s = [(("{V} vertices, {E} edges\n").format(V=self.V, E=self.E))]
    for v in range(self.V):
      s.append("{v}: ".format(v=v))
      for w in self.adj[v]:
        s.append("{w} ".format(w=w))
      s.append("\n")
    return ''.join(s)


 #*****************************************************************************/
 #  % Graph.py ../thirdparty/tinyG.txt
 #  13 vertices, 13 edges 
 #  0: 6 2 1 5 
 #  1: 0 
 #  2: 0 
 #  3: 5 4 
 #  4: 5 6 3 
 #  5: 3 4 0 
 #  6: 0 4 
 #  7: 8 
 #  8: 7 
 #  9: 11 10 12 
 #  10: 9 
 #  11: 9 12 
 #  12: 11 9 
 #  
 #*****************************************************************************/

#  Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
#  Copyright 2015-2016, DV Klopfenstein, Python implementation
