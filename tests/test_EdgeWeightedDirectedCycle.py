#/usr/bin/env python
# TBD: Finish Python port

#*****************************************************************************
 #  Compilation:  javac EdgeWeightedDirectedCycle.java
 #  Execution:    java EdgeWeightedDirectedCycle V E F
 #  Dependencies: EdgeWeightedDigraph.java DirectedEdge.java Stack.java
 #
 #  Finds a directed cycle in an edge-weighted digraph.
 #  Runs in O(E + V) time.
 #
 #
 #*****************************************************************************/

import sys

def main(prt=sys.stdout):
  """Unit tests the EdgeWeightedDirectedCycle data type."""

  # create random DAG with V vertices and E edges; then add F random edges
  V = int(sys.argv[1])
  E = int(sys.argv[2])
  F = int(sys.argv[3])
  EdgeWeightedDigraph G = new EdgeWeightedDigraph(V)
  int[] vertices = new int[V]
  for (int i = 0; i < V; i += 1)
      vertices[i] = i
  StdRandom.shuffle(vertices)
  for (int i = 0; i < E; i += 1):
      v, w
      do:
          v = StdRandom.uniform(V)
          w = StdRandom.uniform(V)
      } while (v >= w)
      double weight = StdRandom.uniform()
      G.addEdge(new DirectedEdge(v, w, weight))

  # add F extra edges
  for (int i = 0; i < F; i += 1):
      v = StdRandom.uniform(V)
      w = StdRandom.uniform(V)
      double weight = StdRandom.uniform(0.0, 1.0)
      G.addEdge(new DirectedEdge(v, w, weight))

  prt.write(G)

  # find a directed cycle
  EdgeWeightedDirectedCycle finder = new EdgeWeightedDirectedCycle(G)
  if finder.hasCycle()):
      StdOut.print("Cycle: ")
      for (DirectedEdge e : finder.cycle()):
          StdOut.print(e + " ")
      prt.write()

  # or give topologial sort
  else:
      prt.write("No directed cycle")

if __name__ == '__main__':
  main()
