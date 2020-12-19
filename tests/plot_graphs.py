#!/usr/bin/env python3
"""Plot tiny graph"""

import sys
from os.path import join
from os.path import dirname
from os.path import abspath
from collections import OrderedDict
from AlgsSedgewickWayne.Graph import Graph
from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin

TEST_DIR = dirname(abspath(__file__))


def main(prt=sys.stdout):
    """Plot tiny graph"""

    fin_graphs = OrderedDict([
        ('tinyG.txt', Graph),
        ('mediumG.txt', Graph),
        ('tinyDG.txt', Digraph),
    ])

    for fin_graph, cls in fin_graphs.items():
        graph = cls(cli_get_fin(join(TEST_DIR, fin_graph)))
        prt.write("Class, {CLS}, has {N} vertices\n".format(
            CLS=type(graph).__name__, N=graph.V()))
        if graph.V() < 30:
            prt.write("{}\n".format(graph))
            fout_png = join(TEST_DIR, 'images', fin_graph.replace('txt', 'png'))
            graph.wr_png(fout_png)


if __name__ == '__main__':
    main()
