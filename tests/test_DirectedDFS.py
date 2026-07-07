#!/usr/bin/env python3
"""Determine single-source or multiple-source reachability in a digraph"""

import sys
import os.path as op
from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.DirectedDFS import DirectedDFS
from tests.pkgtest.utils import get_array


def test_directed_dfs():
    """Determine single-source or multiple-source reachability in a digraph
    using depth first search.
    Runs in O(E + V) time.

    >>> _run_file("tests/tinyDG.txt", 1)
    [1]

    >>> _run_file("tests/tinyDG.txt", 2)
    [0, 1, 2, 3, 4, 5]

    >>> _run_file("tests/tinyDG.txt", 1, 2, 6)
    [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
    """
    assert _run_file("tests/tinyDG.txt", 1) == [1]
    assert _run_file("tests/tinyDG.txt", 2) == [0, 1, 2, 3, 4, 5]
    assert _run_file("tests/tinyDG.txt", 1, 2, 6) == [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
    print('PASSED')


def _run_file(fin_grph, *sources):
    print('FILENAME:', fin_grph)
    print('SOURCES:', sources)
    digraph_arr = get_array(fin_grph)
    #print('DIGRAPH ARRAY:', digraph_arr)
    return _run_arr(digraph_arr, *sources)

def _run_arr(digraph_arr, *sources):
    grph = Digraph(digraph_arr)
    dfs = DirectedDFS(grph, sources) # multiple-source reachability
    return [v for v in grph.keys if dfs.marked(v)]


def cli():
    """Command-line interface"""
    if len(sys.argv) == 1:
        test_directed_dfs()
    else:
        fin_digraph = sys.argv[1]
        assert op.exists(fin_digraph)
        # read in sources from command-line arguments
        sources = [int(s) for s in sys.argv[2:]]
        # print out vertices reachable from sources
        # reachable = test_directed_dfs(digraph_array, *sources)
        reachable = _run_file(fin_digraph, *sources)
        print(' '.join(str(r) for r in reachable))


#****************************************************************************
if __name__ == "__main__":
    cli()

# Copyright 2002, Robert Sedgewick and Kevin Wayne.
# Copyright 2015, DV Klopfenstein, Python implementation.
