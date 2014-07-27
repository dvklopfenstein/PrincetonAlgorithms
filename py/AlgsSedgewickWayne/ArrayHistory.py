#!/ust/bni/env python

# A module for helping to visualize array sorting.
# Copyright (C) 2014  D. Klopfenstein
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


import sys

def prt_array_history(array_history):
  """ Prints array history with spaces between elements."""
  for idx,A in enumerate(array_history):
    sys.stdout.write('{:2d}: {}\n'.format(idx, ' '.join(map(str,A))))

def get_elem2num(array_history):
  """ 1 is assigned to smallest element.  len(arr)+1 is assigned to largest element."""
  # In array_history, last array should be the sorted arrayA
  elem2num = {}
  num = 1
  for elem in array_history[-1]:
    elem2num[elem] = num
    num += 1
  return elem2num

def animate(desc, array_history):
  if isinstance(array_history,list) and len(array_history) != 0:
    """ Print array history plus histogram bars (viewed horizontally) to help visualize sort."""
    elem2num = get_elem2num(array_history)
    for idx,A in enumerate(array_history):
      sys.stdout.write('{:2d} {}: {}\n'.format(idx, desc, ' '.join(map(str,A))))
      for elem in A:
        sys.stdout.write('{:2d} {}: {} {}\n'.format(idx, desc, elem, ''.join(['*']*elem2num[elem])))
      sys.stdout.write('\n')
