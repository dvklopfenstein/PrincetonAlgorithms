#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Graph import Graph
from AlgsSedgewickWayne.BreadthFirstPaths import BreadthFirstPaths
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin


def test_0(prt=sys.stdout):
  """Test BFS using Graph from file represented with ints."""
  prt.write("\ntest_0: BFS using Graph with ints\n")
  L = len(sys.argv[1:])
  g = cli_get_fin(sys.argv[1] if L != 0 else "../thirdparty/tinyCG.txt")
  G = Graph(g)
  prt.write(str(G))

  s = int(sys.argv[2]) if L > 1 else 0
  bfs = BreadthFirstPaths(G, s)

  for v in range(G.V()):
    if bfs.hasPathTo(v):
      prt.write("{} to {} ({}):  ".format(s, v, bfs.distTo(v)))
      for x in reversed(bfs.pathTo(v)):
        if x == s: prt.write(str(x))
        else:      prt.write("-{}".format(x))
      prt.write("\n")

    else:
      prt.write.printf("{} to {} (-):  not connected\n".format(s, v))


def test_1(prt=sys.stdout):
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

def run_all(prt=sys.stdout):
  test_0()
  test_1()

if __name__ == '__main__':
  run_all()
