#!/usr/bin/env python
"""Test that Graph is implemented properly"""

import sys
from os.path import join
from os.path import dirname
from os.path import abspath
from AlgsSedgewickWayne.Graph import Graph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin

TEST_DIR = dirname(abspath(__file__))


def test_0():
    """Test reading tiny Graph"""
    graph = _run(cli_get_fin(join(TEST_DIR, "tinyG.txt")))
    assert graph.num_nodes == 13
    assert graph.num_edges == 13

def test_1(prt=sys.stdout):
    """Test that Graph is implemented properly"""
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
    graph = Graph(adjtxt=adjtxtblk)
    assert graph.num_nodes == 8
    assert graph.num_edges == 10
    prt.write("{}\n".format(graph))
    graph.wr_png("Graph_test_1.png")

def _run(data, prt=sys.stdout):
    graph = Graph(data)
    prt.write("{}\n".format(graph))
    graph.wr_png("Graph_test_0.png")
    return graph

if __name__ == '__main__':
    test_0()
    test_1()
