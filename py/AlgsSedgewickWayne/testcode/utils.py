
import sys

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


