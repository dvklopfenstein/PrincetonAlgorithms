
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


