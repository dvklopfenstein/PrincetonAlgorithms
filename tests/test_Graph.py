#!/usr/bin/env python

from AlgsSedgewickWayne.Graph import Graph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin

import sys

def run(a, prt=sys.stdout):
  g = Graph(a)
  prt.write("{}\n".format(g))
  g.wr_png("Graph_test_0.png")

def test_0(prt=sys.stdout):
  run(cli_get_fin("../thirdparty/tinyG.txt"))

def test_1(prt=sys.stdout):
  adjtxtblk = """
    A:  E B 
    B:  E A F 
    C:  D F 
    D:  C G H 
    E:  A B 
    F:  C G B 
    G:  D H F 
    H:  G D """
  # Convert adjacency list in text block to array, fmt=[V, E, edge_pairs]
  g = Graph(adjtxt=adjtxtblk)
  prt.write("{}\n".format(g))
  g.wr_png("Graph_test_1.png")

def run_all():
  test_0()
  test_1()

if __name__ == '__main__':
  #run_all()
  test_1()
