from AlgsSedgewickWayne.QuickUnionUF import QuickUnionUF
import sys

def _check(MST, G):
  """check optimality conditions (takes time proportional to E V lg* V)"""

  # check total weight
  total = 0.0
  for e in MST.edges():
    total += e.weight()
  if abs(total - MST.weight()) > MST.FLOATING_POINT_EPSILON:
    sys.stderr.write("Weight of edges does not equal weight(): {} vs. {}\n".format(
      total, MST.weight()))
    return False

  # check that it is acyclic
  uf = QuickUnionUF(G.V())
  for e in MST.edges():
    v, w = e.get_vw() 
    if uf.connected(v, w):
      sys.stderr.write("Not a forest\n")
      return False
    uf.union(v, w)

  # check that it is a spanning forest
  for e in G.edges():
    print v, w
    if not uf.connected(v, w):
      sys.stderr.write("Not a spanning forest\n")
      return False

  # check that it is a minimal spanning forest (cut optimality conditions)
  for e in edges():
    # all edges in MST except e
    uf = QuickUnionUF(G.V())
    for f in MST._mst:
      v, w = e.get_vw() 
      if f != e: uf.union(x, y)
    
    # check that e is min weight edge in crossing cut
    for f in G.edges():
      x, y = f.get_vw() 
      if not uf.connected(x, y):
        if f.weight() < e.weight():
          sys.stderr.write("Edge {} violates cut optimality conditions\n".format(f))
          return False
    return True

