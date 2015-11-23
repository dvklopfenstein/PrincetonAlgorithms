#!/usr/bin/env python
"""Convert an adjacency list presented as text to an array."""

from AlgsSedgewickWayne.testcode.utils import adjtxtblk2OrderedDict
from AlgsSedgewickWayne.testcode.utils import adjtxtblk2arr_ud
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
  od = adjtxtblk2OrderedDict(txtblk)
  assert od == cx.OrderedDict([
    ('A', ['F', 'B', 'E']),
    ('B', ['F', 'A']),
    ('C', ['G', 'F']),
    ('D', ['H', 'G']),
    ('E', ['A']),
    ('F', ['G', 'A', 'B', 'C']), 
    ('G', ['F', 'C', 'D']), 
    ('H', ['D'])])
  # Convert adjacency list in OrderedDict to array of format seen in tinyG.txt
  a, i2v = adjtxtblk2arr_ud(txtblk)
  assert a == [
    8, # V -> Number of vertices
    9, # E -> Number of edges
    (0, 1), (2, 6), (5, 6), (1, 5), (0, 5), (3, 6), (0, 4), (3, 7), (2, 5)] # edges
  


def run_all():
  test_0()

if __name__ == '__main__':
  #run_all()
  test_0()
