#!/usr/bin/env python3
"""Test Merge."""

import sys

from AlgsSedgewickWayne.Merge import Sort
from AlgsSedgewickWayne.testcode.ArrayHistory import ArrayHistory


def run(arr, desc, prt=sys.stdout):
    ahist = ArrayHistory()
    Sort(arr, array_history=ahist)
    ahist.prt_intlvd() # After each merge, print the state of both arr and aux
    #ahist.show(desc)
    prt.write("{DESC} RESULT: {A}\n".format(DESC=desc, A=arr))

def test_14238():
    arr = [int(s) for s in "80 97 50 29 23 83 66 67 43 47 41 42".split()]
    run(arr, "14238")

def test_3():
    # (seed = 183182)
    # Give the array that results after the first 4 exchanges when
    # selection sorting the following array:
    arr = [int(s) for s in "13 16 40 60 19 70 71 47 12 67".split()]
    run(arr, "MERGESORT 183182")

def test_2():
    # (seed = 183182)
    # Give the array that results after the first 4 exchanges when
    # selection sorting the following array:
    arr = "M E R G E S O R T E X A M P L E".split()
    run(arr, "MERGE SORT EXAMPLE")

def test_1():
    """Mergesort (23:54) Example at 02:19."""
    arr = "E E G M R A C R T".split()
    run(arr, "MERGE 1st Lec Ex")

def run_all():
    test_1()
    test_2()
    test_14238()

def run_seq():
    arr = [int(s) for s in sys.argv[1].split()]
    run(arr, "MERGESORT")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        run_all()
    else:
        run_seq()
