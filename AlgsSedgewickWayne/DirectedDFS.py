"""Data type for determining the vertices reachable from a given src vertex(s)."""
# pylint: disable=invalid-name


class DirectedDFS:
    """Data type for determining the vertices reachable from a given src vertex(s)."""

    def __init__(self, graph, sources): # O ~ V + E (wc)
        if isinstance(sources, int):
            self._init(graph, [sources])
        else:
            self._init(graph, sources)

    def _init(self, graph, sources):
        """Computes vertices in digraph graph that are connected to any src vertices, sources"""
        ## print(f'DirectedDFS ON GRAPH({graph})')
        self._marked = [False for _ in range(graph.num_vertices)] # True if v is reachable from src (or srcs)
        self._count = 0 # number of vertexertices reachable from s
        for vertex in sources:
            if not self._marked[vertex]:
                self._dfs(graph, vertex)

    def _dfs(self, graph, v_src):
        """Depth First Search; Recursively called"""
        self._count += 1
        self._marked[v_src] = True
        for w_dst in graph.adj(v_src):
            if not self._marked[w_dst]:
                self._dfs(graph, w_dst)

    def marked(self, vertex):
        """Directed path from source vertex (or any of the source vertices) and vertex ?"""
        return self._marked[vertex]

    def count(self):
        """Returns the number of vertices reachable from the source vertex"""
        return self._count


# Copyright 2002-present, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-present, DV Klopfenstein, Python implementation.
