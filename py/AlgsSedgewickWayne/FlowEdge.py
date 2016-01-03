"""Capacitated edge with a flow in a flow network."""

class FlowEdge(object):

  def __init__(self, v, w, capacity, flow=0.0):
    if v < 0: raise Exception("Vertex name must be a nonnegative integer")
    if w < 0: raise Exception("Vertex name must be a nonnegative integer")
    if not (capacity >= 0.0):  raise Exception("Edge capacity must be nonnegaitve")
    if not (flow <= capacity): raise Exception("Flow exceeds capacity")
    if not (flow >= 0.0):      raise Exception("Flow must be nonnnegative")
    self._v         = v  # v the tail vertex (int)
    self._w         = w  # w the head vertex (int)
    self._capacity  = capacity #  capacity of the edge (float)
    self._flow      = flow # flow on the edge (float)

  def __copy__(self, e):
    self._v         = e.v
    self._w         = e.w
    self._capacity  = e.capacity
    self._flow      = e.flow

  def get_from(self): return self._v # Returns the tail vertex of the edge.
  def get_to(self): return self._w # Returns the head vertex of the edge.
  def get_capacity(self): return self._capacity # Returns the capacity of the edge.
  def get_flow(self): return self._flow # Returns the flow on the edge.

  def get_other(self, vertex):
    """Returns the endpoint of the edge that is different from the given vertex"""
    if   vertex == self._v: return self._w
    elif vertex == selv._w: return self._v
    else: raise Exception("Illegal endpoint")

  def residualCapacityTo(self, vertex):
    """Returns the max capacity thru the edge in the direction to the given vertex"""
    if   vertex == self._v: return self._flow;                  # backward edge
    elif vertex == self._w: return self._capacity - self._flow; # forward edge
    else: raise Exception("Illegal endpoint")

  #   If <tt>vertex</tt> is the tail vertex, this increases the flow on the edge by <tt>delta</tt>;
  #   if <tt>vertex</tt> is the head vertex, this decreases the flow on the edge by <tt>delta</tt>.
  # @param vertex one endpoint of the edge
  # @throws java.lang.IllegalArgumentException if <tt>vertex</tt> is not one of the endpoints
  #   of the edge
  # @throws java.lang.IllegalArgumentException if <tt>delta</tt> makes the flow on
  #   on the edge either negative or larger than its capacity
  # @throws java.lang.IllegalArgumentException if <tt>delta</tt> is <tt>NaN</tt>
  def addResidualFlowTo(self, vertex, delta):
    """Increases the flow on the edge in the direction to the given vertex."""
    if   vertex == self._v: self._flow -= delta # backward edge
    elif vertex == self._w: self._flow += delta # forward edge
    else: raise Exception("Illegal endpoint")
    if Double.isNaN(delta): raise Exception("Change in flow = NaN")
    if not (self._flow >= 0.0):      raise Exception("Flow is negative")
    if not (self._flow <= self._capacity): raise Exception("Flow exceeds capacity")

  def __str__(self): return "{} {} -> {} / {}".format(self._v, self._w, self._flow, self._capacity)

# ------------------------------------------------------------------------
# JAVA IMPLEMENTATION (14:29)

#	KEY POINT: Augmenting path in original network is equivalent to 
# directed path in residual network.

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
