#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Knuth import shuffle
from AlgsSedgewickWayne.InputArgs import getStrArray

# Reads in a sequence of strings from standard input, shuffles
# them, and prints out the results.
def main():

  # read in the data
  a = getStrArray("a b c d e f")

  # shuffle the array
  shuffle(a)

  # print results.
  sys.stdout.write('{}\n'.format(' '.join(map(str, a))))


if __name__ == '__main__':
  main()
