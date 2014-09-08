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
 #  A program with cubic run_timedning time. Read in N integers
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


####################################################################
# Lecture Week 1 Mathematical Models (12:48)
####################################################################
# 
# 03:10 COST OF BASIC OPERATIONS
# variable declaration    int a               c1
# assignment statement    a = b               c2
# integer compare         a < b               c3
# array element access    a[i]                c4
# array length            a.length            c5
# 1D array allocation     new int[N]          c6*N
# 2D array allocation     new int[N][N]       c7*N^2
# string length           s.length            c8
# substring extraction    s.substring(N/2, N) c9
# string concatenation    s + t               c10*N
# 
# NOVICE MISTAKE. Abusive string concatenation.
# If you concatenate 2 strings, run_timedning time is proportional to length of string.


# 03:56 HOW MANY INSTRUCTIONS AS A FUNCTION OF INPUT SIZE N?
# 
#   int count = 0;
#   for (int i = 0; i<N; i++)
#     if (a[i] == 0)
#       count++;
# 
#   operation              freq     code
#   ---------------------- -----    --------
#   variable declaration     2      i, cnt
#   assignment statement     2      i=0, cnt=0
#   less than compare      N + 1    i<N
#   equal to compare         N      a[i] == 0
#   array access             N      a[i]
#   increment             N to 2 N  i inc N times. cnt inc 0 to N times (dep. on input data)


# 05:03 EXAMPLE 2-SUM: HOW MANY INSTRUCTIONS AS A FUNCTION OF INPUT SIZE N?
# 
#   int count = 0;
#   for (int i = 0; i< N;i++)
#     for (int j = i+1; j < N; j++)
#       if (a[i] + a[j] == 0)
#         count++;
#
# 09:12 BOTTOM LINE. Use COST MODEL and TILDE NOTATION to simplify counts.
# ANSWER:	~N^2 array accesses.
#
# if (a[i] + a[j] == 0):                    (N) <- N choose 2
#   0 + 1 + 2 + ... + (N-1) = 1/2(N)(N-1) = (2)
# 
#     operation                  freq             tilde      code
#     ----------------------     -----            --------   ----------
#   0 variable declaration       N + 2            ~N         i, cnt
#   1 assignment statement       N + 2            ~N         i=0, cnt=0
#  *2 less than compare      1/2(N+1)(N+2)        ~1/2N^2    i<N
#  *3 equal to compare       1/2(N)(N-1)          ~1/2N^2    a[i] == 0
#  *4 array access                N(N-1)          ~N^2       a[i]
#  *5 increment        1/2(N)(N-1) to N(N-1)  1/2N^2 to ~N^2

# *2-*5 are tedious to compute
#
# 7:08 So use the operation that is either/both:
#   * the most expensive
#   * the most frequent
# 
# SIMPLIFICATION 1: Choose array accesses as most important to count

# 07:20 SIMPLIFICATION 2: TILDE NOTATION (Ignore low order terms in derived functions)
# 
# *  Estimate run_timedning time (or memory) as a function of input size N.
# * Ignore lower order terms.
#   - when N is large, terms are negliglible
#   - when N is small, we don't care
# 
# EX1: 1/6N^3 +  20N       + 16    ~ 1/6N^3
# EX2: 1/6N^3 + 100N^(4/3) + 56    ~ 1/6N^3
# EX3: 1/6N^3 - 1/2N^2     + 1/3N  ~ 1/6N^3

# 08:12 TECHNICAL DEFINITION. 
# 
#   f(N) ~ g(N) means    lim f(N)
#                     N->Inf ---- = 1
#                            g(N)

# 10:00 APPROXIMATELY how many ARRAY ACCESSES as a function of input size N
# for ThreeSum:
#
# if (a[i] + a[j] + a[k] == 0)
# 
# /N\ = N(N-1)(N-2)     1
# \3/   -----------   ~ - N^3
#           3!          6
#
# ANSWER: THREESUM has 1/3N^3 array accesses

# 11:31 ESTIMATING A DISCRETE SUM: Replacing a discrete sum w/an integral:
#
# EX1: 1 + 2 +...+ N.           SUM(i=1:N) ~ Integral(x=1:N)[x dx]   ~ 1/2 N^2
# EX2: 1 + 1/2 + 1/3 +...+ 1/N  SUM(i=1:N) ~ Insegral(x=1:N)[1/x dx] ~ ln N
# EX3: 3-sum triple loop. SUM(i=1:N)SUM(y=x:N)SUM(z=y:N)dz dy dx     ~ 1/6 N^3

# 11:45 MATHEMATICAL MODELS FOR RUNNING TIME
#
# IN PRINCIPLE. accurate mathematical models are available.
#
# IN PROACTICE.
#  * Formulas can be complicated.
#  * Advanced mathematics might be required.
#  * Exact models best left for experts.
#
# T(N) = c1*A + c2*B + c3*C + c4*D + c5*E
#   A = array access
#   B = integer add
#   C = integer compare
#   D = increment
#   E = variable assignment
# cN depends on machine, compiler
# A..E frequencies: depend on algorithm, input
# 
# BOTTOM LINE. We use APPROXIMATE models in this course: T(N) ~ cN^3

# 12:42 QUESTION: How many array accesses does the following code fragment
# make as a function of N? (Assume the compiler does not optimize away
# accesses in the innermost loop.)
# 
# int sum = 0;
# for (int i = 0; i < N; i++)
#   for (int j = i+1; j < N; j++)
#     for (int k = 1; k < N; k = k*2)
#       if (a[i] + a[j] >= a[k])
#         sum++;      
#
# ANSWER: ~3/2*N^2*lg(N)
#
# EXPLANATION: Not all tripl loops have cubic run_timedning times. for a given
# value of i and j, the k-loop requires only 3*lg(N) array access: the 
# body is executed lg(N) times and each time involves 3 array accesses.
# As in the 2-SUM and 3-SUM analysis, the number of times the k-loop
# is executed is (N choose 2) ~ 1/2 N^2

# 01:45 Lecture Week 1 "Theory of Algorithms"
# 
# EX 1. Array accesses for brute-force 3-SUM.
#   BEST.      ~ 1/2 N^2
#   AVERAGE.   ~ 1/2 N^2
#   WORST.     ~ 1/2 N^2






import InputArgs
import sys
import itertools
import timeit
import datetime

# Returns the number of triples (i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0.
# @param a the array of integers
# @return the number of triples (i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0

# http://stackoverflow.com/questions/25712596/why-is-the-map-version-of-threesum-so-slow/25717916#25717916
def count_slow(a, prt=False): # initial translate of Java (super slow)
  """ThreeSum: Given N distinct integers, how many triples sum to exactly zero?"""
  print "RUNNING count_slow..."
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


def count_itertools(a): # written by Ashwini Chaudhary
  """ThreeSum using itertools"""
  print "RUNNING count_itertools..."
  return sum((1 for x in itertools.combinations(a, r=3) if not sum(x)))


def count_itertools_faster(a):
  print "RUNNING count_itertools (faster)..."
  return sum(1 for x, y, z in itertools.combinations(xs, r=3) if x+y==z)


def count_fixed(a): # written by roippi
  print "RUNNING count_fixed..."
  N = len(a)
  cnt = 0
  for i in range(N):
    for j in range(i+1, N):
      for k in range(j+1, N):
        if a[i] + a[j] + a[k] == 0:
          cnt += 1
  return cnt


def count_enumerate(a): # written by roippi
  print "RUNNING count_enumerate..."
  cnt = 0
  for i, x in enumerate(a):
    for j, y in enumerate(a[i+1:], i+1):
      for z in a[j+1:]:
        if x + y + z == 0:
          cnt += 1
  return cnt

# --------------------------------------------------------------------------------------
# Reads in a sequence of integers from a file, specified as a command-line argument;
# counts the number of triples sum to exactly zero; prints out the time to perform
# the computation.
def run_timed(a, cnt_fnc):
  """Run ThreeSum and report the elapsed time."""
  tic = timeit.default_timer()
  cnt = cnt_fnc(a)
  sys.stdout.write('ThreeSum found {} times when run_timed on {} integers\n'.format(cnt, len(a)))
  sys.stdout.write("Elapsed HMS: {}\n".format(
    str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))))

def run_timed_fin(fin, cnt_fnc): 
  """Run ThreeSum using integers stored in a column in a file."""
  sys.stdout.write('\nRunning ThreeSum on data in: {}\n'.format(fin))
  run_timed(InputArgs.get_ints_from_file(fin), cnt_fnc)

def run_timed_fins(fins): 
  """Run ThreeSum on multiple files containing integers."""
  for fin in fins:
    run_timed_fin(fin)

if __name__ == '__main__':
  import os
  from random import randrange
  # If there are no arguments, run 1 example using a few different Python algorithms
  # to show different ways to implement the O(N^3) algorithm in Python
  if len(sys.argv) == 1:
    run_timed_fin('../../thirdparty/1Kints.txt', count_slow)
    run_timed_fin('../../thirdparty/1Kints.txt', count_itertools)
    run_timed_fin('../../thirdparty/1Kints.txt', count_itertools_faster)
    run_timed_fin('../../thirdparty/1Kints.txt', count_fixed)
    run_timed_fin('../../thirdparty/1Kints.txt', count_enumerate)
  # Run all the examples from the Princeton Algorithms book-site
  elif sys.argv[1] == 'all':
    fins = [
      '../../thirdparty/1Kints.txt',
      '../../thirdparty/2Kints.txt',
      '../../thirdparty/4Kints.txt',
      '../../thirdparty/8Kints.txt']
    run_timed_fins(fins)
  # If the argument is a file, run using the integers from that file
  elif os.path.isfile(sys.argv[1]):
    run_timed_fin(sys.argv[1])
  # If the argument is a digit, run using that many randomly chosen digits.
  elif sys.argv[1].isdigit():
    a = [randrange(-999999, 999999) for i in range(int(sys.argv[1]))]
    run_timed(a, count_slow)
    run_timed(a, count_itertools)
    


# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne. 
# Java Last updated: Tue Sep 24 09:27:51 EDT 2013.
