"""find shortest paths from a source vertex src to every other vertex in an undirected graph."""

import sys
from collections import OrderedDict
from collections import deque

class BreadthFirstPaths:
    """Run breadth first search on an undirected graph."""
    inf = float("inf")

    def __init__(self, graph, src, prt=None):
        # Mark src-vertex path
        self.marked = OrderedDict([(vertex, False)    for vertex in graph.keys])
        # edgeTo[vertex] = last edge on src-vertex path
        self.edge_to = OrderedDict([(vertex, self.inf) for vertex in graph.keys])
        # distTo[vertex] = number of edges shortest src-vertex path
        self.dist_to = OrderedDict([(vertex, self.inf) for vertex in graph.keys])
        self._bfs(graph, src, prt)
        assert self._check(graph, src)

    def _bfs(self, graph, sources, prt):
        """breadth-first search from multiple sources."""
        queue = deque() # Queue
        if isinstance(sources, int):
            sources = [sources]
        for src in sources:
            self.marked[src] = True
            self.dist_to[src] = 0
            queue.append(src) # enqueue
        while queue:
            vertex = self.deque(queue, prt)
            for w in graph.adj(vertex):
                if not self.marked[w]:
                    self.edge_to[w] = vertex
                    self.dist_to[w] = self.dist_to[vertex] + 1
                    self.marked[w] = True
                    queue.append(w) # enqueue(w)

    #### def hasPathTo(self, vertex):
    ####     return self.marked[vertex]

    def has_path_to(self, vertex):
        """True if there is a path to the vertex"""
        return self.marked[vertex]

    #### def distTo(self, vertex):
    ####     return self.dist_to[vertex]

    def dist_to(self, vertex):
        """Get distance in 'hops' to vertex"""
        return self.dist_to[vertex]

    def pathTo(self, vertex):
        """Returns a shortest path between the source vertex src (or sources) or None"""
        if not self.has_path_to(vertex):
            return None
        path = [] # Stack
        x = vertex
        while self.dist_to[x] != 0:
            path.append(x) # push
            x = self.edge_to[x]
        path.append(x) # push
        return path

    def deque(self, queue, prt):
        """Deque and print dequed value if user requests."""
        vertex = queue.popleft() # dequeue()
        if prt is not None:
            prt.write("{} ".format(vertex))
        return vertex

    def _check(self, graph, src, prt=sys.stdout):
        """check optimality conditions for single source."""

        # check that the distance of src = 0
        if self.dist_to[src] != 0:
            prt.write("distance of source {} to itself = {}\n".format(src, self.dist_to[src]))
            return False

        # check that for each edge vertex-w dist[w] <= dist[vertex] + 1
        # provided vertex is reachable from src
        for vertex in graph.keys:
            for w in graph.adj(vertex):
                if self.has_path_to(vertex) != self.has_path_to(w):
                    prt.write("edge {}-{}".format(vertex, w))
                    prt.write("has_path_to({}) = {}".format(vertex, self.has_path_to(vertex)))
                    prt.write("has_path_to({}) = {}".format(w, self.has_path_to(w)))
                    return False
                if self.has_path_to(vertex) and (self.dist_to[w] > self.dist_to[vertex] + 1):
                    prt.write("edge {}-{}".format(vertex, w))
                    prt.write("dist_to[{}] = {}".format(vertex, self.dist_to[vertex]))
                    prt.write("dist_to[{}] = {}".format(w, self.dist_to[w]))
                    return False

        # check that vertex = edgeTo[w] satisfies dist_to[w] + dist_to[vertex] + 1
        # provided vertex is reachable from src
        for w in graph.keys:
            if not self.has_path_to(w) or w == src: continue
            vertex = self.edge_to[w]
            if self.dist_to[w] != self.dist_to[vertex] + 1:
                prt.write("shortest path edge {}-{}".format(vertex, w))
                prt.write("dist_to[{}] = ".format(vertex, self.dist_to[vertex]))
                prt.write("dist_to[{}] = ".format(w, self.dist_to[w]))
                return False

        return True


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2019, DV Klopfenstein, Python port
