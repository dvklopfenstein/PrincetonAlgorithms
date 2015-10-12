#!/usr/bin/env python

from AlgsSedgewickWayne.SeparateChainingHashST import SeparateChainingHashST
import fileinput

def test_stdin():
  st = SeparateChainingHashST()
  for item in fileinput.input():
    item = item.rstrip("\n\r")
    if item == ".": break

if __name__ == '__main__':
  test_stdin()
