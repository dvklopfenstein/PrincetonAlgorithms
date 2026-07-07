#!/usr/bin/env python
"""Test Digraph from lecture or provided by user"""

import sys
import os.path as op
from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.plot.Digraph import PlotDigraph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin
from tests.pkgtest.utils import get_array

TEST_DIR = op.dirname(op.abspath(__file__))


def test_digraph():
    """Test Digraph"""
    #g = cli_get_fin(sys.argv[1] if len(sys.argv) != 1 else op.join(TEST_DIR, "tinyDG.txt"))
    g = cli_get_fin(op.join(TEST_DIR, "tinyDG.txt"))
    digrph = Digraph(g)
    print(digrph)
    exp_outdegree = [2, 0, 2, 2, 2, 1, 4, 2, 1, 2, 1, 2, 1]
    exp_indegree  = [2, 1, 2, 2, 3, 2, 2, 0, 1, 3, 1, 1, 2]
    for vint in range(digrph.num_vertices):
        assert digrph.outdegree(vint) == exp_outdegree[vint]
        assert digrph.indegree(vint) == exp_indegree[vint]
        #print(f'{digrph.indegree(vint)}, ', end="")
    PlotDigraph(digrph).wr_png("Digraph_tinyDG.png")

def test_lecture_digraph():
    """Plot tinyDG2.txt from 'Diagraph Search' Coursera Algs2 lecture."""
    g = cli_get_fin(op.join(TEST_DIR, "tinyDG2.txt"))
    digrph = Digraph(g)
    print(digrph)
    PlotDigraph(digrph).wr_png("Digraph_tinyDG2.png")
    assert digrph.num_vertices == 6
    assert digrph.num_edges == 8

def test_digraph_search():
    """Test Depth-first search in Digraph from lecture, 'Digraph Search'"""
    digrph = Digraph(get_array('tests/tinyDG.txt'))
    print(digrph)

def run_all():
    """Run all tests"""
    test_digraph()
    test_lecture_digraph()


if __name__ == '__main__':
    #run_all()
    test_digraph_search()
    #test_lecture_digraph()
