#!/usr/bin/env python

from sys import stdout
from sys import argv
from os.path import join
from os.path import dirname
from os.path import abspath
from AlgsSedgewickWayne.Graph import Graph
from AlgsSedgewickWayne.BreadthFirstPaths import BreadthFirstPaths
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin

TEST_DIR = dirname(abspath(__file__))


def test_0(prt=stdout):
    """Test BFS using Graph from file represented with ints."""
    prt.write("\ntest_0: BFS using Graph with ints\n")
    ##num_args = len(argv[1:])
    ##g = cli_get_fin(argv[1] if num_args != 0 else join(TEST_DIR, "tinyCG.txt"))
    ##s = int(argv[2]) if num_args > 1 else 0
    s = 0
    g = cli_get_fin(join(TEST_DIR, "tinyCG.txt"))
    G = Graph(g)
    prt.write(str(G))

    bfs = BreadthFirstPaths(G, s)

    for v in range(G.V()):
        if bfs.has_path_to(v):
            prt.write(f"{s} to {v} ({bfs.get_dist_to(v)}):  ")
            for x in reversed(bfs.pathTo(v)):
                if x == s: prt.write(str(x))
                else:      prt.write("-{}".format(x))
            prt.write("\n")

        else:
            prt.write.printf("{} to {} (-):  not connected\n".format(s, v))


def test_1(prt=stdout):
    """Test BFS using Graph from text-block represented with letters."""
    txtblk = """
      A:  E B 
      B:  E A F 
      C:  D F 
      D:  C G H 
      E:  A B 
      F:  C G B 
      G:  D H F 
      H:  G D 
    """
    prt.write("\ntest_1: BFS using Graph with letters\n")
    G = Graph(adjtxt=txtblk)
    bfs = BreadthFirstPaths(G, 'A', prt)
    prt.write("\n{}\n".format(G))

def run_all(prt=stdout):
    test_0()
    test_1()

if __name__ == '__main__':
    run_all()
