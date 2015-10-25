#!/usr/bin/env python

from AlgsSedgewickWayne.Quick import _partition
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array
import sys

def run(a, prt=sys.stdout):
  desc = 'QUICKSORT PARTITION'
  ah = ArrayHistory()
  j = _partition(a, lo=0, hi=len(a)-1, array_history=ah)
  ah.prt()
  ah.show(desc)
  print desc, "RESULT:", ' '.join(str(e) for e in a)


if __name__ == '__main__':
  run(cli_get_array("13 16 40 60 19 70 71 47 12 67"))


