#!/usr/bin/env python
#************************************************************************
 #  Compilation:  javac ThreeSum.java
 #  Execution:    java ThreeSum input.txt
 #  Dependencies: In.java StdOut.java Stopwatch.java
 #  Data files:   http://algs4.cs.princeton.edu/14analysis/1Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/2Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/4Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/8Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/16Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/32Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/1Mints.txt
 #
 #  A program with cubic running time. Read in N integers
 #  and counts the number of triples that sum to exactly 0
 #  (ignoring integer overflow).
 #
 #  % java ThreeSum 1Kints.txt 
 #  70
 #
 #  % java ThreeSum 2Kints.txt 
 #  528
 #
 #  % java ThreeSum 4Kints.txt 
 #  4039
 #
 #************************************************************************/

#*
 #  The <tt>ThreeSum</tt> class provides static methods for counting
 #  and printing the number of triples in an array of integers that sum to 0
 #  (ignoring integer overflow).
 #  <p>
 #  This implementation uses a triply nested loop and takes proportional to N^3,
 #  where N is the number of integers.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/14analysis">Section 1.4</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #
 #/

####################################################################
# Lecture Week 1 Observations (10:05)
####################################################################
# 
# 3-SUM: Given N distinct integers, how many triples sum to exactly zero?
# 
# a = [30 -40 -20 -10 40 0 10 5]
# 
#   a[i] a[j] a[k] sum
#   ---  ---- ---- ---
# 1  30   -40   10   0
# 2  30   -20  -10   0
# 3 -40    40    0   0
# 4 -10     0   10   0
# 
# CONTEXT: Deeply related to problems in computational geometry.
# graphics, movies, etc.

import InputArgs
import sys
import itertools

# Returns the number of triples (i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0.
# @param a the array of integers
# @return the number of triples (i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0

def count(a, prt=False):
  """ThreeSum: Given N distinct integers, how many triples sum to exactly zero?"""
  N = len(a)
  cnt = 0
  for i in range(N):
    for j in range(i+1, N):
      for k in range(j+1, N):
        if sum([a[i], a[j], a[k]]) == 0:
          cnt += 1
          if prt:
            sys.stdout.write('{:7d} + {:7d} + {:7d}\n'.format(a[i], a[j], a[k]))
  return cnt

def count_python(a):
  """ThreeSum using itertools"""
  return sum((1 for x in itertools.combinations(a, r=3) if not sum(x)))



# Reads in a sequence of integers from a file, specified as a command-line argument;
# counts the number of triples sum to exactly zero; prints out the time to perform
# the computation.
def run(a):
  """Run ThreeSum and report the elapsed time."""
  import timeit
  import datetime

  tic = timeit.default_timer()
  cnt = count(a)
  sys.stdout.write('ThreeSum found {} times when run on {} integers\n'.format(cnt, len(a)))
  sys.stdout.write("Elapsed HMS: {}\n".format(
    str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))))

  #tic = timeit.default_timer()
  #cnt = count_python(a)
  #sys.stdout.write('ThreeSum found {} times when run on {} integers\n'.format(cnt, len(a)))
  #sys.stdout.write("Elapsed HMS: {}\n".format(
  #  str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))))

def run_fin(fin): 
  """Run ThreeSum using integers stored in a column in a file."""
  sys.stdout.write('\nRunning ThreeSum on data in: {}\n'.format(fin))
  run(InputArgs.get_ints_from_file(fin))

def run_fins(fins): 
  """Run ThreeSum on multiple files containing integers."""
  for fin in fins:
    run_fin(fin)

if __name__ == '__main__':
  import os
  from random import randrange
  # If there are no arguments, run the examples (May take a While)
  if len(sys.argv) == 1:
    fins = [
      '../../thirdparty/1Kints.txt',
      '../../thirdparty/2Kints.txt',
      '../../thirdparty/4Kints.txt',
      '../../thirdparty/8Kints.txt']
    run_fins(fins)
  elif os.path.isfile(sys.argv[1]):
    run_fin(sys.argv[1])
  elif sys.argv[1].isdigit():
    a = [randrange(-999999, 999999) for i in range(int(sys.argv[1]))]
    a = range(5)
    run(a)
    


# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne. 
# Java Last updated: Tue Sep 24 09:27:51 EDT 2013.
