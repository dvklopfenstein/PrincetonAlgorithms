"""A directed graph, implemented using an array of lists. Parallel edges & self-loops permitted."""

__copyright__ = 'Copyright (C) 2023-present, DV Klopfenstein, PhD. All rights reserved'
__author__ = 'DV Klopfenstein, PhD'


class Digraph:
    """A directed graph, implemented w/array of lists. Parallel edges & self-loops permitted."""

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_edges = 0
        self._adj = [set() for v in range(num_vertices)]
        ##self._indegree = [0]*num_vertices # indegree[v] = indegree of vertex v
        self.keys = list(range(self.num_vertices))

    def add_edge(self, src_v, dst_w):
        """Adds directed edge src_v-dst_w to self graph."""
        self.num_edges += 1
        self._adj[src_v].add(dst_w)
        print(f'add_edge(src({src_v}), dst({dst_w}))')
        ##self._indegree[dst_w] += 1

    def get_edges(self):
        """Get all the edges of this directed graph"""
        adj = self._adj
        return set((src_v, dst_w) for src_v in self.keys for dst_w in adj[src_v])

    def adj(self, src_v):
        """Returns the vertices adjacent to vertex src_v."""
        return self._adj[src_v]

    def __str__(self):
        txt = [(("{V} vertices, {E} edges\n").format(V=self.num_vertices, E=self.num_edges))]
        for src_v in self.keys:
            txt.append("{src_v}: ".format(src_v=src_v))
            for dst_w in self._adj[src_v]:
                txt.append("{dst_w} ".format(dst_w=dst_w))
            txt.append("\n")
        return ''.join(txt)

    def __iter__(self): # Makes Graph an iterable.
        return iter(self._adj) # returns an iterator.


# Copyright (C) 2023-present, DV Klopfenstein, PhD. All rights reserved
