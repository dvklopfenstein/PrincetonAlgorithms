
import sys
import re
import collections as cx

def run_unions(alg, union_txt, msg, pngbase=None, prt=sys.stdout):
  """Test user-created sets of union instructions."""
  prt.write("{MSG}\n".format(MSG=msg))
  prt.write("{NODES} Initial values\n".format(NODES=alg))
  for idx, U_str in enumerate(union_txt.split()):
    I = [int(intstr) for intstr in U_str.split('-')]
    fout_png = None if pngbase is None else "{}_step{}.png".format(pngbase, idx)
    alg.union_png(I[0], I[1], fout_png)
    set_str = ["{L}".format(L=list(s)) for s in alg.get_connected_components()]
    prt.write("{NODES} union({STR}) {SETS}\n".format(
        NODES=alg, STR=U_str, SETS=' '.join(set_str)))
  return alg

def get_unions(union_txt):
  """Given str('4-5 6-7 3-4'), return unions."""
  unions = []
  for idx, U_str in enumerate(union_txt.split()):
    I = [int(intstr) for intstr in U_str.split('-')]
    unions.append(I)

def chk_arrays(actual, expected):
  """Test to see if QuickFind passed."""
  if actual == expected:
    return
  sys.stdout.write("EXPECTED: {EXP}\n".format(EXP=expected))
  sys.stdout.write("ACTUAL:   {ACT}\n".format(ACT=actual))
  raise Exception("TEST FAILED.")

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
    prt.write("{ARRAY_ID} {ELEM_IDX:>2} {ELEM} {STARS}\n".format(
      ARRAY_ID=array_id, ELEM_IDX=elem_position, ELEM=elem, STARS='*'*elem2num[elem]))
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

# -------------------------------------------------------------
# Adjacency-list utilities

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
  return cx.OrderedDict(lst)

def adjOrderedDict2VEpairs_ud(od):
  """For Undirected Graph: Convert an adj list into an array of fmt: [V, E, pairs] & names."""
  # Note: the format, "V E pairs" is seen in tinyG.txt
  V = len(od)
  v2i = {v:i for i, v in enumerate(od.keys())} # Vertex name to index
  i2v = {i:v for v, i in v2i.items()}
  edges = set([tuple(sorted([v2i[a], v2i[b]])) for a, bs in od.items() for b in bs])
  a = [V, len(edges)] + list(edges)
  return a, i2v

def _adjstr2arr(adjstr):
  """Convert "A:  F B E" to ('A', ('F', 'B', 'E'))."""
  M = re.search(r'^(\S+)\s*:\s*(\S.*)$', adjstr)
  if M:
    return (M.group(1), M.group(2).split())
  raise Exception("NO ADJACENCY LIST FOUND IN({})".format(adjstr))





