"""Data type for determining the vertices reachable from a given src vertex(s).

Lecture: Digraph Search
"""


class DirectedDFS:
    """Data type for determining the vertices reachable from a given src vertex(s)."""

    def __init__(self, digraph, sources): # O ~ V + E (wc)
        self._marked = [False for _ in range(digraph.num_vertices)]
        self._count = 0 # number of vertex(s) reachable from sources
        self._init(digraph, [sources] if isinstance(sources, int) else sources)

    def _init(self, digraph, sources):
        """Computes vertices in a digraph that are connected to any src vertices, sources"""
        ## print(f'DirectedDFS ON GRAPH({digraph})')
        # marked[v] is True if v is reachable from src (or srcs)
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
        """Returns the number of vertices reachable from the source vertex(s)"""
        return self._count


# Copyright 2002, Robert Sedgewick and Kevin Wayne.
# Copyright 2015, DV Klopfenstein, Python implementation.
