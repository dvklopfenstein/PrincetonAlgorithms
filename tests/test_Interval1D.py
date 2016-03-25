#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Interval1D import Interval1D

def test_0(prt=sys.stdout):
    """Unit tests the Interval1D data type."""
    intervals = [
        Interval1D(15.0, 33.0),
        Interval1D(45.0, 60.0),
        Interval1D(20.0, 70.0),
        Interval1D(46.0, 55.0),
    ]

    get_ivstr = lambda intvls: ", ".join(str(intvl) for intvl in intvls)

    prt.write("Unsorted: {INTVLS}\n".format(INTVLS=get_ivstr(intervals)))
    
    prt.write("Sort by min endpoint: {INTVLS}\n".format(
        INTVLS=get_ivstr(Interval1D.sortby_minendpoint(intervals))))

    prt.write("Sort by max endpoint: {INTVLS}\n".format(
        INTVLS=get_ivstr(Interval1D.sortby_maxendpoint(intervals))))

    prt.write("Sort by length: {INTVLS}\n".format(
        INTVLS=get_ivstr(Interval1D.sortby_length(intervals))))


if __name__ == "__main__":
  test_0()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

