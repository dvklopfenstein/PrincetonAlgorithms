"""Component Base which holds functions to aid in visulaization and understanding."""

# Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved.

import collections as cx

class BaseComp(object):
  """ Holds an index of Nodes which can be combined into components."""

  def __init__(self):
    """Derived class will set the actual values."""
    self.ID = None

  def _root(self, p):
    """Shows _root interface."""
    raise Exception("TIME TO IMPLEMENT A _root METHOD IN THE DERIVED CLASS")

  def __str__(self):
    """>>> print obj."""
    idxs = " ".join(str(e) for e in range(len(self.ID)))
    vals = " ".join(str(e) for e in self.ID)
    #prt = ['']*len(self.ID)
    #for i in self.ID:
    #  if self.ID[i] == i:
    #    prt[i] = '-'
    #for i,v in enumerate(prt):
    #  print v, i
    return '\n'.join([idxs, vals])

  def get_connected_components(self):
    """Return a list of the contents of each component."""
    roots = cx.defaultdict(set)
    for ID, parent in enumerate(self.ID):
      roots[self._root(parent)].add(ID)
    return list(roots.values())


