#!/usr/bin/env python
"""Test EdgeWeightedGraph"""

from AlgsSedgewickWayne.EdgeWeightedDigraph import EdgeWeightedDigraph
from tests.pkgtest.utils import get_array


def test_edge_weighted_digraph():
    """Test EdgeWeightedGraph"""
    arr = get_array('tests/tinyEWD.txt')

    ewd = EdgeWeightedDigraph(arr)
    txt = str(ewd)
    print(txt)
    print(ewd.indegree)
    print(ewd.adj)
    assert ewd.num_vertices == 8
    assert ewd.num_edges == 30


if __name__ == '__main__':
    test_edge_weighted_digraph()
