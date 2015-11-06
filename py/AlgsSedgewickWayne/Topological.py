"""Compute topological ordering of a DAG or edge-weighted DAG. Runs in O(E + V) time."""

#*****************************************************************************
 #  Execution:    java  Topological filename.txt separator
 #  Dependencies: Digraph.java DepthFirstOrder.java DirectedCycle.java
 #                EdgeWeightedDigraph.java EdgeWeightedDirectedCycle.java
 #                SymbolDigraph.java
 #  Data files:   http://algs4.cs.princeton.edu/42digraph/jobs.txt
 #
 #
 #  % java Topological jobs.txt "/"
 #  Calculus
 #  Linear Algebra
 #  Introduction to CS
 #  Programming Systems
 #  Algorithms
 #  Theoretical CS
 #  Artificial Intelligence
 #  Machine Learning
 #  Neural Networks
 #  Robotics
 #  Scientific Computing
 #  Computational Biology
 #  Databases
 #
 #
 #*****************************************************************************/
#*
 #  The <tt>Topological</tt> class represents a data type for 
 #  determining a topological order of a directed acyclic graph (DAG).
 #  Recall, a digraph has a topological order if and only if it is a DAG.
 #  The <em>hasOrder</em> operation determines whether the digraph has
 #  a topological order, and if so, the <em>order</em> operation
 #  returns one.
 #  <p>
 #  This implementation uses depth-first search.
 #  The constructor takes time proportional to <em>V</em> + <em>E</em>
 #  (in the worst case),
 #  where <em>V</em> is the number of vertices and <em>E</em> is the number of edges.
 #  Afterwards, the <em>hasOrder</em> and <em>rank</em> operations takes constant time;
 #  the <em>order</em> operation takes time proportional to <em>V</em>.
 #  <p>
 #  See {@link DirectedCycle}, {@link DirectedCycleX}, and
 #  {@link EdgeWeightedDirectedCycle} to compute a
 #  directed cycle if the digraph is not a DAG.
 #  See {@link TopologicalX} for a nonrecursive queue-based algorithm
 #  to compute a topological order of a DAG.
 #  <p>
 #  For additional documentation,
 #  see <a href="http://algs4.cs.princeton.edu/42digraph">Section 4.2</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne

class Topological(object):
  """Determines if digraph G has a topological order and, if so, finds topological order."""
  private Iterable<Integer> order;  # topological order
  private int[] rank;               # rank[v] = position of vertex v in topological order

  def __init__(self, G): # G is Digraph
    DirectedCycle finder = new DirectedCycle(G)
    if not finder.hasCycle()):
        DepthFirstOrder dfs = new DepthFirstOrder(G)
        self._order = dfs.reversePost()
        self._rank = new int[G.V()]
        i = 0
        for (int v : order)
            rank[v] = i += 1

  def Topological(EdgeWeightedDigraph G): # EdgeWeightedDigraph
    """Determines if digraph G has a topological order and, if so, finds topological order."""
    EdgeWeightedDirectedCycle finder = new EdgeWeightedDirectedCycle(G)
    if not finder.hasCycle():
        DepthFirstOrder dfs = new DepthFirstOrder(G)
        order = dfs.reversePost()

  # Returns a topological order if the digraph has a topologial order, None otherwise
  def order(self): return self._order

  # Does the digraph have a topological order?
  def hasOrder(self): return self.order is not None

  def rank(self, v):
    """The the rank of vertex v in the topological order; -1 if the digraph is not a DAG."""
    self._validateVertex(v)
    if hasOrder()) return rank[v]
    else:            return -1

  def _validateVertex(self, v):
    """raise an IndexOutOfBoundsException unless 0 <= v < V."""
    V = len(rank)
    if v < 0 or v >= V:
        raise Exception("vertex {} is not between 0 and {}".format(v, (V-1))

    #*
     # Unit tests the <tt>Topological</tt> data type.
     #/
  def main(String[] args):
      String filename  = args[0]
      String delimiter = args[1]
      SymbolDigraph sg = new SymbolDigraph(filename, delimiter)
      Topological topological = new Topological(sg.G())
      for (int v : topological.order()):
          prt.write(sg.name(v))


# Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
# Copyright 2002-2015, DV Klopfenstein, Python port
