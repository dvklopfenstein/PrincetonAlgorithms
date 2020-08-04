#!/usr/bin/env python3
"""Plot tiny graph"""

import sys
from os.path import join
from os.path import dirname
from os.path import abspath
from AlgsSedgewickWayne.Graph import Graph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin

TEST_DIR = dirname(abspath(__file__))


def main(prt=sys.stdout):
    """Plot tiny graph"""
    fin_graphs = ['tinyG.txt', 'mediumG.txt']
    for fin_graph in fin_graphs:
        graph = Graph(cli_get_fin(join(TEST_DIR, fin_graph)))
        prt.write("{}\n".format(graph))
        fout_png = fin_graph.replace('txt', 'png')
        graph.wr_png(fout_png)


if __name__ == '__main__':
    main()
