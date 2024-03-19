#!/usr/bin/env python
"""Test shell sort"""
# pylint: disable=missing-function-docstring

import sys
from collections import OrderedDict
from AlgsSedgewickWayne.Shell import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array


def test_wk2_lec_a():
    """From Alg 1, week 2, lecture Shellsort (10:48) at 1:48"""
    arr = "S H E L L S O R T E X A M P L E".split()
    run(arr, 'SHELL SORT LEC EX')

def test_wk2_lec_b():
    """From Alg 1, week 2, lecture Shellsort (10:48) at 2:02"""
    arr = "M O L E E X A S P R T".split()
    run(arr, 'SHELL SORT LEC EX', sort_seq=[1, 3, 7])

def test_1():
    # (seed = 183182)
    # Give the array that results after the first 4 exchanges when
    # selection sorting the following array:
    arr = [int(n) for n in "13 16 40 60 19 70 71 47 12 67".split()]
    run(arr, 'SHELL SORT')

#   This test did not work as hoped using a dict, but is based on this Week 2 Exercise question:
#   TBD: Make arr test which demonstrates this idea...
#
#   QUESTION: If two items arr and b have equal keys and arr appears before b
#     in the input array, then arr appears before b in the array
#     after Shellsorting (with Knuth's 3x+1 increments) the array.
#   ANSWER(FALSE): Consider an array with five items
#       { (B, 1), (B, 2), (B, 3), (B, 4), (A, 1) },
#     where the key is the letter A or B. After Shellsort, the array is
#       { (A, 1), (B, 2), (B, 3), (B, 4), (B, 1) }.
#     This property is known as stability. Stay tuned for the mergesort lecture.
def test_2():
    # Keys are 'A' and 'B':
    ##arr = [{'B':1}, {'B':2}, {'B':3}, {'B':4}, {'B':5}, {'A':1}]
    arr = OrderedDict([('B', 1), ('B', 2), ('B', 3), ('B', 4), ('B', 5), ('A', 1)])
    ahobj = ArrayHistory()
    Sort(arr, array_history=ahobj)
    ahobj.show('SHELL')

def test_3():
    # Keys are 'A' and 'B':
    arr = [int(n) for n in "51 99 35 60 96 18 19 64 42 10".split()]
    run(arr, "SHELL CUR")

def test_q3a():
    # Q: The number of compares to Shellsort (with Knuth's 3x+1 increments)
    # an array of length N depends only on N (and not on the items in the array).
    # A: The number of compares to Shellsort the array { 1, 2, 3 } is 2;
    # the number of compares to Shellsort the array { 3, 2, 1 } is three.
    run([1, 2, 3], "SHELL N=3 => 2 COMPARES")
    run([3, 2, 1], "SHELL N=3 => 3 COMPARES")

def test_q3b():
    """Wk2 Ex Sorts Q3"""
    # An array of N distinct keys that is both 2-sorted and 3-sorted
    # can be 1-sorted in one insertion-sort pass, using only N compares.
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    run(arr, 'SHELL EX', sort_seq=[1, 2, 3])


def run(arr, desc=None, sort_seq=None, prt=sys.stdout):
    ahobj = ArrayHistory()
    prt.write(f"{desc} START:\n    {' '.join(str(e) for e in arr)}\n")
    Sort(arr, array_history=ahobj, sort_seq=sort_seq)
    if desc is None:
        desc = "SHELL SORT"
    prt.write(f"{desc} RESULT:\n    {' '.join(str(e) for e in arr)}\n")
    prt.write(f"{desc} START:\n    {' '.join(str(e) for e in arr)}\n")
    ahobj.prt()
    ahobj.show(desc)

def run_all():
    test_wk2_lec_a()
    test_wk2_lec_b()
    test_1()
    #test_2()
    test_3()
    test_q3a()

def cli():
    len_array = len(sys.argv)
    if len_array == 1:
        run_all()
    elif len_array == 2:
        run(cli_get_array())

if __name__ == '__main__':
    cli()
