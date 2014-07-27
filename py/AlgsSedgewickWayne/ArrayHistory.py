#!/ust/bni/env python

import sys

def prt_array_history(array_history):
  for idx,A in enumerate(array_history):
    sys.stdout.write('{:2d}: {}\n'.format(idx, ' '.join(map(str,A))))

def get_elem2num(array_history):
  # In array_history, last array should be the sorted arrayA
  elem2num = {}
  num = 0
  for elem in array_history[-1]:
    elem2num[elem] = num
    num += 1
  return elem2num

def animate(array_history):
  elem2num = get_elem2num(array_history)
  print elem2num
