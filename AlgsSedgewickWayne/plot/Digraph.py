"""A directed graph, implemented using an array of lists. Parallel edges & self-loops permitted."""
# pylint: disable=invalid-name
# ../algs4/src/main/java/edu/princeton/cs/algs4/Digraph.java

import pydot


class PlotDigraph:
    """A directed graph, implemented w/array of lists. Parallel edges & self-loops permitted."""

    def __init__(self, digraph):
        self.digraph = digraph

    def wr_png(self, fout_png="Digraph.png"):
        """Make a png showing a diagram of the connected components."""
        dot_digraph = self.get_pydot_digraph()
        # pylint: disable=no-member
        dot_digraph.write_png(fout_png)
        print(f"  WROTE: {fout_png}")

    def get_pydot_digraph(self):
        """Make a pydot graph showing a diagram of the connected components."""
        # 1. Create/initialize Graph
        digraph = pydot.Dot(graph_type='digraph') # Undirected Graph
        # 2. Create Nodes
        nodes = [pydot.Node(src_v) for src_v in self.digraph.keys]
        # 3. Add nodes to Graph
        for node in nodes:
            digraph.add_node(node)
        # 4. Add Edges between Nodes to Graph
        for src_v, dst_w in self.get_edges():
            if src_v != dst_w: # Print only edges from one node to another (not to self)
                digraph.add_edge(pydot.Edge(src_v, dst_w))
        return digraph

    def get_edges(self):
        """Get all the edges of this directed graph"""
        edges = set()
        for src_v in self.digraph.keys:
            for dst_w in self.digraph.adjs[src_v]:
                ###edges.add(tuple(sorted([src_v, dst_w])))
                edges.add(tuple([src_v, dst_w]))
        return edges


#  Copyright 2015-present, DV Klopfenstein, PhD, Python implementation
