#!/usr/bin/env python
"""Test ResizingArrayStack."""

from AlgsSedgewickWayne.ResizingArrayStack import ResizingArrayStack

import sys

def main(prt=sys.stdout):
  """Unit tests the Stack data type."""
  a = "to be or not to be".split()
  prt.write("{}\n".format(a))
  s = ResizingArrayStack()
  while a:
    item = a.pop()
    prt.write("{}\n".format(item))
    if item != "-": s.push(item)
    elif not s.isEmpty(): 
      prt.write("{} \n".format(s.pop()))
  sys.stdout.write("({}) left on stack)".format(s.size()))
  for S in s: 
    prt.write("{}\n".format(S))

if __name__ == '__main__':
  main()
