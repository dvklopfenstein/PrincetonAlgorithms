# TBD Finish Python port

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

    prt.write("Unsorted: {INTVLS}\n".format(INTVLS=", ".join(str(I) for I in intervals)))
    
    #prt.write("Sort by min endpoint\n")
    #Arrays.sort(intervals, Interval1D.MIN_ENDPOINT_ORDER)
    #for (int i = 0; i < len(intervals); i += 1)
    #    prt.write(intervals[i])
    #prt.write("\n")

    #prt.write("Sort by max endpoint\n")
    #Arrays.sort(intervals, Interval1D.MAX_ENDPOINT_ORDER)
    #for (int i = 0; i < len(intervals); i += 1)
    #    prt.write(intervals[i])
    #prt.write("\n")

    #prt.write("Sort by length\n")
    #Arrays.sort(intervals, Interval1D.LENGTH_ORDER)
    #for (int i = 0; i < len(intervals); i += 1)
    #    prt.write(intervals[i])
    #prt.write("\n")

#****************************************************************************
if __name__ == "__main__":
  test_0()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

