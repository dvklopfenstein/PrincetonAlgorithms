"""Immutable weighted directed edge."""


class DirectedEdge:
    """a directed edge from vertex v_src to vertex w_dst with the given weight"""

    def __init__(self, v_src, w_dst, weight):
        if v_src < 0:
            raise RuntimeError("Vertex names must be nonnegative integers")
        if w_dst < 0:
            raise RuntimeError("Vertex names must be nonnegative integers")
        if not isinstance(weight, float):
            raise RuntimeError("Weight should be a float")
        self.v_src = v_src # the tail vertex
        self.w_dst = w_dst # the head vertex
        self.weight = weight # the weight of the directed edge

    def get_from(self):
        """Get the tail vertex of the directed edge"""
        return self.v_src

    def get_to(self):
        """Get the head vertex of the directed edge"""
        return self.w_dst

    def get_from_to(self):
        """Get the tail(source) and head(destination) of the edge"""
        return [self.v_src, self.w_dst]

    def get_weight(self):
        """Get the weight of the directed edge"""
        return self.weight

    def __str__(self):
        return f"{self.v_src} -> {self.w_dst} {self.weight:5.2f}"


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2019, DV Klopfenstein, Python port
