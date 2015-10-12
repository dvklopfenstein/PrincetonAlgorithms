#!/usr/bin/env python

from AlgsSedgewickWayne.Transaction import Transaction

import sys
from operator import attrgetter

def test_sortbys(prt=sys.stdout):
  """Unit tests the <tt>Transaction</tt> data type."""
  a = [
    Transaction("Turing   6/17/1990  644.08"),
    Transaction("Tarjan   3/26/2002 4121.85"),
    Transaction("Knuth    6/14/1999  288.34"),
    Transaction("Dijkstra 8/22/2007 2678.40")]

  prt.write("\nUnsorted\n")
  for tr in a:
    prt.write("{}\n".format(tr))
  
  prt.write("\nSort by date\n")
  for tr in sorted(a, key=attrgetter('when')):
    prt.write("{}\n".format(tr))

  prt.write("\nSort by customer\n")
  for tr in sorted(a, key=attrgetter("who")):
    prt.write("{}\n".format(tr))

  prt.write("\nSort by amount\n")
  for tr in sorted(a, key=attrgetter("amount")):
    prt.write("{}\n".format(tr))

def test_hash(prt=sys.stdout):
  trs = [
    Transaction("Turing   6/17/1990  644.08"),
    Transaction("Tarjan   3/26/2002 4121.85"),
    Transaction("Knuth    6/14/1999  288.34"),
    Transaction("Dijkstra 8/22/2007 2678.40")]
  for tr in trs:
    prt.write("{} {}\n".format(tr, tr.hashCode()))

def run_all():
  #test_sortbys()
  test_hash()

if __name__ == '__main__':
  run_all()
