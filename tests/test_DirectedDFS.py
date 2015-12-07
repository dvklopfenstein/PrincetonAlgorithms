#!/usr/bin/env python
# TBD Finish Python port

import sys
from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.DirectedDFS import DirectedDFS
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin

def test_main(g, *sources):
  """Determine single-source or multiple-source reachability in a digraph
  using depth first search.
  Runs in O(E + V) time.

  >>> test_main("tinyDG.txt", 1)
  1

  >>> test_main("tinyDG.txt", 2)
  0 1 2 3 4 5

  >>> test_main("tinyDG.txt", 1, 2, 6)
  0 1 2 3 4 5 6 8 9 10 11 12 
  """
  G = Digraph(g)
  dfs = DirectedDFS(G, *sources) # multiple-source reachability
  return [v for v in G.keys if dfs.marked[v]]


def cli(prt=sys.stdout):
  if len(sys.argv) == 1:
    import doctest    
    doctest.testmod()
  else:
    # read in digraph from command-line argument
    digraph_txt = cli_get_fin(sys.argv[1])
    # read in sources from command-line arguments
    sources = [int(s) for s in sys.argv[2:]]
    print "SSSS", sources
    # print out vertices reachable from sources
    reachable = test_main(digraph_txt, *sources)
    prt.write("{}\n".format(' '.join(str(r) for r in reachable)))


#****************************************************************************
if __name__ == "__main__":
  cli()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

