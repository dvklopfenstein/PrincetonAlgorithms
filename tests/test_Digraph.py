#!/usr/bin/env python

from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin
import sys

def main(prt=sys.stdout):
  g = cli_get_fin(sys.argv[1] if len(sys.argv) != 1 else "../thirdparty/tinyDG.txt")
  print "GGGGGG", g
  G = Digraph(g)
  prt.write("{}\n".format(G))

def test_lecture(prt=sys.stdout):
  """Plot tinyDG2.txt from 'Diagraph Search' Coursera Algs2 lecture."""
  g = cli_get_fin("../thirdparty/tinyDG2.txt")
  G = Digraph(g)
  prt.write("{}\n".format(G))
  G.wr_png("Digraph_lecture.png", prt)

def run_all(prt=sys.stdout):
  main(prt)
  test_lecture(prt)


if __name__ == '__main__':
  #run_all()
  test_lecture()
