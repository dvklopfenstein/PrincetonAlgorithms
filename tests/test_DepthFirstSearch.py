#!/usr/bin/env python3
"""Unit tests DepthFirstSearch data type"""

import sys
from os.path import join
from os.path import dirname
from os.path import abspath
from AlgsSedgewickWayne.Graph import Graph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin
from AlgsSedgewickWayne.DepthFirstSearch import DepthFirstSearch

TEST_DIR = dirname(abspath(__file__))


def test_depthfirstsearch():
    """Unit tests DepthFirstSearch data type"""
    ## fin_graph = "mediumG.txt"
    fin_graph = "tinyG.txt"
    graph_array = cli_get_fin(join(TEST_DIR, fin_graph))
    ## print(graph_array)
    graph = Graph(graph_array)

    # Run test from main in algs4/DepthFirstSearch.java
    #     % java DepthFirstSearch tinyG.txt 0
    #     0 1 2 3 4 5 6
    #     NOT connected
    #
    #     % java DepthFirstSearch tinyG.txt 9
    #     9 10 11 12
    #     NOT connected
    if len(sys.argv) == 1:
        results_0 = _run(graph, src_node=0)
        results_9 = _run(graph, src_node=9)
        if fin_graph == 'tinyG.txt':
            assert results_0 == [0, 1, 2, 3, 4, 5, 6]
            assert results_9 == [9, 10, 11, 12]

    # Run user tests from the command-line
    else:
        for src_node in sys.argv[1:]:
            if src_node.isdigit():
                _run(graph, int(src_node))


def _run(graph, src_node):
    """Run the depth first search"""
    nodes_connected = []
    dfsobj = DepthFirstSearch(graph, src_node)
    for node_v in range(graph.num_nodes()):
        if dfsobj.marked[node_v]:
            nodes_connected.append(node_v)

    # Is this a fully connected Graph
    num_connected = len(nodes_connected)
    assert num_connected == dfsobj.count()
    print('Node {SRC} is connected to {N} nodes: {DSTs}'.format(
        SRC=src_node, N=num_connected,
        DSTs=' '.join(str(n) for n in sorted(nodes_connected))))
    if dfsobj.count() != graph.num_nodes():
        print("NOT connected\n")
    else:
        print("connected\n")
    return nodes_connected


if __name__ == '__main__':
    test_depthfirstsearch()
