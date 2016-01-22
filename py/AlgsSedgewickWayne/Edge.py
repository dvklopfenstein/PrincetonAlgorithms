"""Immutable weighted edge."""

class Edge(object):

  def __init__(self, v, w, weight):
    if v < 0: raise Exception("Vertex name must be a nonnegative integer")
    if w < 0: raise Exception("Vertex name must be a nonnegative integer")
    if not isinstance(weight, float): raise Exception("Weight is NaN")
    self._v = v
    self._w = w
    self._weight = weight

  def weight(self): return self._weight # Returns the weight of self edge.
  def either(self): return self._v # Returns either endpoint of self edge.
  def get_vw(self): return [self._v, self._w]

  def other(self, vertex):
    """Returns the endpoint of self edge that is different from the given vertex."""
    if   vertex == self._v: return self._w
    elif vertex == self._w: return self._v
    else: raise Exception("Illegal endpoint")

  def compareTo(self, that):
    """Compares two edges by weight."""
    if   self.weight() < that.weight(): return -1
    elif self.weight() > that.weight(): return +1
    else:                               return  0

  def __str__(self): return "{}-{} {:.5f}".format(self._v, self._w, self._weight)

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2002-2016, DV Klopfenstein, Pythom port
