"""Utilities for Binary Heaps."""

import sys
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array
from AlgsSedgewickWayne.testcode.utils import get_png_label

def wr_png(bh_arrstr, **kwargs):
  wr_png_array(cli_get_array(bh_arrstr), kwargs)
  
def wr_png_array(bh_st, kwargs):
  """Given an array for a binary heap, draw tree."""
  import pydot
  prt = sys.stdout if 'prt' not in kwargs else kwargs['prt']
  fout_png = "binary_heap_{}.png".format('_'.join(str(e) for e in bh_st))
  label = get_png_label(bh_st, kwargs)
  # 1. Create/initialize Graph
  G = pydot.Dot(label=label, graph_type='digraph') # Directed Graph
  edge_idxs = get_edges(bh_st)
  badcol = {c:'#fe2f4a' for p, c in edge_idxs if bh_st[p] < bh_st[c]}
  # 2. Create Nodes
  mknode = lambda i, v: pydot.Node(
    "{V}[{I}]".format(I=i+1, V=v), 
    style = "filled",
    fillcolor = badcol.get(i, "beige"))
  nodes = [mknode(i,v) for i, v in enumerate(bh_st) if v is not None]
  # 3. Add nodes to Graph
  for node in nodes:
    G.add_node(node)
  # 4. Add Edges between Nodes to Graph
  for p, c in edge_idxs:
    G.add_edge(pydot.Edge(nodes[p], nodes[c]))
  # 5. Write Graph to png file
  G.write_png(fout_png)
  prt.write("  WROTE: {}\n".format(fout_png))

def get_edges(arr):
  """Return list of edges in binary heap."""
  edges = []
  L = len(arr)
  for k in range(1, L+1):
    k_a = 2*k
    if k_a > L: break
    edges.append((k-1, k_a-1))
    k_b = k_a + 1
    if k_b > L: break
    edges.append((k-1, k_b-1))
  return edges

