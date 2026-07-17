#!/usr/bin/env python3

from AlgsSedgewickWayne.Digraph import Digraph
#from AlgsSedgewickWayne.DepthFirstOrder import DepthFirstOrder
from tests.pkgtest.utils import get_array

def test_depth_first_order():
    _run('tests/tinyDAG.txt')
    _run('tests/tinyDG.txt')

def _run(fin_dag):
    arr = get_array(fin_dag)
    dag = Digraph(arr)
    print(f'DAG: {fin_dag}')
    print(dag)

    #dfs = DepthFirstOrder(dag)
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

    #print("Reverse postorder: ", end="")
    #for (int v : dfs.reversePost()) {
    #    print(v + " ", end="")
    #}
    #print("")


if __name__ == '__main__':
    test_depth_first_order()


# Copyright 2002, Robert Sedgewick and Kevin Wayne.
# Copyright 2026, DV Klopfenstein, Python port
