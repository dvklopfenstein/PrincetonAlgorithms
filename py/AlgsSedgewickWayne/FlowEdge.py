"""Capacitated edge with a flow in a flow network."""
# TBD Finish Python port

 #  The <tt>FlowEdge</tt> class represents a capacitated edge with a 
  # flow in a {@link FlowNetwork}. Each edge consists of two integers
 #  (naming the two vertices), a real-valued capacity, and a real-valued
 #  flow. The data type provides methods for accessing the two endpoints
 #  of the directed edge and the weight. It also provides methods for
 #  changing the amount of flow on the edge and determining the residual
 #  capacity of the edge.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/64maxflow">Section 6.4</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
class FlowEdge(object):
  private final v;             # from
  private final w;             # to 
  private final double capacity;   # capacity
  private double flow;             # flow

    #*
     # Initializes an edge from vertex <tt>v</tt> to vertex <tt>w</tt> with
     # the given <tt>capacity</tt> and zero flow.
     # @param v the tail vertex
     # @param w the head vertex
     # @param capacity the capacity of the edge
     # @throws java.lang.IndexOutOfBoundsException if either <tt>v</tt> or <tt>w</tt>
     #    is a negative integer
     # @throws java.lang.IllegalArgumentException if <tt>capacity</tt> is negative
     #/
  public FlowEdge(int v, w, double capacity):
      if v < 0) raise new IndexOutOfBoundsException("Vertex name must be a nonnegative integer")
      if w < 0) raise new IndexOutOfBoundsException("Vertex name must be a nonnegative integer")
      if !(capacity >= 0.0)) raise new IllegalArgumentException("Edge capacity must be nonnegaitve")
      self.v         = v
      self.w         = w
      self.capacity  = capacity
      self.flow      = 0.0

    #*
     # Initializes an edge from vertex <tt>v</tt> to vertex <tt>w</tt> with
     # the given <tt>capacity</tt> and <tt>flow</tt>.
     # @param v the tail vertex
     # @param w the head vertex
     # @param capacity the capacity of the edge
     # @param flow the flow on the edge
     # @throws java.lang.IndexOutOfBoundsException if either <tt>v</tt> or <tt>w</tt>
     #    is a negative integer
     # @throws java.lang.IllegalArgumentException if <tt>capacity</tt> is negative
     # @throws java.lang.IllegalArgumentException unless <tt>flow</tt> is between 
     #    <tt>0.0</tt> and <tt>capacity</tt>.
     #/
  public FlowEdge(int v, w, double capacity, double flow):
      if v < 0) raise new IndexOutOfBoundsException("Vertex name must be a nonnegative integer")
      if w < 0) raise new IndexOutOfBoundsException("Vertex name must be a nonnegative integer")
      if !(capacity >= 0.0))  raise new IllegalArgumentException("Edge capacity must be nonnegaitve")
      if !(flow <= capacity)) raise new IllegalArgumentException("Flow exceeds capacity")
      if !(flow >= 0.0))      raise new IllegalArgumentException("Flow must be nonnnegative")
      self.v         = v
      self.w         = w
      self.capacity  = capacity
      self.flow      = flow

    #*
     # Initializes a flow edge from another flow edge.
     # @param e the edge to copy
     #/
  public FlowEdge(FlowEdge e):
      self.v         = e.v
      self.w         = e.w
      self.capacity  = e.capacity
      self.flow      = e.flow

  def from(self): return self._v # Returns the tail vertex of the edge.
  def to(self): return self._w # Returns the head vertex of the edge.
  def capacity(self): return self._capacity # Returns the capacity of the edge.
  def flow(self): return self._flow # Returns the flow on the edge.

  def other(self, vertex):
    """Returns the endpoint of the edge that is different from the given vertex"""
    if   vertex == self._v: return self._w
    elif vertex == selv._w: return self._v
    else: raise Exception("Illegal endpoint")

  def residualCapacityTo(self, vertex):
    """Returns the residual capacity of the edge in the direction to the given vertex"""
    if   vertex == self._v: return self._flow;                  # backward edge
    elif vertex == self._w: return self._capacity - self._flow; # forward edge
    else: raise Exception("Illegal endpoint")

    #*
     #   If <tt>vertex</tt> is the tail vertex, this increases the flow on the edge by <tt>delta</tt>;
     #   if <tt>vertex</tt> is the head vertex, this decreases the flow on the edge by <tt>delta</tt>.
     # @param vertex one endpoint of the edge
     # @throws java.lang.IllegalArgumentException if <tt>vertex</tt> is not one of the endpoints
     #   of the edge
     # @throws java.lang.IllegalArgumentException if <tt>delta</tt> makes the flow on
     #   on the edge either negative or larger than its capacity
     # @throws java.lang.IllegalArgumentException if <tt>delta</tt> is <tt>NaN</tt>
     #/
  def addResidualFlowTo(self, vertex, delta):
    """Increases the flow on the edge in the direction to the given vertex."""
    if   vertex == self._v: self._flow -= delta # backward edge
    elif vertex == self._w: self._flow += delta # forward edge
    else: raise Exception("Illegal endpoint")
    if Double.isNaN(delta): raise Exception("Change in flow = NaN")
    if not (self._flow >= 0.0):      raise Exception("Flow is negative")
    if not (self._flow <= self._capacity): raise Exception("Flow exceeds capacity")


  def __str__(self): return "{} -> {} / {}".format(self._v, self._w, + " " + flow + "/" + capacity

# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
