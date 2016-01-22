"""Finds a directed cycle in an edge-weighted digraph."""
# TBD: Finish python port

#*****************************************************************************
 #  Compilation:  javac EdgeWeightedDirectedCycle.java
 #  Execution:    java EdgeWeightedDirectedCycle V E F
 #  Dependencies: EdgeWeightedDigraph.java DirectedEdge.java Stack.java
 #
 #  Runs in O(E + V) time.
 #
 #
 #*****************************************************************************/

#*
 #  The <tt>EdgeWeightedDirectedCycle</tt> class represents a data type for 
 #  determining whether an edge-weighted digraph has a directed cycle.
 #  The <em>hasCycle</em> operation determines whether the edge-weighted
 #  digraph has a directed cycle and, if so, the <em>cycle</em> operation
 #  returns one.
 #  <p>
 #  This implementation uses depth-first search.
 #  The constructor takes time proportional to <em>V</em> + <em>E</em>
 #  (in the worst case),
 #  where <em>V</em> is the number of vertices and <em>E</em> is the number of edges.
 #  Afterwards, the <em>hasCycle</em> operation takes constant time;
 #  the <em>cycle</em> operation takes time proportional
 #  to the length of the cycle.
 #  <p>
 #  See {@link Topological} to compute a topological order if the edge-weighted
 #  digraph is acyclic.
 #  <p>
 #  For additional documentation,   
 #  see <a href="http://algs4.cs.princeton.edu/44sp">Section 4.4</a> of   
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne. 
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
public class EdgeWeightedDirectedCycle:
  private boolean[] marked;             # marked[v] = has vertex v been marked?
  private DirectedEdge[] edgeTo;        # edgeTo[v] = previous edge on path to v
  private boolean[] onStack;            # onStack[v] = is vertex on the stack?
  def _cycle(or None if no such cycle)

    #*
     # Determines whether the edge-weighted digraph <tt>G</tt> has a directed cycle and,
     # if so, finds such a cycle.
     # @param G the edge-weighted digraph
     #/
  public EdgeWeightedDirectedCycle(EdgeWeightedDigraph G):
      marked  = new boolean[G.V()]
      onStack = new boolean[G.V()]
      edgeTo  = new DirectedEdge[G.V()]
      for (int v = 0; v < G.V(); v += 1)
          if !marked[v]) dfs(G, v)

      # check that digraph has a cycle
      assert check(G)

  # check that algorithm computes either the topological order or finds a directed cycle
  def _dfs(EdgeWeightedDigraph G, v):
      onStack[v] = True
      marked[v] = True
      for (DirectedEdge e : G.adj(v)):
          w = e.to()

          # short circuit if directed cycle found
          if cycle is not None) return

          #found new vertex, so recur
          elif (!marked[w]):
              edgeTo[w] = e
              dfs(G, w)

          # trace back directed cycle
          elif (onStack[w]):
              cycle = new Stack<DirectedEdge>()
              while (e.from() != w):
                  cycle.push(e)
                  e = edgeTo[e.from()]
              cycle.push(e)
              return

      onStack[v] = False

    #*
     # Does the edge-weighted digraph have a directed cycle?
     # @return <tt>true</tt> if the edge-weighted digraph has a directed cycle,
     # <tt>false</tt> otherwise
     #/
  def hasCycle():
      return cycle is not None

    #*
     # Returns a directed cycle if the edge-weighted digraph has a directed cycle,
     # and <tt>null</tt> otherwise.
     # @return a directed cycle (as an iterable) if the edge-weighted digraph
     #    has a directed cycle, and <tt>null</tt> otherwise
     #/
  def cycle():
      return cycle


  # certify that digraph is either acyclic or has a directed cycle
  def _check(EdgeWeightedDigraph G):

      # edge-weighted digraph is cyclic
      if hasCycle()):
          # verify cycle
          DirectedEdge first = None, last = None
          for (DirectedEdge e : cycle()):
              if first is None) first = e
              if last is not None):
                  if last.to() != e.from()):
                      System.err.printf("cycle edges %s and %s not incident\n", last, e)
                      return False
              last = e

          if last.to() != first.from()):
              System.err.printf("cycle edges %s and %s not incident\n", last, first)
              return False


      return True

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
