"""Dijkstra's algorithm. Computes the shortest path tree. Assumes all weights are nonnegative."""

class DijkstraSP(object):
  """Get shortest-paths tree from src vertex s to every other vertex in the edge-weighted DAG G."""
  private IndexMinPQ<Double> pq;    # priority queue of vertices

  Inf = float('Inf')

  def __init__(self, G, s): # EdgeWeightedDigraph O(E lof V)
    for e in G.edges():
      if e.weight() < 0:
        raise Exception("edge {} has negative weight".format(e))

    self._distTo = [self.Inf for i in range(G.V())] # distTo[v] = distance  of shortest s->v path
    self._edgeTo = [None for i in range(G.V())]     # edgeTo[v] = last edge on shortest s->v path
    self._distTo[s] = 0.0

    # relax vertices in order of distance from s
    pq = new IndexMinPQ<Double>(G.V())
    pq.insert(s, distTo[s])
    while (!pq.isEmpty()):
      v = pq.delMin()
      for e in G.adj(v):
        self._relax(e)

    # check optimality conditions
    assert _check(G, s)

  def _relax(self, e):
    """relax edge e and update pq if changed"""
    v, w = e.get_from_to()
    if self._distTo[w] > (self._distTo[v] + e.weight()):
       self._distTo[w] =  self._distTo[v] + e.weight()
       self._edgeTo[w] = e
       if pq.contains(w): pq.decreaseKey(w, self._distTo[w])
       else               pq.insert(w, self._distTo[w])

  def distTo(self, v): # O(k)
    """Returns the length of a shortest path from the source vertex s to vertex v."""
    return self._distTo[v]

  def hasPathTo(self, v): # O(k)
    """Returns true if there is a path from the source vertex s to vertex v."""
    return self._distTo[v] < self.Inf

  def pathTo(self, v):
    """Returns a shortest path from the source vertex s to vertex v."""
    if not hasPathTo(v): return None
    path = [] # new Stack<DirectedEdge>()
    e = edgeTo[v]
    while e is not None: 
      path.append(e) # push(e)
      e = self.edgeTo[e.from()]
    return path


  # check optimality conditions:
  # (i) for all edges e:            distTo[e.to()] <= distTo[e.from()] + e.weight()
  # (ii) for all edge e on the SPT: distTo[e.to()] == distTo[e.from()] + e.weight()
  def _check(EdgeWeightedDigraph G, s):

      # check that edge weights are nonnegative
      for (DirectedEdge e : G.edges()):
          if e.weight() < 0):
              System.err.println("negative edge weight detected")
              return False

      # check that distTo[v] and edgeTo[v] are consistent
      if distTo[s] != 0.0 or edgeTo[s] is not None):
          System.err.println("distTo[s] and edgeTo[s] inconsistent")
          return False
      for (int v = 0; v < G.V(); v += 1):
          if v == s) continue
          if edgeTo[v] is None and distTo[v] != Double.POSITIVE_INFINITY):
              System.err.println("distTo[] and edgeTo[] inconsistent")
              return False

      # check that all edges e = v->w satisfy distTo[w] <= distTo[v] + e.weight()
      for (int v = 0; v < G.V(); v += 1):
          for (DirectedEdge e : G.adj(v)):
              w = e.to()
              if distTo[v] + e.weight() < distTo[w]):
                  System.err.println("edge " + e + " not relaxed")
                  return False

      # check that all edges e = v->w on SPT satisfy distTo[w] == distTo[v] + e.weight()
      for (int w = 0; w < G.V(); w += 1):
          if edgeTo[w] is None) continue
          DirectedEdge e = edgeTo[w]
          v = e.from()
          if w != e.to()) return False
          if distTo[v] + e.weight() != distTo[w]):
              System.err.println("edge " + e + " on shortest path not tight")
              return False
      return True

# Dijkstra's Algorithm (18:58)
#
# PQ implementation insert    delete-min decrease-key total
# ----------------- ------    ---------- ------------ -----
# unordered array      1           V          1         V^2
# binary heap        log V       log V      log V     E log V
# d-way heap       d log_d V   d log_d V   log_d V   E log_E/V V
# Fibonacci heap       1         log V        1      E + V log V
#
# BOTTOM LINE:
#   * Array implementation optiomal for dense graphs
#   * Binary heap faster for sparse graphs.
#   * 4-way heap wort the trouble in preformance-critical situations
#   * Fibonacci heap best in theory, but not worht implementing.

# QUESTION: What is the order of growth of the running time of Dijkstra's 
# algorithm using a binary heap: Assume that all vertices are reachable 
# from the source.
# ANSWER: E log V
# EXPLANATION: The bottleneck is the hap operations. There are at most
# V insert, V delete-min, and E decrease-key operations. Each operation
# is logarithmic in the size of the binary heap, which is at most V.

# DIJKSTRA'S Algorithm is GREEDY (so cannot do negative edges)





# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
