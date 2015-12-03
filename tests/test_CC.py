#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.CC import CC
from AlgsSedgewickWayne.Graph import Graph
import collections as cx
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_fin
import inspect
import collections as cx


def test_0(prt=sys.stdout):
  L = len(sys.argv[1:])
  g = cli_get_fin(sys.argv[1] if L != 0 else "../thirdparty/tinyG.txt")
  G = Graph(g)
  cc = CC(G)

  # number of connected components
  M = cc.count()
  prt.write("{M} components\n".format(M=M))

  # compute list of vertices in each connected component
  components = [cx.deque() for i in range(M)]
  for v in range(G.V()):
    components[cc.id(v)].append(v) # enqueue(v)

  # print results
  for i in range(M):
    for v in components[i]:
      prt.write("{v} ".format(v=v))
    prt.write("\n")

def test_1(prt=sys.stdout):
  txtblk = """
    A:  F B 
    B:  F A 
    C:  G 
    D:  I E J H 
    E:  D J 
    F:  A B 
    G:  C 
    H:  I D 
    I:  D H J 
    J:  D I E 
  """
  G = Graph(adjtxt=txtblk)
  cc = CC(G)
  cc.prt_ids(prt)
  prt.write("\n{}\n".format(G))

def cli():
  N = len(sys.argv)
  if N == 1:
    test_0()
  elif N == 2:
    fnc_to_run = sys.argv[1]
    module = sys.modules[__name__]
    name2fnc = cx.OrderedDict(inspect.getmembers(module, inspect.isfunction))
    fnc = name2fnc.get(fnc_to_run, None)
    if fnc:
      fnc()
    else:
      raise Exception("{} NOT PRESENT IN: {}".format(
        fnc_to_run, ' '.join(name2fnc.keys())))

if __name__ == '__main__':
  cli()
