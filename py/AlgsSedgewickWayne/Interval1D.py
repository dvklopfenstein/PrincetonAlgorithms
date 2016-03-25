
"""The Interval1D class represents a one-dimensional interval.

       The interval is closed - it contains both endpoints.
       Intervals are immutable: their values cannot be changed after they are created.
       The class Interval1D includes methods for checking whether
       an interval contains a point and determin_valing whether two intervals intersect.

       For additional documentation, 
       see <a href="http://algs4.cs.princeton.edu/12oop/">Section 1.2</a> of 
       Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne. 

       @author Robert Sedgewick
       @author Kevin Wayne
"""
# TBD Finish Python port
import numpy as np

class Interval1D(object):

  def __init__(self, min_val, max_val):
      """Initializes a closed interval [self.min_val, self.max_val]."""
      assert np.isfinite(min_val) and np.isfinite(max_val), "Endpoints must be finite"
      if min_val <= max_val:
          self.min_val = min_val
          self.max_val = max_val
      else: raise Exception("Illegal interval")

  def intersects(self, that):
      """Returns True if self interval intersects the specified interval."""
      if self.max_val < that.min_val: return False
      if that.max_val < self.min_val: return False
      return True

  # Returns True if self interval contains the specified value.
  def contains(self, x): return self.min_val <= x and x <= self.max_val

  # Returns the length of self interval.
  def length(self): return self.max_val - self.min_val

  # Returns a string representation of self interval.
  def __str__(self): return "[{MIN}, {MAX}]".format(MIN=self.min_val, MAX=self.max_val)

  def equals(self, other):
      """True if self interval equals the other interval else False."""
      if other == self: return True
      if other is None: return False
      if isinstance(other, Interval1D) != isinstance(self, Interval1D): return False
      return self.min_val == other.min_val and self.max_val == other.max_val

  # ascending order of self.min_val endpoint, breaking ties by self.max_val endpoint
  @staticmethod
  def MinEndpointComparator(Interval1D_a, Interval1D_b):
      """Compares two intervals by self.min_val endpoint."""
      if   Interval1D_a.min_val < Interval1D_b.min_val: return -1
      elif Interval1D_a.min_val > Interval1D_b.min_val: return +1
      elif Interval1D_a.max_val < Interval1D_b.max_val: return -1
      elif Interval1D_a.max_val > Interval1D_b.max_val: return +1
      else:                                             return  0

  @staticmethod
  def MaxEndpointComparator(Interval1D_a, Interval1D_b):
      """Compares two intervals by self.max_val endpoint."""
      if   Interval1D_a.min_val < Interval1D_b.max_val: return -1
      elif Interval1D_a.min_val > Interval1D_b.max_val: return +1
      elif Interval1D_a.min_val < Interval1D_b.min_val: return -1
      elif Interval1D_a.min_val > Interval1D_b.min_val: return +1
      else:                                             return  0

  @staticmethod
  def LengthComparator(Interval1D_a, Interval1D_b):
      """Compares two intervals by length."""
      alen = Interval1D_a.length()
      blen = Interval1D_b.length()
      if    alen < blen: return -1
      elif  alen > blen: return +1
      else:              return  0

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.
