
import sys

def run_unions(alg, union_txt, msg, prt=sys.stdout):
  """Test user-created sets of union instructions."""
  prt.write("{MSG}\n".format(MSG=msg))
  prt.write("{NODES} Initial values\n".format(NODES=alg))
  for U_str in union_txt.split():
    I = [int(intstr) for intstr in U_str.split('-')]
    alg.union(I[0], I[1])
    set_str = ["{L}".format(L=list(s)) for s in alg.get_connected_components()]
    prt.write("{NODES} union({STR}) {SETS}\n".format(
        NODES=alg, STR=U_str, SETS=' '.join(set_str)))
  return alg

def chk_arrays(actual, expected):
  """Test to see if QuickFind passed."""
  if actual == expected:
    return
  raise Exception("TEST FAILED.")


