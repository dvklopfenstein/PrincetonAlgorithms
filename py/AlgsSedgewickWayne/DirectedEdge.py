"""Immutable weighted directed edge."""

class DirectedEdge(object): 
  """a directed edge from vertex v to vertex w with the given weight"""

  def __init__(self, v, w, weight):
    if v < 0: raise Exception("Vertex names must be nonnegative integers")
    if w < 0: raise Exception("Vertex names must be nonnegative integers")
    if not isinstance(weight, float): raise Exception("Weight is NaN")
    self._v = v # the tail vertex
    self._w = w # the head vertex
    self._weight = weight # the weight of the directed edge

  def get_from(self): return self._v # Returns the tail vertex of the directed edge.
  def get_to(self): return self._w # Returns the head vertex of the directed edge.
  def get_from_to(self): return [self._v, self._w]
  def get_weight(self): return self._weight # Returns the weight of the directed edge.
  def __str__(self):
    return "{v} -> {w} {wt:5.2f}".format(v=self._v, w=self._w, wt=self._weight)

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
