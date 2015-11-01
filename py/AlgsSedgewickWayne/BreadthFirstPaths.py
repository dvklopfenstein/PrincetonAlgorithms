"""find shortest paths from a source vertex s to every other vertex in an undirected graph."""
 #  Runs in O(E + V) time.
 #
 #  %  java Graph tinyCG.txt
 #  6 8
 #  0: 2 1 5 
 #  1: 0 2 
 #  2: 0 1 3 4 
 #  3: 5 4 2 
 #  4: 3 2 
 #  5: 3 0 
 #
 #  %  java BreadthFirstPaths tinyCG.txt 0
 #  0 to 0 (0):  0
 #  0 to 1 (1):  0-1
 #  0 to 2 (1):  0-2
 #  0 to 3 (2):  0-2-3
 #  0 to 4 (2):  0-2-4
 #  0 to 5 (1):  0-5
 #
 #  %  java BreadthFirstPaths largeG.txt 0
 #  0 to 0 (0):  0
 #  0 to 1 (418):  0-932942-474885-82707-879889-971961-...
 #  0 to 2 (323):  0-460790-53370-594358-780059-287921-...
 #  0 to 3 (168):  0-713461-75230-953125-568284-350405-...
 #  0 to 4 (144):  0-460790-53370-310931-440226-380102-...
 #  0 to 5 (566):  0-932942-474885-82707-879889-971961-...
 #  0 to 6 (349):  0-932942-474885-82707-879889-971961-...
 #
 #*****************************************************************************/

from collections import deque
import sys

class BreadthFirstPaths(object):
  """Run breadth first search on an undirected graph."""
  Inf = float("inf")

  def __init__(self, G, s):
    self._marked = [False]*G.V() # marked[v] = is there an s-v path
    self._edgeTo = [self.Inf]*G.V() # edgeTo[v] = previous edge on shortest s-v path
    self._distTo = [self.Inf]*G.V() # distTo[v] = number of edges shortest s-v path
    self._bfs(G, s)
    assert self._check(G, s)

  def _bfs(self, G, sources):
    """breadth-first search from multiple sources."""
    q = deque() # Queue
    if isinstance(sources, int):
      sources = [sources]
    for s in sources:
      self._marked[s] = True
      self._distTo[s] = 0
      q.append(s) # enqueue
    while q:
      v = q.popleft() # dequeue()
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


  def _check(self, G, s, prt=sys.stdout):
    """check optimality conditions for single source."""

    # check that the distance of s = 0
    if self._distTo[s] != 0:
      prt.write("distance of source {} to itself = {}\n".format(s, self._distTo[s]))
      return False

    # check that for each edge v-w dist[w] <= dist[v] + 1
    # provided v is reachable from s
    for v in range(G.V()):
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
    for w in range(G.V()):
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
