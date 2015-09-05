"""Component Base which holds functions to aid in visulaization and understanding."""

# Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved.

import collections as cx
import sys

class BaseComp(object):
  """ Holds an index of Nodes which can be combined into components."""

  def __init__(self, name):
    """Derived class will set the actual values."""
    self.name = name
    self.ID = None

  def _root(self, p):
    """Shows _root interface."""
    raise Exception("TIME TO IMPLEMENT A _root({P}) METHOD IN THE DERIVED CLASS".format(P=p))

  def __str__(self):
    """Print the ID vector. Used in  >>> print obj"""
    idxs = " ".join("{IDX:>2}".format(IDX=e) for e in range(len(self.ID)))
    vals = " ".join("{VAL:>2}".format(VAL=e) for e in self.ID)
    #prt = ['']*len(self.ID)
    #for i in self.ID:
    #  if self.ID[i] == i:
    #    prt[i] = '-'
    #for i,v in enumerate(prt):
    #  print v, i
    return '\n'.join(["IDX: " + idxs, "val: " + vals])

  def get_connected_components(self):
    """Return a list of the contents of each component."""
    roots = cx.defaultdict(set)
    for ID, parent in enumerate(self.ID):
      roots[self._root(parent)].add(ID)
    return list(roots.values())

  def wr_png(self, fout_png="components.png", prt=sys.stdout):
    """Make a png showing a diagram of the connected components."""
    import pydot
    # 1. Create/initialize Graph
    G = pydot.Dot(graph_type='digraph') # Directed Graph
    # 2. Create Nodes
    nodes = [pydot.Node(str(idx)) for idx in range(len(self.ID))]
    # 3. Add nodes to Graph
    for node in nodes:
      G.add_node(node)
    # 4. Add Edges between Nodes to Graph
    for child, parent in enumerate(self.ID):
      if child != parent: # Print only edges from one node to another (not to self)
        G.add_edge(pydot.Edge(nodes[parent], nodes[child]))
    # 5. Write Graph to png file
    G.write_png(fout_png)
    prt.write("  WROTE: {}\n".format(fout_png))

  def wr_png_tree_state(self, state=None, fout_png=None):
    """Set the state and write a png showing tree image of the state."""
    # Expecting state is an ID array. e.g. state=[0, 9, 6, 5, 4, 2, 6, 1, 0, 5]
    self.ID = state
    if fout_png is None:
      fout_png = "state_{NAME}_{STATE}.png".format(
          NAME = self.name,
          STATE = "_".join([str(s) for s in state]))
    self.wr_png(fout_png)



