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
  FLOATING_POINT_EPSILON = 1E-11

  def __init__(self, G, s, t): # G is FlowNetwork
    self._validate(s, G.V())
    self._validate(t, G.V())
    self._marked # marked[v] = True iff s->v path in residual graph
    self._edgeTo # edgeTo[v] = last FlowEdge on shortest residual s->v path
    self._value  # current value(float) of max flow
    if s == t:                        raise Exception("Source equals sink")
    if not self._isFeasible(G, s, t): raise Exception("Initial flow is infeasible")

    # while there exists an augmenting path, use it
    self._value = self._excess(G, t) # current value of max flow
    while self._hasAugmentingPath(G, s, t):

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
    assert self._check(G, s, t)

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
  def _hasAugmentingPath(self, G, s, t): # G id FlowNetwork
    self._edgeTo = [None  for i in range(G.V())] # Will contain FlowEdges
    self._marked = [False for i in range(G.V())]

    # breadth-first search (note: Can also use other search algorithms can also be adapted)
    queue = cx.deque() # Queue
    queue.append(s) # enqueue(s)
    self._marked[s] = True
    while queue and not self._marked[t]:
      v = queue.popleft() # dequeue()

      for e in G.adj(v): # Loop thru FLowEdges
        w = e.other(v)

        # if residual capacity from v to w
        if e.residualCapacityTo(w) > 0: # Have a way to get to w
          if not self._marked[w]: # Have not been there yet
            self._edgeTo[w] = e
            self._marked[w] = True
            queue.append(w) # enqueue(w)

    # is there an augmenting path?
    return self._marked[t] # Is t reachable from s in residual network?



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
              if e.flow() < -self.FLOATING_POINT_EPSILON or e.flow() > e.capacity() + self.FLOATING_POINT_EPSILON):
                  sys.stderr.write("Edge does not satisfy capacity constraints: " + e)
                  return False

      # check that net flow into a vertex equals zero, except at source and sink
      if abs(value + self._excess(G, s)) > self.FLOATING_POINT_EPSILON):
        sys.stderr.write("Excess at source = {}".format(self._excess(G, s)))
        sys.stderr.write("Max flow         = {}".format(value))
        return False
      if abs(value - self._excess(G, t)) > self.FLOATING_POINT_EPSILON):
        sys.stderr.write("Excess at sink   = {}".format(self._excess(G, t)))
        sys.stderr.write("Max flow         = {}".format(value))
        return False
      for v in G.V():
        if v == s or v == t: continue
        elif abs(self._excess(G, v)) > self.FLOATING_POINT_EPSILON):
          sys.stderr.write("Net flow out of " + v + " doesn't equal zero")
          return False
      return True



  # check optimality conditions
  def _check(FlowNetwork G, s, t):

      # check that flow is feasible
      if not self._isFeasible(G, s, t):
          sys.stderr.write("Flow is infeasible")
          return False

      # check that s is on the source side of min cut and that t is not on source side
      if not self.inCut(s):
          sys.stderr.write("source {} is not on source side of min cut".format(s))
          return False
      if self.inCut(t):
          sys.stderr.write("sink {} is on source side of min cut".format(t))
          return False

      # check that value of min cut = value of max flow
      mincutValue = 0.0
      for (int v = 0; v < G.V(); v += 1):
          for e in G.adj(v): # iterate thru FlowEdges
              if (v == e.from()) and self.inCut(e.from()) and not self.inCut(e.to()))
                  mincutValue += e.capacity()

      if Math.abs(mincutValue - value) > self.FLOATING_POINT_EPSILON):
          sys.stderr.write("Max flow value = " + value + ", min cut value = " + mincutValue)
          return False

      return True


# -----------------------------------------------------------------
# INTRODUCTION TO MAXFLOW (10:33)

# MINCUT PROBLEM 2:49
#
# DEF: A **st-cut (cut)** is a partition of the vertices into two disjoint sets,
# with s in onset A and t in the other set B.
#
# DEF: Its **capacity** is the sum of the capacities of the edges from A to B.

# 1) QUESTION: In the flow network below, what is the capacity of the cut with 
# A = {s, 2, 4} and B = {1, 3, t}?
#
#           (1)--4-->(3)
#          ^ | \      ^ \
#         /  |  \     |  \
#        /   |   \    |   \
#      10    2    8   6    10
#      /     |     \  |     \
#     /      v      v |      v
#   (s)-10->(2)--9-->(4)-10->(t)
#
# ANSWER #1 (Pick one):
#   19
#   20
#   26 
#   36

# MAXFLOW PROBLEM 6:11
#
# DEF: An **st-flow (flow)** is an assignment of values to the edges such that:
#   * Capacity constraint: 0 <= edge's flow <= edge's capacity.
#   * Local equilibrium: inflow = outflow at every vertex (except s and t)
#
# DEF: The **value** of a flow is "the inflow at t" or the "outflow at s".
#      (we assume no edge points to s or from t)
#
# MAXIMUM ST-FLOW (MAXFLOW) PROBLEM. Find a flow of maximum value.

# 2) QUESTION: In the flow network below, what is the value of the flow f?
#
#           (1)-0/4->(3)
#          ^ | \      ^ \
#         /  |  \     |  \
#        /   |   \    |   \
#   10/10   2/2  8/8 6/6  6/10
#      /     |     \  |     \
#     /      v      v |      v
#   (s)6/10>(2)-8/9->(4)10/10>(t)
#
# ANSWER #2 (Pick one):
#   10
#   16
#   18 
#   19
#
# EXPLANATION: By definition, it is the inflow at t, which is 10 + 6

# SUMMARY:
# 
# INPUT: A weighted digraph, source vertex s, and target vertex t.
# MINCUT PROBLEM: Find a cut of minimum capacity.
# MAXFLOW PROBLEM: Find a flow of maximum value.
#
# REMARKABLE FACT: These two problems are dual!
# If you solve one problem, you solve the other.

#-----------------------------------------------------------------------
# FORD-FULKERSON ALGORITHM (6:32)
# (Dates back to the 1950s)

# FORD-FULKERSON ALGORITHM 
#
# INITIALIZATION: Start with 0 flow. (But has capacity)

# IDEA: INCREASE FLOW ALONG AUGMENTING PATHS 00:34
#
# AUGMENTING PATH: Find an undirected path from s to t such that:
#   * Can increase flow on forward edges (not full).
#   * Can decrease flow on backward edge (not empty).

# IDEA: INCREASE FLOW ALONG AUGMENTING PATHS 4:29
#
# TERMINATION: All paths from s to t are blocked by either a
#   * Full forward edge.  (ie Can't add    more flow to forward edge)
#   * Empty backward edge.(ie Can't remove more flow from a backward edge)

# FORD-FULKERSON ALGORITHM  5:06
#
# 1. Start with 0 flow.
# 2. While there exists an augmenting path:
#    * find an augmenting path
#    * compute bottleneck capacity
#    * increase flow on that path by bottleneck capcity
#
# QUESTIONS:
#   * How to compute a mincut? EASY.
#   * How to find an augmenting path? BFS WORKS WELL. (Many ways, though)
#   * If FF terminates, does it always compute a maxflow? YES
#   * Does DD always terminate?
#     => yes, provided edge capacities are integers (or augmenting paths are chosen carefully)
#     * If so, after how many augmentations?
#       -> requires clever analysis

# 3) QUESTION: In the flow network below, how many distinct augmenting paths are there 
# with respect to the given flow f?
#
#           (1)-0/4->(3)
#          ^ | \      ^ \
#         /  |  \     |  \
#        /   |   \    |   \
#   10/10   2/2  8/8 6/6  6/10
#      /     |     \  |     \
#     /      v      v |      v
#   (s)6/10>(2)-8/9->(4)10/10>(t)
#
# ANSWER #3 (pick one):
#   0
#   1
#   2 
#   3
#

#-----------------------------------------------------------------------
# MAXFLOW-MINCUT THEOREM (9:38)

# 4) QUESTION: Given a flow network, let f be any flow and let (A, B) be any cut.
# Then, the net flow across (A, B) is ____ the value of f.
#
#  * less than
#  * greater than
#  * not related to

# 5) QUESTION: Given a maxflow f in a flow network, what is the order of growth 
# of the running time to compute a mincut?
#
#  * V + E
#  * V^2
#  * V(E + V)
#  * E^2

#-----------------------------------------------------------------------
# RUNNING TIME ANALYSIS (8:49)

# FORD-FULKERSON ALGORITHM
# 1. Start with 0 flow.
# 2. While there exists an augmenting path:
#    * find an augmenting path
#    * compute bottleneck capacity
#    * increase flow on that path by bottleneck capcity
#
# QUESTIONS:
#   * How to compute a mincut? EASY.
#   * How to find an augmenting path? BFS WORKS WELL. (Many ways, though)
#   * If FF terminates, does it always compute a maxflow? YES
#   * Does DD always terminate?
#     => yes, provided edge capacities are integers (or augmenting paths are chosen carefully)
#     * If so, after how many augmentations?
#       -> requires clever analysis

# FF W/INTEGER CAPACITIES 02:05
# IMPORTANT SPECIAL CASE: Edge capacities are integers betwen 1 and U.
# INVARIANT: The flow is **integer-values** throughout FF.
# ...
# INTEGRALITY THEOREM: There exists an integer-valued maxflow (and FF finds one!).
#   * important for some applications (stay tuned)
# ...

# 6) QUESTION: If all the edge capacities are integers, the value of the maxflow is:
#    * integer 
#    * rational number 
#    * real number
#    * imaginary number

#-----------------------------------------------------------------------
# JAVA IMPLEMENTATION (14:29)

# 7) QUESTION: Suppose that Edge e is an edge returned by G.adj(v), with w = e.other(v) and
# e.residualCapacityTo(w) > 0. Which of the following myst be true?
#   * e = v -> w is a forward edge that is not full
#   * e = v -> w is a backward edge that is not empty
#   * e = v -> w is either a forward edge that is not full or a backward edge that is not empty.
#   * None of the above

#-----------------------------------------------------------------------
# MAXFLOW AND MINCUT APPLICATIONS (22:20)
#  * Data mining
#  * Open-pit mining
#  * Bipartite matching
#  * Network reliability
#  * Baseball elimination
#  * Image segmentation
#  * Betwork connectivity
#  * Distributed computing
#  * Egaltarian stable matching
#  * Security of statistical data.
#  * Mutli-camera scene reconstruction
#  * Sensor placment for homeland security
#  ...

# 8) QUESTION: Suppose that you run the Ford-Fulkerson algorithm(using the 
#    shortest augmenting path heuristic) to solve a bipartite matching problem
#    with N students and N companies. How many augmenting paths are needed in the 
#    worst case?
#      *       N
#      *       N^2
#      * (1/2)*N^3
#      *       N^3

# 9) QUESTION: How many vertices and edges, respectively, are there in the flow
#    network that is constructed to determine whether one team is mathematically
#    eliminated from a baseball league containing N teams? Give the order of growth
#    in the worst case (when there is a game remaining between every pair of teams
#    in the league).
#      * N   and N^2
#      * N^2 and N^2
#      * N^2 and N^3
#      * N^2 and N^4

#-----------------------------------------------------------------------
# ANSWERS: WEEK 3 MAXIMUM FLOW (72:21)
#
# 1) ANSWER: 26 
#
# 2) ANSWER: 16 
#
# 3) ANSWER: 2
#   EXPLANATION: The two augmenting paths are:
#     s -> 2 -> 1 -> 3 -> t         (with bottleneck capacity 2) and
#     s -> 2 -> 4 -> 1 -> -> 3 -> t (with bottleneck capacity 1)
#
# 4) ANSWER: equal to
#
# 5) ANSWER: V + E
#   EXPLANATION: The algorithm is to find all of the vertices reachable from s
#     using only forward edges that aren't full or backwards edges that aren't
#     empty. This can be done in linear time using either breadth-first search
#     or depth-first search.
#
# 6) ANSWER: integer (not rational number, real number, imaginary number)
#   EXPLANATION: The integrality theorem asserts that there exists a maxflow in which 
#   the flow on each edge is an integer. This impolies that the value of the
#   maxflow is an integer.
#
# 7) ANSWER:e = v -> w is either a forward edge that is not full or a backward edge that is not empty.
#   EXPLANATION: e = v -> w is an edge in the residual graph, which means that either it is
#   a forward edge that is not full or a backward edge that is not empty.
#
# 8) ANSWER: N
#   EXPLANATION: For general networks, the shortest augmenting path heuristic 
#   requires (1/2)*EV augmenting paths to find a maxflow in a network with V
#   vertices and E edges. However, in the bipartite matching reduction, all edge
#   capacities are 1 and the value of the maximum flow is at most N. Thus, at
#   most N augmenting paths are needed (since each augmenting path delivers 1 unit of flow to t).
#
#   We note that a more refined version of the shortest augmenting path heuristic 
#   leads to an overall running time of E*sqrt(V) for the bipartite matching problem.
#
# 9) ANSWER: N^2 and N^2                      (N-1)
#   EXPLANATION: There are N-1 team vertices, ( 2 ) (N-1 CHOOSE 2) game vertices, 1 source, and 1 sink.
#   In the worst case, there are 2*(N-1 CHOOSE 2) edges from game vertices to team vertices
#   (2 for each game vertex), (N-1 CHOOSE 2) edges pointing from the source, and N-1
#   edges pointing to the sink.

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port

