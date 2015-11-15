"""Ford-Fulkerson: compute a max flow and a min cut using shortest augmenting path rule."""
# TBD Finish Python port

 #  This implementation uses the <em>Ford-Fulkerson</em> algorithm with
 #  the <em>shortest augmenting path</em> heuristic.
 #  The constructor takes time proportional to <em>E V</em> (<em>E</em> + <em>V</em>)
 #  in the worst case and extra space (not including the network)
 #  proportional to <em>V</em>, where <em>V</em> is the number of vertices
 #  and <em>E</em> is the number of edges. In practice, the algorithm will
 #  run much faster.
 #  Afterwards, the <tt>inCut()</tt> and <tt>value()</tt> methods take
 #  constant time.
 #  <p>
 #  If the capacities and initial flow values are all integers, then this
 #  implementation guarantees to compute an integer-valued maximum flow.
 #  If the capacities and floating-point numbers, then floating-point
 #  roundoff error can accumulate.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

from AlgsSedgewickWayne.FlowNetwork import FlowNetwork

class FordFulkerson(object):
  """Data type for computing maxflow and mincut in a flow network."""

  Inf = float('Inf')
  private static final double FLOATING_POINT_EPSILON = 1E-11

  private boolean[] marked;     # marked[v] = True iff s->v path in residual graph
  private FlowEdge[] edgeTo;    # edgeTo[v] = last edge on shortest residual s->v path
  private double value;         # current value of max flow
  
  def __init__(self, FlowNetwork G, s, t):
    self._validate(s, G.V())
    self._validate(t, G.V())
    if s == t:                       raise Exception("Source equals sink")
    if not self.isFeasible(G, s, t): raise Exception("Initial flow is infeasible")

    # while there exists an augmenting path, use it
    self._value = self.excess(G, t) # current value of max flow
    while self.hasAugmentingPath(G, s, t):

        # compute bottleneck capacity
        bottle = self.Inf
        v = t
        while v != s:
          bottle = min(bottle, self._edgeTo[v].residualCapacityTo(v))
          v = self._edgeTo[v].other(v)):

        # augment flow
        v = t
        while v != s:
          self._edgeTo[v].addResidualFlowTo(v, bottle)
          v = self._edgeTo[v].other(v)):

        self._value += bottle

    # check optimality conditions
    assert _check(G, s, t)

  # Returns the value of the maximum flow.
  def value(self): return self._value

  def inCut(self, v):
    """Returns true if the specified vertex is on the s side of the mincut."""
    self._validate(v, len(self._marked))
    return self._marked[v]

  def _validate(self, v, V):
    """raise an exception if v is outside prescibed range"""
    if v < 0 or v >= V:
      raise Exception("vertex {} is not between 0 and {}\n".format(v, V-1))


  # is there an augmenting path? 
  # if so, upon termination edgeTo[] will contain a parent-link representation of such a path
  # self implementation finds a shortest augmenting path (fewest number of edges),
  # which performs well both in theory and in practice
  def _hasAugmentingPath(FlowNetwork G, s, t):
    edgeTo = new FlowEdge[G.V()]
    marked = new boolean[G.V()]

    # breadth-first search
    Queue<Integer> queue = new Queue<Integer>()
    queue.enqueue(s)
    marked[s] = True
    while (!queue.isEmpty() and !marked[t]):
      v = queue.dequeue()

      for e in G.adj(v): # Loop thru FLowEdges
        w = e.other(v)

        # if residual capacity from v to w
        if e.residualCapacityTo(w) > 0:
            if not self._marked[w]:
                self._edgeTo[w] = e
                self._marked[w] = True
                queue.enqueue(w)

    # is there an augmenting path?
    return self._marked[t]



  def _excess(self, G, v):
    """return excess flow at vertex v"""
    excess = 0.0
    for e in G.adj(v): # Loop thru FlowEdges of FlowNetwork
      if v == e.get_from(): excess -= e.flow()
      else:                 excess += e.flow()
    return excess

  # return excess flow at vertex v
  def _isFeasible(FlowNetwork G, s, t):

      # check that capacity constraints are satisfied
      for (int v = 0; v < G.V(); v += 1):
          for (FlowEdge e : G.adj(v)):
              if e.flow() < -FLOATING_POINT_EPSILON or e.flow() > e.capacity() + FLOATING_POINT_EPSILON):
                  System.err.println("Edge does not satisfy capacity constraints: " + e)
                  return False

      # check that net flow into a vertex equals zero, except at source and sink
      if abs(value + excess(G, s)) > FLOATING_POINT_EPSILON):
        System.err.println("Excess at source = " + excess(G, s))
        System.err.println("Max flow         = " + value)
        return False
      if abs(value - excess(G, t)) > FLOATING_POINT_EPSILON):
        System.err.println("Excess at sink   = " + excess(G, t))
        System.err.println("Max flow         = " + value)
        return False
      for v in G.V():
        if v == s or v == t: continue
        elif abs(excess(G, v)) > FLOATING_POINT_EPSILON):
          System.err.println("Net flow out of " + v + " doesn't equal zero")
          return False
      return True



  # check optimality conditions
  def _check(FlowNetwork G, s, t):

      # check that flow is feasible
      if !isFeasible(G, s, t)):
          System.err.println("Flow is infeasible")
          return False

      # check that s is on the source side of min cut and that t is not on source side
      if !inCut(s)):
          System.err.println("source " + s + " is not on source side of min cut")
          return False
      if inCut(t)):
          System.err.println("sink " + t + " is on source side of min cut")
          return False

      # check that value of min cut = value of max flow
      double mincutValue = 0.0
      for (int v = 0; v < G.V(); v += 1):
          for (FlowEdge e : G.adj(v)):
              if (v == e.from()) and inCut(e.from()) and !inCut(e.to()))
                  mincutValue += e.capacity()

      if Math.abs(mincutValue - value) > FLOATING_POINT_EPSILON):
          System.err.println("Max flow value = " + value + ", min cut value = " + mincutValue)
          return False

      return True


# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
