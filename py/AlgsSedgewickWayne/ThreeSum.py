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
 #/

import InputArgs
import sys
import timeit
import datetime

# Prints to standard output the (i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0.
# @param a the array of integers
def printAll(a):
  N = len(a)
  for i in range(N):
    for j in range(i+1, N):
      for k in range(j+1, N):
        if (a[i] + a[j] + a[k]) == 0:
          sys.stdout.write('{:6d} + {:6d} + {:6d}\n'.format(a[i], a[j], a[k]))

# Returns the number of triples (i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0.
# @param a the array of integers
# @return the number of triples (i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0
def count(a):
  N = len(a)
  cnt = 0
  for i in range(N):
    for j in range(i+1, N):
      for k in range(j+1, N):
        if (a[i] + a[j] + a[k]) == 0:
          cnt += 1
  return cnt

# Reads in a sequence of integers from a file, specified as a command-line argument;
# counts the number of triples sum to exactly zero; prints out the time to perform
# the computation.
def main(): 
  a = InputArgs.getStrArray()
  run(a)

def run(a):
  tic = timeit.default_timer()
  cnt = count(a)
  sys.stdout.write("Elapsed HMS: {}\n".format(
    str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))))
  sys.stdout.write('lines={} ThreeSum found {} times\n'.format(len(a), cnt))

def run_all(): 
  fins = [
    '../../thirdparty/1Kints.txt',
    '../../thirdparty/2Kints.txt',
    '../../thirdparty/4Kints.txt',
    '../../thirdparty/8Kints.txt']
  for fin in fins:
    sys.stdout.write('\nRunning ThreeSum on data in: {}\n'.format(fin))
    a = InputArgs.get_ints_from_file(fin)
    run(a)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    main()
  else:
    run_all()


# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne. 
# Java Last updated: Tue Sep 24 09:27:51 EDT 2013.
