"""An edge-weighted undirected graph, implemented using adjacency lists."""
# pylint: disable=invalid-name

import random
from AlgsSedgewickWayne.Edge import Edge


class EdgeWeightedGraph:
    """Undirected weighter graph. Parallel edges and self-loops are permitted."""

    def __init__(self, V, E=None):
        if isinstance(V, int):
            self._init_int(V, E)
        else:
            self._init_arr(V)

    def _init_num_vertices(self, num_vertices):
        """Graph with num_vertices vertices and no Edges."""
        if num_vertices < 0:
            raise Exception("Number of vertices must be nonnegative")
        self.num_vertices = num_vertices  # Use instead of Java's V()
        self.num_edges = 0                # Use instead of Java's E()
        self._adj = [set() for v_src in range(num_vertices)]

    def _init_int(self, num_vertices, num_edges):
        """Graph with num_vertices vertices, randomly connected w_dst/random weights."""
        self._init_num_vertices(num_vertices)
        if num_edges < 0:
            raise Exception("Number of edges must be nonnegative")
        for _ in range(num_edges):
            v_src = random.randint(0, num_vertices) # get random int in [0, num_vertices)
            w_dst = random.randint(0, num_vertices)
            weight = random.uniform()
            edge = Edge(v_src, w_dst, weight)
            self.add_edge(edge)

    def _init_arr(self, arr):
        self._init_num_vertices(arr[0])
        self.num_edges = arr[1]
        if self.num_edges < 0:
            raise Exception("Number of edges must be nonnegative")
        for num_edges in arr[2:]:
            v_src = num_edges[0]
            w_dst = num_edges[1]
            weight = num_edges[2]
            edge = Edge(v_src, w_dst, weight)
            self.add_edge(edge)

    def __copy__(self):
        self._init_num_vertices(self.num_vertices)
        self.num_edges in self.num_edges
        for v_src in range(self.num_vertices):
            # reverse so that adjacency list is in same order as original
            reverse = [] # Stack<Edge>()
            for edge in self._adj[v_src]:
                reverse.append(edge) # push(edge)
            for edge in reverse:
                self._adj[v_src].add(edge)

    def _validate_vertex(self, v_src):
        """raise an IndexOutOfBoundsException unless 0 <= v_src < num_vertices"""
        if v_src < 0 or v_src >= self.num_vertices:
            raise Exception("vertex {} is not between 0 and {}".format(
                v_src, (self.num_vertices-1)))

    def add_edge(self, edge):
        """Adds the undirected edge <tt>edge</tt> to this edge-weighted graph."""
        v_src = edge.either()
        w_dst = edge.other(v_src)
        self._validate_vertex(v_src)
        self._validate_vertex(w_dst)
        self._adj[v_src].add(edge)
        self._adj[w_dst].add(edge)
        self.num_edges += 1

    def adj(self, v_src):
        """Returns the edges incident on vertex v_src."""
        self._validate_vertex(v_src)
        return self._adj[v_src]

    def degree(self, v_src):
        """Returns the degree of vertex v_src."""
        self._validate_vertex(v_src)
        return self._adj[v_src].size()

    def edges(self):
        """Returns all edges in this edge-weighted graph."""
        bag = set()
        for v_src in range(self.num_vertices):
            self_loops = 0
            for edge in self._adj[v_src]:
                if edge.other(v_src) > v_src:
                    bag.add(edge)
                # only add one copy of each self loop (self loops will be consecutive)
                elif edge.other(v_src) == v_src:
                    if self_loops % 2 == 0:
                        bag.add(edge)
                    self_loops += 1
        return bag

    def __str__(self):
        txt = ["{} {}\n".format(self.num_vertices, self.num_edges)]
        for v_src in range(self.num_vertices):
            txt.append("{}: ".format(v_src))
            for edge in self._adj[v_src]:
                txt.append("{}  ".format(edge))
            txt.append("\n")
        return ''.join(txt)


# Copyright 2002-present, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-present, DV Klopfenstein, Python port
