#!/usr/bin/env python

from AlgsSedgewickWayne.SeparateChainingHashST import SeparateChainingHashST
import fileinput
import sys

def test_stdin(prt=sys.stdout):
  """echo "a b c d e f" | test_SeparateChainingHashST.py"""
  st = SeparateChainingHashST() # Initialize empty chaining-hash
  items_in = [w.rstrip("\n\r") for t in fileinput.input() for w in t.split(" ")]
  for i, key in enumerate(items_in):
    st.put(key, i)

  prt.write("\n")
  for s in st.keys():
    prt.write("{} {}\n".format(s, st.get(s)))

if __name__ == '__main__':
  test_stdin()
