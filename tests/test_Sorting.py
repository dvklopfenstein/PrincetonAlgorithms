#!/usr/bin/env python

# For comparing sorts.
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


# Used to help answer Week 2, Excersize Question 2 regarding various sorts and their invariants

# Selection Sort INVARIANTS: 02:31
#   * Entries left of the Ptr (inc the Ptr) fixed and in ascending order
#   * No entry to the right of Ptr is smaller than any entry to the left of Ptr.

# Insertion Sort INVARIANTS: 02:50
#   * Entries to the left or Ptr (inc Ptr) are in ascending order
#   * Entries to the right of Ptr have not yet been seen


import AlgsSedgewickWayne.Selection as Selection
import AlgsSedgewickWayne.Insertion as Insertion
import AlgsSedgewickWayne.Shell     as Shell

from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory

import unittest
import copy


def getData(blktxt):
  blkdata = []
  hstdata = []
  txt = blktxt.split("\n")
  # Loop through each line in the block text
  for T in txt:
    # If the text contains elements in the sort
    if len(T)!=0 and not T.isspace():
      blkdata.append( T.split() )
  # Transpose the block data so each array contains one instance in the sort history
  # Map to a list so elements can be changed.
  hstdata = map( list, zip(*blkdata) )
  return hstdata

def prtData(D):
  for idx, sort_this in enumerate(D):
    #print idx, 'SORT THIS:', ' '.join(sort_this)
    print idx, 'SORT THIS:', sort_this
  print

def get_sort_history(lst ):
  lst_Selection = copy.deepcopy( lst )
  lst_Insertion = copy.deepcopy( lst )
  lst_Shell     = copy.deepcopy( lst )
  history_Selection = ArrayHistory()
  history_Insertion = ArrayHistory()
  history_Shell     = ArrayHistory()
  Selection.Sort( lst_Selection, array_history=history_Selection )
  Insertion.Sort( lst_Insertion, array_history=history_Insertion )
  Shell.Sort(     lst_Shell,     array_history=history_Shell )
  return [history_Selection, history_Insertion, history_Shell]

def determine_sort( list_orig, data ):
  # Get history for sorts: Selection, Insertion, and Shell
  hSelection, hInsertion, hShell = get_sort_history( list_orig )
  # Append 0 for "Original Sort"
  res = [0]
  # Determine sorts for test_data 1 to N-1
  for i,test_data in enumerate(data[1:-1]):
    # TBD: Update...
    R = [H.history_contains( hInsertion, test_data ),
         H.history_contains( hSelection, test_data ),
         H.history_contains( hShell,     test_data )]
    if   R[0] and not R[1] and not R[2]:
      res.append(1) # Insertion sort
    elif not R[0] and R[1] and not R[2]:
      res.append(2) # Selection sort
    elif not R[0] and not R[1] and R[2]:
      res.append(3) # Shell sort
    else:
      raise Exception("UNKNOWN SORT")
    print test_data
    print i+1, res[-1], R[0]
    print i+1, res[-1], R[1]
    print i+1, res[-1], R[2]
  # Append 4 for "Sorted"
  res.append(4)
  return res


class Sorting_Tests(unittest.TestCase):

  def test_week2_exercise_Q2(self): # Lecture: Quick-Union Improvements 1:22
    # (seed = 709890)
    # The column on the left contains the original input of 16 strings to be sorted;
    # the column on the right contains the strings in sorted order;
    # the other 6 columns contain the contents at some intermediate
    # step during one of the elementary sorting algorithms listed below.
    #
    str_data = """
    gold   aqua   drab   aqua   aqua   gold   aqua   aqua
    bone   bark   aqua   bone   bark   bone   bone   bark
    pink   bone   bark   dust   bone   bark   dust   bone
    dust   corn   corn   gold   corn   dust   gold   corn
    iris   drab   gold   iris   iris   iris   iris   drab
    aqua   dust   bone   pink   gold   aqua   kobi   dust
    rust   gold   pine   rust   rust   rust   pink   gold
    kobi   iris   dust   kobi   kobi   kobi   rust   iris
    wine   wine   iris   wine   wine   wine   wine   jade
    jade   jade   jade   jade   jade   jade   jade   kobi
    pine   pine   plum   pine   pine   pine   pine   pine
    corn   rust   kobi   corn   dust   corn   corn   pink
    drab   kobi   wine   drab   drab   drab   drab   plum
    puce   puce   puce   puce   puce   puce   puce   puce
    plum   plum   rust   plum   plum   plum   plum   rust
    bark   pink   pink   bark   pink   pink   bark   wine
    """
    #---   ----   ----   ----   ----   ----   ----   ----
    #0      ?      ?      ?      ?      ?      ?      4
    #
    # You may use an algorithm more than once. Your answer should be a
    # sequence of 8 integers between 0 and 4 (starting with 0 and ending with 4)
    # and with each integer separated by a whitespace.

    data = getData(str_data)
    list_orig   = data[0]   # Original unsorted data
    list_sorted = data[-1]  # Data sorted

    # Determine which intermediate result could have come from which sort for all data[1:-2]
    #     0. Original input
    #     1. Insertion sort
    #     2. Selection sort
    #     3. Shellsort (3x + 1 increments)
    #     4. Sorted
    res = determine_sort( list_orig, data )

    # Print results
    print ' '.join(map(str,res))


  def test_week2_exercise_Q2a(self): # Lecture: Quick-Union Improvements 1:22
    # (seed = 213292)
    #        1      2      3      4      5      6
    str_data = """
    HOLE   BECK   HOLE   BECK   BECK   HOLE   BECK   BECK
    BUSH   BUSH   BUSH   BUSH   BUSH   BUSH   BUSH   BUSH
    MIMS   DEVO   EVE6   DEVO   DEVO   DEVO   HOLE   DEVO
    BECK   EVE6   BECK   EVE6   HOLE   BECK   MIMS   EVE6
    WHAM   HOLE   WHAM   HOLE   MIMS   SADE   NOFX   HOLE
    SOAD   JAYZ   SOAD   JAYZ   NOFX   KORN   SOAD   JAYZ
    NOFX   NOFX   NOFX   KORN   RATT   EVE6   TOTO   KORN
    TOTO   TOTO   TOTO   MIMS   SOAD   MIMS   WHAM   MIMS
    VAIN   VAIN   VAIN   VAIN   TOTO   VAIN   VAIN   NOFX
    RATT   RATT   RATT   RATT   VAIN   RATT   RATT   PINK
    DEVO   MIMS   DEVO   TOTO   WHAM   JAYZ   DEVO   RATT
    PINK   PINK   PINK   PINK   PINK   PINK   PINK   SADE
    SADE   SADE   SADE   SADE   SADE   WHAM   SADE   SOAD
    KORN   KORN   KORN   NOFX   KORN   SOAD   KORN   TOTO
    JAYZ   SOAD   JAYZ   SOAD   JAYZ   NOFX   JAYZ   VAIN
    EVE6   WHAM   MIMS   WHAM   EVE6   TOTO   EVE6   WHAM
    """
    #---   ----   ----   ----   ----   ----   ----   ----
    #0      ?      ?      ?      ?      ?      ?      4

    data = getData(str_data)
    list_orig   = data[0]   # Original unsorted data
    list_sorted = data[-1]  # Data sorted

    # Determine which intermediate result could have come from which sort for all data[1:-2]
    #     0. Original input
    #     1. Insertion sort
    #     2. Selection sort
    #     3. Shellsort (3x + 1 increments)
    #     4. Sorted
    res = determine_sort( list_orig, data )

    # Print results
    print ' '.join(map(str,res))


def curr(): # Exercise
#  self = Sorting_Tests()
  # (seed = 419606)
  #        1      2      3      4      5      6
  str_data = """
    gnat   frog   carp   carp   dove   carp   gnat   carp
    seal   gnat   clam   frog   carp   clam   lynx   clam
    sole   goat   dove   gnat   clam   dove   clam   dove
    pony   hake   frog   goat   frog   frog   pony   frog
    myna   myna   gnat   hake   gnat   gnat   myna   gnat
    goat   pony   goat   mole   goat   goat   goat   goat
    hake   seal   hake   myna   hake   hake   hake   hake
    frog   sole   lynx   pony   newt   lynx   frog   lynx
    mole   mole   mole   seal   mole   mole   mole   mole
    carp   carp   myna   sole   lynx   myna   carp   myna
    tuna   tuna   tuna   tuna   seal   newt   tuna   newt
    newt   newt   newt   newt   pony   tuna   newt   oryx
    dove   dove   sole   dove   myna   sole   dove   pony
    oryx   oryx   oryx   oryx   oryx   oryx   oryx   seal
    lynx   lynx   pony   lynx   tuna   pony   seal   sole
    clam   clam   seal   clam   sole   seal   sole   tuna
  """
  #---   ----   ----   ----   ----   ----   ----   ----
  #0      ?      ?      ?      ?      ?      ?      4

  data = getData(str_data)
  list_orig   = data[0]   # Original unsorted data
  list_sorted = data[-1]  # Data sorted

  # Determine which intermediate result could have come from which sort for all data[1:-2]
  #     0. Original input
  #     1. Insertion sort
  #     2. Selection sort
  #     3. Shellsort (3x + 1 increments)
  #     4. Sorted
  res = determine_sort( list_orig, data )

  # Print results
  print ' '.join(map(str,res))

  # Print str_data in a format that is easier to visualize word order
  prt_easy_viz(str_data)



def prt_easy_viz(str_data):
  data = getData(str_data)
  """Prints in a format which is easier to visualize sort order."""
  num_lists = len(data)     # Number of lists
  num_elems = len(data[-1]) # Number of elements per list

  # Assign symbols to each word which are easier to visualize
  d2s = { elem:'{sym:{width}}'.format(sym='*'*(i+1), width=num_elems) for i, elem in enumerate(data[-1]) }

  # Convert data to symbols stored in a list of lists
  data2sym = []
  for curr_lst in data:
    data2sym.append(d2s[elem] for elem in curr_lst)

  print str_data
  elems_by_lists = zip(*data2sym)
  for elem_per_list in elems_by_lists:
    print ' '.join(elem_per_list)


if __name__ == '__main__':
  #unittest.main()
  curr()


