#!/usr/bin/env python
"""Tests the Bag class."""

import sys
from AlgsSedgewickWayne.Bag import Bag
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

def run(item_list):
  """Add items to a Bad. Iterate through Bag."""
  bag = Bag()
  for item in item_list:
    bag.add(item)

  sys.stdout.write("size of bag = {}\n".format(bag.size()))
  for s in bag:
    sys.stdout.write("  BAG CONTAINS: {}\n".format(s))

if __name__ == '__main__':
  run(cli_get_array("0 1 2 3 4 5 6 7 8 9"))
