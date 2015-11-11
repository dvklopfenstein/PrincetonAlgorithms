#!/usr/bin/env python
"""Test Topological data type."""
# TBD Finich Python port

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

import sys


from AlgsSedgewickWayne.SymbolDigraph import SymbolDigraph
from AlgsSedgewickWayne.Topological import Topological

def main(prt=sys.stdout):
  filename  = sys.argv[1]
  delimiter = sys.argv[2]
  sg = SymbolDigraph(filename, delimiter)
  topological = Topological(sg.G())
  for v in topological.order():
    prt.write(sg.name(v))

if __name__ == '__main__':
  main()

