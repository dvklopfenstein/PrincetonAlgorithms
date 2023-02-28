"""Depth-First-Search to determine vertices reachable given a source vertix(s)"""


class DirectedDFS:
    """Depth-First-Search to determine vertices reachable given a source vertix(s)"""

    def __init__(self, digraph): # O ~ V + E (wc)
        """Computes vertices in digraph digraph that are connected to any src vertices, sources"""
        self.digraph = digraph
        self.marked = [False for _ in range(digraph.num_vertices)]

    def get_reachable_states(self):
        """From source states, find all reachable states"""
        return set(v for v, m in enumerate(self.marked) if m)

    def dfs(self, digraph, v_src):
        """Depth First Search; Recursively called"""
        self.marked[v_src] = True
        for w_dst in digraph.adj(v_src):
            if not self.marked[w_dst]:
                self.dfs(digraph, w_dst)

    @classmethod
    def from_state0(cls, digraph):
        """Construct a depth first seach object to find all states reachable from state 0"""
        obj = cls(digraph)
        obj.dfs(digraph, 0)
        return obj

    @classmethod
    def from_sources(cls, digraph, sources):
        """Construct a depth first search object to find all states reachable from sources"""
        obj = cls(digraph)
        for w_dst in sources:
            if not obj.marked[w_dst]:
                obj.dfs(digraph, w_dst)
        return obj
