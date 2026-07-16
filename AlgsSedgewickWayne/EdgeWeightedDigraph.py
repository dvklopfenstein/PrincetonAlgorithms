"""An edge-weighted digraph, implemented using adjacency lists."""

import random
from AlgsSedgewickWayne.DirectedEdge import DirectedEdge

class EdgeWeightedDigraph:
    """An edge-weighted digraph, implemented using adjacency lists."""

    def __init__(self, v_or_arr, num_edges=None):
        self.num_vertices = None
        self.num_edges    = None
        self._indegree    = [] # adj[v] = adjacency list for vertex v
        self._adj         = None
        if isinstance(v_or_arr, int):
            self._init_ve(v_or_arr, num_edges)
        else:
            self._init_arr(v_or_arr)

    ##def __copy__(self):
    ##    """Initializes a new edge-weighted digraph that is a deep copy of digrph."""
    ##    cls = self.__class__
    ##    result = cls.__new__(cls)
    ##    memo[id(self)] = result
    ##    self._init_v(digrph.self.num_vertices)
    ##    self.num_edges = digrph.E()
    ##    for v in range(digrph.num_vertices):
    ##        self._indegree[v] = digrph.indegree(v)
    ##    for v in range(digrph.num_vertices):
    ##        # reverse so that adjacency list is in same order as original
    ##        reverse = [] # new Stack<DirectedEdge>()
    ##        for e in digrph._adj[v]:
    ##            reverse.append(e)
    ##        for e in reverse:
    ##            self._adj[v].add(e)
    ##    return result

    # raise an IndexOutOfBoundsRuntimeError unless 0 <= v < V
    def _validate_vertex(self, v):
        if v < 0 or v >= self.num_vertices:
            raise RuntimeError(f"vertex {v} is not between 0 and {self.num_vertices-1}")

    def add_edge(self, e):
        """Adds the directed edge <tt>e</tt> to this edge-weighted digraph."""
        v = e.get_from()
        w = e.get_to()
        self._validate_vertex(v)
        self._validate_vertex(w)
        self._adj[v].add(e)
        self.num_edges += 1

    def adj(self, v):
        """Returns the directed edges incident from vertex v."""
        self._validate_vertex(v)
        return self._adj[v]

    def outdegree(self, v):
        """Returns the number of directed edges incident from vertex v."""
        self._validate_vertex(v)
        return self._adj[v].size()

    def indegree(self, v):
        """Returns the number of directed edges incident to vertex v."""
        self._validate_vertex(v)
        return self._indegree[v]

    def edges(self):
        """Returns all directed edges in this edge-weighted digraph."""
        lst = set()
        for v in range(self.num_vertices):
            for e in self._adj(v):
                lst.add(e)
        return lst

    def __str__(self):
        txt = [f"{self.num_vertices} vertices; {self.num_edges} edges\n"]
        for v in range(self.num_vertices):
            edges = "; ".join(str(e) for e in self._adj[v])
            txt.append(f"{v}: {edges}")
        return "\n".join(txt)

    # -- init ----------------------------------------------------------
    def _init_v(self, num_vertices):
        if num_vertices < 0:
            raise RuntimeError("Number of vertices in a Digraph must be nonnegative")
        self.num_vertices = num_vertices # number of vertices in self digraph
        self.num_edges = 0 # number of edges in self digraph
        self._adj = [set() for v in range(num_vertices)] # indegree[v] = indegree of vertex v

    def _init_ve(self, num_vertices, num_edges):
        """Initializes a random edge-weighted digraph with V vertices and E edges."""
        self._init_v(num_vertices)
        if num_edges is not None:
            if num_edges < 0:
                raise RuntimeError("Number of edges in a Digraph must be nonnegative")
            for _ in num_edges:
                v = random.randint(0, num_vertices-1) # get random int in [0, num_vertices)
                w = random.randint(0, num_vertices-1)
                weight = .01 * random.uniform(0, 100)
                e = DirectedEdge(v, w, weight)
                self.add_edge(e)

    def _init_arr(self, arr):
        """Initializes a random edge-weighted digraph with V vertices and E edges."""
        self._init_v(arr[0])
        self.num_edges = arr[1]
        if self.num_edges < 0:
            raise RuntimeError("Number of edges must be nonnegative")
        for v, w, weight in arr[2:]:
            if v < 0 or v >= self.num_vertices:
                raise RuntimeError(f"vertex {v} is not between 0 and {self.num_vertices-1}")
            if w < 0 or w >= self.num_vertices:
                raise RuntimeError(f"vertex {v} is not between 0 and {self.num_vertices-1}")
            self.add_edge(DirectedEdge(v, w, weight))


# Copyright 2002, Robert Sedgewick and Kevin Wayne.
# Copyright 2015, DV Klopfenstein, Python port
