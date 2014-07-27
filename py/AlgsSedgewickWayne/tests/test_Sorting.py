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

import AlgsSedgewickWayne.ArrayHistory as H

import unittest
import copy

class Sorting_Tests(unittest.TestCase):

  def getData(self, blktxt):
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

  def prtData(self, D):
    for idx, sort_this in enumerate(D):
      #print idx, 'SORT THIS:', ' '.join(sort_this)
      print idx, 'SORT THIS:', sort_this
    print

  def get_sort_history( self, lst ):
    lst_Selection = copy.deepcopy( lst )
    lst_Insertion = copy.deepcopy( lst )
    lst_Shell     = copy.deepcopy( lst )
    history_Selection = []
    history_Insertion = []
    history_Shell     = []
    Selection.Sort( lst_Selection, history_Selection )
    Insertion.Sort( lst_Insertion, history_Insertion )
    Shell.Sort(     lst_Shell,     history_Shell )
    return [history_Selection, history_Insertion, history_Shell]

  def determine_sort( self, list_orig, data ):
    # Get history for sorts: Selection, Insertion, and Shell
    hSelection, hInsertion, hShell = self.get_sort_history( list_orig )
    # Append 0 for "Original Sort"
    res = [0] 
    # Determine sorts for test_data 1 to N-1 
    for i,test_data in enumerate(data[1:-1]):
      #print test_data
      R = [H.history_contains( hSelection, test_data ), 
           H.history_contains( hInsertion, test_data ), 
           H.history_contains( hShell,     test_data )]
      # print i, R[0]
      # print i, R[1]
      # print i, R[2]
      if   R[0] and not R[1] and not R[2]:
        res.append(2) # Selection sort
      elif not R[0] and R[1] and not R[2]:
        res.append(1) # Insertion sort
      elif not R[0] and not R[1] and R[2]:
        res.append(3) # Shell sort
      else:
        raise Exception("UNKNOWN SORT")
    # Append 4 for "Sorted"
    res.append(4)
    return res

  def test_week2_exercise_Q2(self): # Lecture: Quick-Union Improvements 1:22
    # (seed = 709890)
    # The column on the left contains the original input of 16 strings to be sorted;
    # the column on the right contains the strings in sorted order; the other 6 columns contain the
    # contents at some intermediate step during one of the elementary sorting algorithms listed below.
    # 
    strData = """
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
    # You may use an algorithm more than once. Your answer should be a sequence of 8 integers between
    # 0 and 4 (starting with 0 and ending with 4) and with each integer separated by a whitespace.

    data = self.getData(strData) 
    list_orig   = data[0]   # Original unsorted data
    list_sorted = data[-1]  # Data sorted

    # Determine which intermediate result could have come from which sort for all data[1:-2]
    #     0. Original input
    #     1. Insertion sort
    #     2. Selection sort
    #     3. Shellsort (3x + 1 increments)
    #     4. Sorted
    res = self.determine_sort( list_orig, data )

    # Print results 
    print ' '.join(map(str,res))



if __name__ == '__main__':
  unittest.main()


