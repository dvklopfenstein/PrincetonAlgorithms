#!/usr/bin/env python3
"""Test DepthFirstOrder"""

import os.path as op
from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.plot.Digraph import PlotDigraph
from AlgsSedgewickWayne.DepthFirstOrder import DepthFirstOrder
from tests.pkgtest.utils import get_array

def test_depth_first_order(plot=True):
    """Test DepthFirstOrder"""
    _run('tests/tinyDAG.txt', plot)
    #_run('tests/tinyDG.txt', plot)

def _run(fin_dag, plot):
    arr = get_array(fin_dag)
    dag = Digraph(arr)
    if plot:
        PlotDigraph(dag).wr_png(f'Digraph_{op.splitext(op.basename(fin_dag))[0]}.png')
    print(f'DAG: {fin_dag}')
    print(dag)

    dfs = DepthFirstOrder(dag, sort_adj=True)
    #print("   v  pre post")
    #print("--------------")
    #for v in range(dag.num_vertices):
    #    print(f'{v:4} {dfs.pre(v, end="")} {dfs.post(v)}')

    #print("Preorder:  ", end="")
    #for (int v : dfs.pre()) {
    #    print(v + " ", end="")
    #}
    #print("")

    #print("Postorder: ", end="")
    #for (int v : dfs.post()) {
    #    print(v + " ", end="")
    #}
    #print("")

    print("Reverse postorder (topological order): ", dfs.get_reverse_post())  # dfs.reversePost()


if __name__ == '__main__':
    test_depth_first_order()


# Copyright 2002, Robert Sedgewick and Kevin Wayne.
# Copyright 2026, DV Klopfenstein, PhD Python port
