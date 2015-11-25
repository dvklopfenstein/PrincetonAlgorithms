"""find shortest paths from a source vertex s to every other vertex in an undirected graph."""

from collections import deque
import sys
import collections as cx

class BreadthFirstPaths(object):
  """Run breadth first search on an undirected graph."""
  Inf = float("inf")

  def __init__(self, G, s, prt=None):
    self._marked = cx.OrderedDict([(v, False)    for v in G.keys]) # marked[v] = is there an s-v path
    self._edgeTo = cx.OrderedDict([(v, self.Inf) for v in G.keys]) # edgeTo[v] = last edge on s-v path
    self._distTo = cx.OrderedDict([(v, self.Inf) for v in G.keys]) # distTo[v] = number of edges shortest s-v path
    self._bfs(G, s, prt)
    assert self._check(G, s)

  def _bfs(self, G, sources, prt):
    """breadth-first search from multiple sources."""
    q = deque() # Queue
    if isinstance(sources, int):
      sources = [sources]
    for s in sources:
      self._marked[s] = True
      self._distTo[s] = 0
      q.append(s) # enqueue
    while q:
      v = self.deque(q, prt)
      for w in G.adj(v):
        if not self._marked[w]:
          self._edgeTo[w] = v
          self._distTo[w] = self._distTo[v] + 1
          self._marked[w] = True
          q.append(w) # enqueue(w)

  def hasPathTo(self, v): return self._marked[v]
  def distTo(self, v): return self._distTo[v]

  def pathTo(self, v):
    """Returns a shortest path between the source vertex s (or sources) or None"""
    if not self.hasPathTo(v): return None
    path = [] # Stack
    x = v
    while self._distTo[x] != 0:
      path.append(x) # push
      x = self._edgeTo[x]
    path.append(x) # push
    return path

  def deque(self, q, prt):
    """Deque and print dequed value if user requests."""
    v = q.popleft() # dequeue()
    if prt is not None:
      prt.write("{} ".format(v))
    return v

  def _check(self, G, s, prt=sys.stdout):
    """check optimality conditions for single source."""

    # check that the distance of s = 0
    if self._distTo[s] != 0:
      prt.write("distance of source {} to itself = {}\n".format(s, self._distTo[s]))
      return False

    # check that for each edge v-w dist[w] <= dist[v] + 1
    # provided v is reachable from s
    for v in G.keys:
      for w in G.adj(v):
        if self.hasPathTo(v) != self.hasPathTo(w):
          prt.write("edge {}-{}".format(v, w))
          prt.write("hasPathTo({}) = {}".format(v, self.hasPathTo(v)))
          prt.write("hasPathTo({}) = {}".format(w, self.hasPathTo(w)))
          return False
        if self.hasPathTo(v) and (self._distTo[w] > self._distTo[v] + 1):
          prt.write("edge {}-{}".format(v, w))
          prt.write("distTo[{}] = {}".format(v, self._distTo[v]))
          prt.write("distTo[{}] = {}".format(w, self._distTo[w]))
          return False

    # check that v = edgeTo[w] satisfies distTo[w] + distTo[v] + 1
    # provided v is reachable from s
    for w in G.keys:
      if not self.hasPathTo(w) or w == s: continue
      v = self._edgeTo[w]
      if self._distTo[w] != self._distTo[v] + 1:
        prt.write("shortest path edge {}-{}".format(v, w))
        prt.write("distTo[{}] = ".format(v, self._distTo[v]))
        prt.write("distTo[{}] = ".format(w, self._distTo[w]))
        return False

    return True

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
