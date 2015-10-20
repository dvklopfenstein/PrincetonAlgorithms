#!/usr/bin/env python

from AlgsSedgewickWayne.Quick import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory

import random
import fileinput
import sys
import os
import re

def test_1(self):
  # (seed = 183182)
  # Give the array that results after the first 4 exchanges when
  # selection sorting the following array:
  desc = 'QUICKSORT'
  a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
  ah = ArrayHistory()
  Sort(a, array_history=ah)
  print desc, "RESULT", a
  # TBD: Implement array history visualization
  # prt_array_history(array_history)
  # show_array_history(desc, array_history)
  print


def test_stdin():
  """echo "a b c d e f" | test_Quick.py"""
  a = cli()
  print a
  print len(a)

def cli():
  """Command-line interface: reads data from arg, stdin, stream, or files."""
  # $ [file.py] "A B C D E F"
  if len(sys.argv) == 2:
    a = arr_int_or_str(sys.argv[1].split(" "))
    if a is not None:
      return a
  # $ echo "A B C D E F" | [file.py]
  # $ [file.py] # And then enter elems 1 at a time on stdin. End with two ctrl-Ds
  a = [w.strip(" \n\r") for t in fileinput.input() for w in t.splitlines()]
  if len(a) == 1 and re.search(r'[(\S+\s+)]+', a[0]):
    return arr_int_or_str(a[0].split(" "))
  # $ test_Quick.py ../thirdparty/1Kints.txt
  if a is not None:
    return a

def arr_int_or_str(a):
  """Return an array of ints or strs."""
  isdigit = True 
  for elem in a:
    if os.path.isfile(elem):
      return None
    M = re.search(r'[0-9.-eE]', elem)
    if not M:
      isdigit = False
      break
  if not isdigit:
    return a
  if isdigit:
    return [int(e) for e in a]

if __name__ == '__main__':
  test_stdin()


