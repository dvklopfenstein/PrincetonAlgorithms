#!/usr/bin/env python
"""Convert an adjacency list presented as text to an array."""

from AlgsSedgewickWayne.testcode.utils import adjtxtblk2arr
import collections as cx

def test_0():
  txtblk = """
    A:  F B E 
    B:  F A 
    C:  G F 
    D:  H G 
    E:  A 
    F:  G A B C 
    G:  F C D 
    H:  D 
"""
  a = adjtxtblk2arr(txtblk)
  print a
  assert a == cx.OrderedDict([
    ('A', ['F', 'B', 'E']),
    ('B', ['F', 'A']),
    ('C', ['G', 'F']),
    ('D', ['H', 'G']),
    ('E', ['A']),
    ('F', ['G', 'A', 'B', 'C']), 
    ('G', ['F', 'C', 'D']), 
    ('H', ['D'])])


def run_all():
  test_0()

if __name__ == '__main__':
  #run_all()
  test_0()
