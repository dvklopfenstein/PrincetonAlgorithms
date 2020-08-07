#!/usr/bin/env python

from AlgsSedgewickWayne.Quick import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

def run(a):
  desc = 'QUICKSORT'
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  ah.prt()
  ah.show(desc)
  print(desc, "RESULT:", a)


if __name__ == '__main__':
  run(cli_get_array("13 16 40 60 19 70 71 47 12 67"))


