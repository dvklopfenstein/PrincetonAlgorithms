#!/usr/bin/env python

from AlgsSedgewickWayne.Graph import Graph
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array
import sys

def run(a, prt=sys.stdout):
  g = Graph(a)
  prt.write("{}\n".format(g))

if __name__ == '__main__':
  run(cli_get_array(5))
