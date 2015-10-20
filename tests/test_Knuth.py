#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Knuth import shuffle
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

# Reads in a sequence of strings from standard input, shuffles
# them, and prints out the results.
def main():

  # read in the data
  a = cli_get_array("a b c d e f")

  # shuffle the array
  shuffle(a)

  # print results.
  sys.stdout.write('{}\n'.format(' '.join(map(str, a))))


if __name__ == '__main__':
  main()
