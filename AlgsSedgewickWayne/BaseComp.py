"""Component Base which holds functions to aid in visulaization and understanding."""

# Copyright (C) 2014-present DV Klopfenstein, PhD. All rights reserved.

from collections import defaultdict
from collections import namedtuple
from collections import Counter
import sys
import pydot
from AlgsSedgewickWayne.testcode.utils import get_png_label

class BaseComp(object):
    """ Holds an index of Nodes which can be combined into components."""

    NtRoot = namedtuple("NtRoot", "rootnode depth")

    def __init__(self, name):
        """Derived class will set the actual values."""
        self.name = name
        self.idvals = None

    def _root(self, val):
        """Shows _root interface."""
        raise NotImplementedError(f"TIME TO IMPLEMENT "
            f"A _root({val}) METHOD IN THE DERIVED CLASS")

    def __str__(self):
        """Print the ID vector. Used in    >>> print obj"""
        idxs = " ".join(f"{e:>2}" for e in range(len(self.idvals)))
        vals = " ".join(f"{e:>2}" for e in self.idvals)
        # vals += " ROOTS: " + ' '.join(f"{v}" for v in sorted(set(self.idvals)))
        return '\n'.join(["ROOT: " + vals, "ID:   " + idxs])

    def get_connected_components(self):
        """Return the root and a list of the contents of each component."""
        root2members = defaultdict(set)
        for id_val, parent in enumerate(self.idvals):
            root2members[self._root(parent)].add(id_val)
        return root2members

    def wr_png(self, fout_png="components.png", prt=sys.stdout, **kwargs):
        """Make a png showing a diagram of the connected components."""
        label = get_png_label(self.idvals, kwargs)
        # 1. Create/initialize Graph
        digraph = pydot.Dot(label=label, graph_type='digraph') # Directed Graph
        # 2. Create Nodes
        nodes = [pydot.Node(str(idx)) for idx in range(len(self.idvals))]
        # 3. Add nodes to Graph
        for node in nodes:
            digraph.add_node(node)
        # 4. Add Edges between Nodes to Graph
        for child, parent in enumerate(self.idvals):
            if child != parent: # Print only edges from one node to another (not to self)
                digraph.add_edge(pydot.Edge(nodes[parent], nodes[child]))
        # 5. Write Graph to png file
        digraph.write_png(fout_png)
        prt.write(f"    WROTE: {fout_png}\n")

    def union_pngs(self, unions, png_base):
        """Do a union, draw a state image. Repeat."""
        for i, (pval, qval) in enumerate(unions):
            fout_png = f"{png_base}{i}.png"
            self.union_png(pval, qval, fout_png)

    def union_png(self, pval, qval, fout_png):
        """Do a union, draw a state image."""
        self.union(pval, qval)
        if fout_png is not None:
            label_pat = f"union({pval}, {qval}) -> {{STATE}}"
            self.wr_png(fout_png, label_pat=label_pat)

    def union(self, pval, qval):
        """Derived class should do union"""
        raise RuntimeError('DERIVED CLASS MUST CALL UNION')

    def get_png(self):
        """Generate a png filename."""
        state = "_".join([str(s) for s in self.idvals])
        return f"state_{self.name}_{state}.png"

    def wr_png_tree_state(self, state=None, fout_png=None):
        """Force state (e.g. [0, 9, 6, 5, 4, 2, 6, 1, 0, 5]), create png showing current state."""
        self.idvals = state
        if fout_png is None:
            fout_png = self.get_png()
        self.wr_png(fout_png)

    def wr_png_tree_statestr(self, statestr=None, fout_png=None):
        """Given state string (e.g. "0 9 6 5 4 2 6 1 0 5"), create png showing current state."""
        usr_state = [int(n) for n in statestr.split()]
        self.wr_png_tree_state(usr_state, fout_png)
