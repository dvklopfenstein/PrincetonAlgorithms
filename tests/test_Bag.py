#!/usr/bin/env python
"""Tests the Bag class."""

import sys
from AlgsSedgewickWayne.Bag import Bag
from AlgsSedgewickWayne.InputArgs import get_list_from_args
from AlgsSedgewickWayne.InputArgs import get_seq__int_or_str

def run(item_list):
  """Add items to a Bad. Iterate through Bag."""
  bag = Bag()
  for item in item_list:
    bag.add(item)

  sys.stdout.write("size of bag = {}\n".format(bag.size()))
  for s in bag:
    sys.stdout.write("  BAG CONTAINS: {}\n".format(s))

def default_examples():
  """Run a simple default example."""
  run(get_seq__int_or_str("0 1 2 3 4 5 6 7 8 9"))

if __name__ == '__main__':
  if len(sys.argv) == 1:
    default_examples()
  else:
    run(get_list_from_args())
