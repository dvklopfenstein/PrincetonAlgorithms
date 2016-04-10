"""Functions to plot a Binary Search Tree."""

import pydot

__copyright__ = "Copyright (C) 2016, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

# -- Graphing of a Binary Search Tree (BST) ---------------------------------
def wr_png(fout_png, nodes_bst, childnames, log):
    """Save tree figure to png file."""
    # 1. create/initialize graph
    g = pydot.Dot(graph_type='digraph') # directed graph
    # 2. create pydot Nodes
    nodes_dot = _get_dotnodes(nodes_bst, childnames)
    # 3. add nodes to graph
    for dotnode in nodes_dot:
        g.add_node(dotnode)
    # 4. add edges between nodes to graph
    edges_dot = _get_dotedges(nodes_bst, childnames)
    for dotedge in edges_dot:
        g.add_edge(dotedge)
    # 5. write graph to png file
    g.write_png(fout_png)
    log.write("  wrote: {}\n".format(fout_png))

def _get_dotnodes(nodes_bst, childnames):
    """Get a list of pydot Nodes."""
    nodes_dot = []
    for bstnode in nodes_bst:
        # Add nodes in the bst
        nodes_dot.append(pydot.Node(str(bstnode)))
        # Add null child nodes (e.g., key_right, key_left)
        for rl in childnames.keys():
            if getattr(bstnode, rl) is None:
                null_child = _get_name_nullchild(bstnode, rl)
                nodes_dot.append(pydot.Node(null_child, style='invis'))
    return nodes_dot

def _get_dotedges(nodes_bst, childnames):
    """Get a list of pydot Edges."""
    edges_dot = []
    for bstnode in nodes_bst:
        for cname, color in childnames.items():
            child_node = getattr(bstnode, cname)
            if child_node is not None:
                edges_dot.append(pydot.Edge(str(bstnode), str(child_node), color=color))
            else:
                null_child = _get_name_nullchild(bstnode, cname)
                edges_dot.append(pydot.Edge(str(bstnode), null_child, style='invis'))
    return edges_dot

def _get_name_nullchild(src_node, lr):
    """Get a name for a Null child node."""
    return "{SRC}_{LR}".format(SRC=src_node.key, LR=lr)

# -- Utilities --------------------------------------------------------------
def sort_balbst(key_vals):
    """Given a list of (key, value) tuples, return list sorted to build a balanced BST."""
    list_sorted = sorted(key_vals)
    list_balanced = []
    _sort_balbst(list_balanced, list_sorted)
    return list_balanced

def _sort_balbst(balanced_bst, sorted_list):
    """Given a sorted list, return a list in an order to create a balanced BST."""
    if not sorted_list: # sorted list
        return
    middle = len(sorted_list)/2
    balanced_bst.append(sorted_list[middle])
    _sort_balbst(balanced_bst, sorted_list[:middle])   # Process left side
    _sort_balbst(balanced_bst, sorted_list[middle+1:]) # Process right side

# Copyright (C) 2016, DV Klopfenstein. All rights reserved.
