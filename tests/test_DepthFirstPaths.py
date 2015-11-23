#!/usr/bin/env python

from AlgsSedgewickWayne.testcode.utils  import adjtxtblk2arr_ud
from AlgsSedgewickWayne.Graph           import Graph
from AlgsSedgewickWayne.DepthFirstPaths import DepthFirstPaths
import sys

def test_0(prt=sys.stdout):
  txtblk = """
    A:  F B E 
    B:  F A 
    C:  G F 
    D:  H G 
    E:  A 
    F:  G A B C 
    G:  F C D 
    H:  D 
  """
  adj, i2v = adjtxtblk2adj(txtblk)
  G = Graph(adj, i2v)
  dfs = DepthFirstPaths(G, 0, prt)
  prt.write("{}\n".format(G))
  

if __name__ == '__main__':
  test_0()
