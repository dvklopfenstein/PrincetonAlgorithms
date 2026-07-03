"""Immutable weighted edge."""
# pylint: disable=invalid-name


class Edge:
    """Edge between two vertices"""

    def __init__(self, v, w, weight):
        if v < 0:
            raise RuntimeError("Vertex name must be a nonnegative integer")
        if w < 0:
            raise RuntimeError("Vertex name must be a nonnegative integer")
        if not isinstance(weight, float):
            raise RuntimeError("Weight is NaN")
        self.v_src = v
        self.w_dst = w
        self.weight = weight

    def get_from(self):
        """Get the vertex at the beginning of this edge (the source)"""
        return self.v_src

    def get_to(self):
        """Get the vertex at the end of this edge (the destination)"""
        return self.w_dst

    def either(self):
        """Returns either endpoint of self edge"""
        return self.v_src

    def get_vw(self):
        """Get both vertices attached to this edge"""
        return [self.v_src, self.w_dst]

    def other(self, vertex):
        """Returns the endpoint of self edge that is different from the given vertex."""
        if vertex == self.v_src:
            return self.w_dst
        if vertex == self.w_dst:
            return self.v_src
        raise RuntimeError("Illegal endpoint")

    def compare_to(self, that):
        """Compares two edges by weight."""
        if self.weight < that.weight:
            return -1
        if self.weight > that.weight:
            return +1
        return  0

    def __str__(self):
        return f"{self.v_src}-{self.w_dst} {self.weight:.5f}"


# Copyright 2002-present Robert Sedgewick and Kevin Wayne.
# Copyright 2002-present DV Klopfenstein, Pythom port
