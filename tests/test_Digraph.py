#!/usr/bin/env python

import sys
from os.path import join
from os.path import dirname
from os.path import abspath
from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin

TEST_DIR = dirname(abspath(__file__))


def test_main(prt=sys.stdout):
  g = cli_get_fin(sys.argv[1] if len(sys.argv) != 1 else join(TEST_DIR, "tinyDG.txt"))
  G = Digraph(g)
  prt.write("{}\n".format(G))

def test_lecture(prt=sys.stdout):
  """Plot tinyDG2.txt from 'Diagraph Search' Coursera Algs2 lecture."""
  g = cli_get_fin(join(TEST_DIR, "tinyDG2.txt"))
  G = Digraph(g)
  prt.write("{}\n".format(G))
  G.wr_png("Digraph_lecture.png", prt)

def run_all(prt=sys.stdout):
  test_main(prt)
  test_lecture(prt)


if __name__ == '__main__':
  #run_all()
  test_lecture()
