"""Utilities for running/checking algorithms."""

# ------------------------------------------------------------
# Used in Sort routines
def __lt__(v, w, prt=None): 
  """is v < w ?"""
  if prt is not None:
    prt.write("XXXX {V} < {W} = {LT}\n".format(V=v, W=w, LT=v<w))
  return v < w

def _exch(a, i, j):
  """exchange a[i] and a[j]"""
  a[i], a[j] = a[j], a[i]

def _isSorted(a, lo=None, hi=None):
  """is the array Sorted from a[lo] to a[hi] inclusive of idx==lo and idx==hi"""
  if lo is None and hi is None:
    lo = 0
    hi = len(a)-1
  for i in range(lo+1, hi+1):
      if __lt__(a[i], a[i-1]): return False
  return True

