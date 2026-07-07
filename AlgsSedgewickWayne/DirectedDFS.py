"""Data type for determining the vertices reachable from a given src vertex(s).

Lecture: Digraph Search
"""


class DirectedDFS:
    """Data type for determining the vertices reachable from a given src vertex(s)."""

    def __init__(self, digraph, sources): # O ~ V + E (wc)
        if isinstance(sources, int):
            self._init(digraph, [sources])
        else:
            self._init(digraph, sources)

    def _init(self, digraph, sources):
        """Computes vertices in a digraph that are connected to any src vertices, sources"""
        ## print(f'DirectedDFS ON GRAPH({digraph})')
        # marked[v] is True if v is reachable from src (or srcs)
        self._marked = [False for _ in range(digraph.num_vertices)]
        self._count = 0 # number of vertexertices reachable from s
        for vertex in sources:
            if not self._marked[vertex]:
                self._dfs(digraph, vertex)

    def _dfs(self, digraph, v_src):
        """Depth First Search; Recursively called"""
        self._count += 1
        self._marked[v_src] = True
        for w_dst in digraph.adj(v_src):
            if not self._marked[w_dst]:
                self._dfs(digraph, w_dst)

    def marked(self, vertex):
        """Directed path from source vertex (or any of the source vertices) and vertex ?"""
        return self._marked[vertex]

    def count(self):
        """Returns the number of vertices reachable from the source vertex"""
        return self._count


# Copyright 2002-present, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-present, DV Klopfenstein, Python implementation.
