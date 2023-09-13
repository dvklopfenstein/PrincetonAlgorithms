"""Run depth first search on an undirected graph. O(E + V) time."""
# https://algs4.cs.princeton.edu/41graph


class DepthFirstSearch:
    """Gets vertices in graph connected to the source vertex (src_node) O(E + V)"""

    def __init__(self, graph_undirected, src_node):
        """Gets vertices in graph connected to the source vertex (src_node) O(E + V)"""
        # marked[v] = is there an s-v path?
        # THETA(V) extra space (not including the graph)
        self.marked = [False for _ in range(graph_undirected.num_nodes)]
        # number of vertices connected to s
        self.cnt = 0
        self._validate_vertex(src_node)
        self._dfs(graph_undirected, src_node)

    def _dfs(self, graph, node_v):
        """depth first search from node_v"""
        self.cnt += 1
        self.marked[node_v] = True
        for node_w in graph.adj(node_v):
            if not self.marked[node_w]:
                self._dfs(graph, node_w)

    def is_marked(self, node_v):
        """Return True if exists a path between the source vertex {@code s} and vertex {@code v}"""
        self._validate_vertex(node_v)
        return self.marked[node_v]

    def count(self):
        """Get number of vertices connected to the source vertex"""
        return self.cnt

    def _validate_vertex(self, node_v):
        """throw an IllegalArgumentException unless {@code 0 <= node_v < V}"""
        num_nodes = len(self.marked)
        if node_v < 0 or node_v >= num_nodes:
            raise RuntimeError("vertex {V} is not between 0 and {Z}".format(
                V=node_v, Z=num_nodes-1))


# Copyright 2002-present, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-present, DV Klopfenstein, Python implementation
