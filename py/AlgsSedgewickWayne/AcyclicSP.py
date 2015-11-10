"""Solve single-source shortest paths problem in edge-weighted DAG"""
# TBD: Finish Python port

class AcyclicSP(object):
  """Computes a shortest paths tree from s to every other vertex in the DAG G."""
  Inf = float('Inf')
  private double[] distTo;         # distTo[v] = distance  of shortest s->v path
  private DirectedEdge[] edgeTo;   # edgeTo[v] = last edge on shortest s->v path

  def __init__(self, G, s): # G=DAG, v=source vertex O(V+E)
    self._distTo = [0.0 for i in range(G.V())]
    self._edgeTo = new DirectedEdge[G.V()]
    for v in range(G.V()):
      self._distTo[v] = self.Inf
    self._distTo[s] = 0.0

    # visit vertices in toplogical order
    topological = Topological(G)
    if not topological.hasOrder():
      raise Exception("Digraph is not acyclic.")
    for v in topological.order():
      for e in G.adj(v):
        self.relax(e)

  def _relax(self, e):
    """relax edge e"""
    v, w = e.get_from_to()
    if self._distTo[w] > (self._distTo[v] + e.weight()):
       self._distTo[w] =  self._distTo[v] + e.weight()
       self._edgeTo[w] = e

  def self.distTo(self, v): # O(K)
    """Returns the length of a shortest path from the source vertex s to vertex v."""
    return self._distTo[v]

  def hasPathTo(self, v): # O(K)
    """Is there a path from the source vertex s to vertex v?"""
    return self._distTo[v] < self.Inf

  def pathTo(self, v): # O(E in shortest path)
    """Returns a shortest path from the source vertex s to vertex v."""
    if not hasPathTo(v): return None
    path = [] # new Stack<DirectedEdge>()
    for e = self._edgeTo[v]; e is not None; e = self._edgeTo[e.from()]):
      path.push(e)
    return path

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
