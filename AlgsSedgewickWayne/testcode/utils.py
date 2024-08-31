"""Visualizations"""

__copyright__ = 'Copyright (C) 2016-present, DV Klopfenstein, PhD. All rights reserved'
__author__ = 'DV Klopfenstein, PhD'

import sys
import re
from collections import OrderedDict

def run_unions(alg, union_txt, msg, pngbase=None, prt=sys.stdout):
    """Test user-created sets of union instructions."""
    prt.write(f"{msg}\n")
    prt.write(f"{alg} Initial values: root[member, ...]\n")
    for idx, u_str in enumerate(union_txt.split()):
        i_arr = [int(intstr) for intstr in u_str.split('-')]
        fout_png = None if pngbase is None else f"{pngbase}_step{idx:03}.png"
        alg.union_png(i_arr[0], i_arr[1], fout_png)
        set_str = _str_ccomps(alg)
        prt.write(f"{alg} union({u_str}) {' '.join(set_str)}\n\n")
    return alg

def _str_ccomps(alg):
    """Get a string representation of connected components"""
    ccomps = alg.get_connected_components()
    ## print('TYPE', type(next(iter(ccomps))))
    if isinstance(next(iter(ccomps)), int):
        return [f"{r}{sorted(s)}" for r, s in sorted(ccomps.items(), key=lambda t: t[0])]
    # <class 'AlgsSedgewickWayne.BaseComp.NtRoot'>
    #   assert r.depth == 0
    ## for ntd, members in sorted(ccomps.items(), key=lambda t: t[0]):
    ##     assert
    return [f"R{r.rootnode}{sorted(s)}" for r, s in sorted(ccomps.items(), key=lambda t: t[0])]

def get_unions(union_txt):
    """Given str('4-5 6-7 3-4'), return unions."""
    unions = []
    for u_str in union_txt.split():
        i_arr = [int(intstr) for intstr in u_str.split('-')]
        unions.append(i_arr)

def chk_roots(alg, expected):
    """Test to see if QuickFind passed."""
    actual = [alg._root(i) for i in alg.idvals]
    if actual == expected:
        return
    print(f"EXPECTED: {expected}")
    print(f"ACTUAL:   {actual}")
    raise RuntimeError("TEST FAILED.")

def chk_arrays(actual, expected):
    """Test to see if QuickFind passed."""
    if actual == expected:
        return
    print(f"EXPECTED: {expected}")
    print(f"ACTUAL:   {actual}")
    raise RuntimeError("TEST FAILED.")

def blk_visualizer(blkstr, prt=sys.stdout):
    """Used to help visualize arrays in columns for Algs 1, Week 2 Sort Q2."""
    # Read block text into a list of row elements
    blk = [row.split() for row in blkstr.split('\n') if row]
    # Transpose blk to get a list of column elements
    arrays = zip(*blk)
    # Iterate through each array
    for array_id, arr in enumerate(arrays):
        arr_vis(arr, array_id, 0, prt)

def arr_vis(arr, array_id=0, i0=0, prt=sys.stdout):
    # Get a number, starting with 1, based on the element's order in the sort
    elem2num = {elem:idx for idx, elem in enumerate(sorted(arr), 1)}
    # Iterate through the elements in the current array
    for elem_position, elem in enumerate(arr, i0):
        # Print information about each element in the array
        prt.write(f"{array_id} {elem_position:>2} {elem} {'*'*elem2num[elem]}\n")
    prt.write('\n')

def str_vis(str_arr, array_id=0, prt=sys.stdout):
    arr_vis(str_arr.split(), array_id, prt)

def get_png_label(arr, kwargs):
    """Return label to be used in image."""
    if 'label' in kwargs:
        return kwargs['label']
    pat = "{STATE}"
    if 'label_pat' in kwargs:
        pat = kwargs['label_pat']
    state_str = " ".join([str(e) for e in arr])
    return pat.format(STATE=state_str)

#   -------------------------------------------------------------
#   Adjacency-list utilities

def adjtxtblk2arr_ud(txtblk):
    """Convert an adjacency block into an array for an undirected graph."""
    return adjOrderedDict2VEpairs_ud(adjtxtblk2OrderedDict(txtblk))

def adjtxtblk2OrderedDict(txtblk):
    """Convert a text-block representing an adjacency list into an array."""
    lst = []
    for line in txtblk.splitlines():
        line = line.strip()
        if line:
            lst.append(_adjstr2arr(line))
    return OrderedDict(lst)

def adjOrderedDict2VEpairs_ud(od):
    """For Undirected Graph: Convert an adj list into an array of fmt: [V, E, pairs] & names."""
    # Note: the format, "V E pairs" is seen in tinyG.txt
    num_vertices = len(od)
    v2i = {v:i for i, v in enumerate(od.keys())} # Vertex name to index
    i2v = {i:v for v, i in v2i.items()}
    edges = set(tuple(sorted([v2i[a], v2i[b]])) for a, bs in od.items() for b in bs)
    a = [num_vertices, len(edges)] + list(edges)
    return a, i2v

def _adjstr2arr(adjstr):
    """Convert "A:  F B E" to ('A', ('F', 'B', 'E'))."""
    mtch = re.search(r'^(\S+)\s*:\s*(\S.*)$', adjstr)
    if mtch:
        return (mtch.group(1), mtch.group(2).split())
    raise RuntimeError(f"NO ADJACENCY LIST FOUND IN({adjstr})")


def hl_idnum(idnum, array, bgcolor=0, fgcolor=15):
    """Highlight one idnum in an array"""
    txt = []
    bg = f'48;5;{bgcolor}'
    fg = f'38;5;{fgcolor};1'
    for id_cur in range(len(array)):
        if id_cur != idnum:
            txt.append(f'{id_cur:2}')
        else:
            #txt.append(f"\x1b[48;5;0;{fg_bg};5;{color};1m{id_cur:2}\x1b[0m")
            txt.append(f"\x1b[{bg};{fg}m{id_cur:2}\x1b[0m")
    return ' '.join(txt)

def hl_idroot(idnum, rootvals, bgcolor=0, fgcolor=15):
    """Highlight one idnum in an array"""
    txt = []
    bg = f'48;5;{bgcolor}'
    fg = f'38;5;{fgcolor};1'
    id_root = rootvals[idnum]
    for root_cur in rootvals:
        if root_cur != id_root:
            txt.append(f'{root_cur:2}')
        else:
            #txt.append(f"\x1b[48;5;0;{fg_bg};5;{color};1m{root_cur:2}\x1b[0m")
            txt.append(f"\x1b[{bg};{fg}m{root_cur:2}\x1b[0m")
    return ' '.join(txt)


# Copyright (C) 2016-present, DV Klopfenstein, PhD. All rights reserved.
