#!/usr/bin/env python

from AlgsSedgewickWayne.Quick3way import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array
import sys

def run(a, prt=sys.stdout):
  desc = 'QUICK3WAY'
  ah = ArrayHistory()
  # Do not shuffle so that we may better visualize _sort actions
  Sort(a, array_history=ah, shuffle=False)
  ah.prt()
  #ah.show(desc)
  prt.write("{DESC} RESULT: {A}\n".format(
    DESC=desc, A=' '.join([str(e) for e in a])))


if __name__ == '__main__':
  run(cli_get_array("P A B X W P P V P D P C Y Z"))


