"""A undirected graph, implemented using an array of sets. Parallel edges and self-loops allowed."""

import sys

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
    self._V = V
    self._E = 0
    self._adj = [set() for v in range(V)]

  def _init(self, a):
    """Initializes a graph from an input stream."""
    # The format is the number of vertices V, followed by the number of edges E,
    # followed by E pairs of vertices, with each entry separated by whitespace.
    self._init_empty(a[0]) # init V, and the empty adj list
    E = a[1]
    if E < 0: raise Exception("Number of edges must be nonnegative")
    for v, w in a[2:]:
      self.addEdge(v, w)

  def V(self): return self._V # Returns the number of vertices in self graph.
  def E(self): return self._E # Returns the number of edges in self graph.

  def addEdge(self, v, w):
    """Adds the undirected edge v-w to self graph."""
    self._validateVertex(v)
    self._validateVertex(w)
    self._E += 1
    self._adj[v].add(w)
    self._adj[w].add(v)

  def adj(self, v):
    """Returns the vertices adjacent to vertex v."""
    self._validateVertex(v)
    return self._adj[v]

  def degree(self, v):
    """Returns the degree of vertex v."""
    self._validateVertex(v)
    return self._adj[v].size()

  def _validateVertex(self, v):
    """raise an IndexOutOfBoundsException unless 0 <= v < V."""
    if v < 0 or v >= self._V:
        raise Exception("vertex {} is not between 0 and {}".format(v, self._V-1))

  def __str__(self):
    s = [(("{V} vertices, {E} edges\n").format(V=self._V, E=self._E))]
    for v in range(self._V):
      s.append("{v}: ".format(v=v))
      for w in self._adj[v]:
        s.append("{w} ".format(w=w))
      s.append("\n")
    return ''.join(s)

  def __iter__(self): # Makes Graph an iterable.
    return iter(self._adj) # returns an iterator.

  def wr_png(self, fout_png="Graph.png", prt=sys.stdout, **kwargs):
    """Make a png showing a diagram of the connected components."""
    import pydot
    from AlgsSedgewickWayne.testcode.utils import get_png_label
    # 1. Create/initialize Graph
    G = pydot.Dot(graph_type='graph') # Undirected Graph
    # 2. Create Nodes
    nodes = [pydot.Node(str(idx)) for idx in range(len(self._adj))]
    # 3. Add nodes to Graph
    for node in nodes:
      G.add_node(node)
    # 4. Add Edges between Nodes to Graph
    for v, w in self.get_edges():
      if v != w: # Print only edges from one node to another (not to self)
        G.add_edge(pydot.Edge(v, w))
    # 5. Write Graph to png file
    G.write_png(fout_png)
    prt.write("  WROTE: {}\n".format(fout_png))

  def get_edges(self):
    edges = set()
    for v, ws in enumerate(self._adj):
      for w in ws:
        edges.add(tuple(sorted([v, w]))) 
    return edges

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

# -----------------------------------------------------------------------------
# INTRODUCTION TO GRAPHS (9:32)


# SOME GRAPH-PROCESSING PROBLEMS 08:14
#
# PATH: Is there a path between s and t?
# SHORTEST PATH: What is the shortest path between s and t?
#
# CYCLE: Is there a cycle in the graph?
# EULER TOUR: Is there a cycle that uses each edge exactly once?
# HAMILTON TOUR: Is there a cycle that uses each vertex exactly once?
#
# CONNECTIVITY: Is there a awy to connect all of the vertices?
# MST: What is the best way to connect all of the vertices?
# BICONNECTIVITY: Is there a vertex whose removeal disconnects the graph?
#
# PLANARITY: Can you draw the graph in the plane with no crossing edges?
# GRAPH ISOMORPHISM: Do two adjacency lists represent the same graph?
# 
# CHALLENGE: Whinc of these problems are easy? difficult? intractable?



# QUESTION: A cycle that uses eachedge of a graph exactly once is called
# ANSWER: An Euler tour

#  Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
#  Copyright 2015-2016, DV Klopfenstein, Python implementation
