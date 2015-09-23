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
# IN PRACTICE.
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

####################################################################
# 01:45 Lecture Week 1 "Order-of-Growth Classifications (14:39)
####################################################################
# constant            1
# logarithmic     log N
# linear              N
# linearithmic  N log N
# quadratic         N^2
# cubic             N^3
# exponential       2^N

####################################################################
# 01:45 Lecture Week 1 "Theory of Algorithms"
####################################################################
#
# EX 1. Array accesses for brute-force 3-SUM.
#   BEST.      ~ 1/2 N^2
#   AVERAGE.   ~ 1/2 N^2
#   WORST.     ~ 1/2 N^2

# 02:56 TYPES OF ANALYSES
#
# BEST  CASE. Lower bound on cost.
# WORST CASE. Upper bound on cost.
# AVERAGE CASE. "Expected" cost.
#
# ACTUAL DATA MIGHT NOT MATCH INPUT MODEL?
# * Need to understand input to effectively process it.
# * Approach 1: design for the worst case.
# * Approach 2: randomize, depend on probabilistic guarantee.

# 02:58 51 GOALS.
#   * Establish "difficulty" of a problem.
#   * Develop "optimal" algorithms.
#
# APPROACH
#   * Suppress details in analysis: analyze "to within a constant factor".
#   * Eliminate variability in in put model by focusing on the worst case.
#
# OPTIMAL ALGORITHM
#   * Performance guarantee (to within a constant factor) for any input.
#   * No algorithm can provide a better performance guarantee.

# 04:36 COMMONLY-USED NOTATIONS IN THE THEORY OF ALGORITHMS
#
# NOTATION   PROVIDES         EXAMPLE     SHORTHAND FOR            USED TO
# ---------  ---------------  ----------  -----------------------  -------
# Big Theta  asymptotic       theta(N^2)         1/2 N^2           classify
#            order of growth                      10 N^2           algorithms
#                                         5 N^2 + 22 N log N + 3N
#
# Big Oh     theta(N^2)       Oh(N^2)             10 N^2           develop
#            and smaller                         100 N^2           upper bounds
#                                             22 N log N + 3N
#
# Big Omega  theta(N^2)       omega(N^2)         1/2 N^2           develop
#            and larger                              N^5           lower bounds
#                                          N^3 + 22 N log N + 3 N
#
# Tilde      Leading term     ~10^2               10 N^2           provide
# 11:14                                    10 N^2 + 22 N log N     approximate
#                                          10 N^2 +  2 N + 37      model
#
# COMMON MISTAKE: Interpreting big-Oh as an approximate model.
# THIS COURSE: Focus on approximate models: use Tilde-notation

# 11:28 LECTURE QUESTION: Which of the fllowing functions is O(N^3)?
#
#   11 N + 15 lg N + 100
#   1/3 N^2
#   25,000 N^3
#
# ANSWER: ALL OF THE ABOVE
# EXPLANATION: Recall that big-Oh notation provides only an upper bound on the
# growth rate of a function as N gets large. In this course, we primarily
# use tilde notation because it more accurately describes the function -- it
# provides both an upper and lower bound on the function as well as
# the coefficient of the leading term.
#

# 07:02 53 THEORY OF ALGORITHMS: EXAMPLE 1
#
# EX: 1-Sum = "Is there a 0 in the array"
#
# UPPER BOUND. A specific algorithm.
#   * Ex. Brute-force algorithm for 1-Sum: Look at every array entry.
#   * Running time of the optimal algorithm for 1-Sum is )(N)
#
# LOWER BOUND. Proof that no algorithm can do better.
#   * Ex. Have to examine all N entries (any unexamined one might be 0).
#   * Running time of the optimal algorithm for 1-Sum is omega(N)
#
# OPTIMAL ALGORITHM.
#   * Lower bound equals upper bound (to within a constant factor).
#   * Ex. **Brute-fore algorithm for 1-Sum is optimal: its running time is theta(N).


# 07:38 55 THEORY OF ALGORITHMS: EXAMPLE 2
#
# EX: 3-Sum
#
# UPPER BOUND. A specific algorithm.
#   * Ex. Improved algorithm for 3-Sum
#   * Running time of the optimal algorithm for 3-Sum is O(N^2 log N)
#
# LOWER BOUND. Proof that no algorithm can do better.
#   * Ex. Have to examine all N entries to solve 3-Sum.
#   * Running time of the optimal algorithm for 3-SUm is omega(N)
#
# OPTIMAL ALGORITHM.
#   * Optimal algorithm for 3-Sum?
#   * Subquadratic algorithm of Quadratic lower bound for 3-Sum?
#     Do not know.
#     DO not know if alg is < O(N^2)

# 08:42 56 ALGORITHM DESIGN APPROACH
#
# START
#  * Develop an algorithm
#  * Prove a lower bound
#
# GAP?
#  * Lower the upper bound (discover a new algorithm)
#  * Raise the lower bound (more difficult)
#
# GOLDEN AGE OF ALGORITHM DESIGN
#  * 1970s-.
#  * Steadily decreasing upper bounds for many imporant problems.
#  * Many known optimal algorithms.
#
# CAVEATS.
#  * Overly pessimistic to focus on worst case?
#  * Need closer analysis than "to within a constant factor" to predict performance.
#

####################################################################
# Lecture Week 1 "Memory" (08:11)
####################################################################
# BASICS
#   BIT.   0 or 1
#   BYTE.  8 bits
#   MEGABYTE (MB). 1 million or 2^20 bytes
#   GIGABYTE (GB). 1 billion or 2^30 bytes

# TYPICAL MEMORY USAGE FOR PRIMITIVE TYPES
# type     bytes
# -------  -----
# boolean     1
# byte        1
# char        2
# int         4
# float       4
# long        8
# double      8

# 02:42 TYPICAL MEMORY USAGE FOR ARRAYS
# type       bytes
# ---------  --------
# char[]     2N + 24
# int[]      4N + 24
# double[]   8N + 24

# 03:00 FOR TWO DIMENSIONAL ARRAYS
# type       bytes
# ---------  --------
# char[][]   ~ 2 M N
# int[][]    ~ 4 M N
# double[][] ~ 8 M N

# 03:42 TYPICAL USAGE FOR OBJECTS IN JAVA
#   OBJECT OVERHEAD. 16 bytes
#   OBJECT REFERENCE. 8 bytes
#   OBJECT. 16 bytes + memory for each instance variable
#     +8 if inner class (for pointer to enclosing class).
#   PADDING.  Each object uses a multiple of 8 bytes.

# 05:28
# SHALLOW MEMORY USAGE: Don't count referenced objects.
# DEEP    MOMORY USAGE: If array entry or instance is a refence,
#   add memory (recursively) for referenced object.

# 04:00 EX 1 DATE OBJECT
#
# public class Date       // 16 bytes (object overhead)
# {
#   private int day;      //  4 bytes (int)
#   private int month;    //  4 bytes (int)
#   private int year;     //  4 bytes (int)
# ...                     //----------------
# }                       //  4 bytes (padding)
#                         //----------------
#                         // 32 bytes

# 04:29 EX 2 A VIRGIN STRING OF LENGTH N USES ~2N BYTES OF MEMORY
#
# public class String     // 16 bytes (object overhead)
# {
#   private char[] value; //  8 bytes (reference to array)
#                         //  2N + 24 bytes (char[] array)
#   private int offset;   //  4 bytes (int)
#   private int count;    //  4 bytes (int)
#   private int hash;     //  4 bytes (int)
# ...                     //----------------
# }                       //  4 bytes (padding)
#                         //----------------
#                         // 2N + 64 bytes

# 06:00 public class WeightedQuickUnionUF { // 16 bytes (object overhead)
#           private int[] id;          // 4N + 24 bytes (int[] array)
#                                      //       8 bytes (reference to array)
#           private int[] sz;          // 4N + 24 bytes (int[] array)
#                                      //       8 bytes (reference to array)
#           private int count;         //       4 bytes (int)
#                                      -----------
#                                      // 8N + 84
#                                      //    +  4 bytes padding




from AlgsSedgewickWayne.testcode.InputArgs import get_ints_from_file
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
  print "RUNNING count_itertools, written by Ashwini Chaudhary..."
  return sum((1 for x in itertools.combinations(a, r=3) if not sum(x)))


def count_itertools_faster(a): # written by Veedrak/modified (fastest)
  print "RUNNING count_itertools (faster), written by Veedrak(modified)..."
  return sum(1 for x, y, z in itertools.combinations(a, r=3) if x+y==-z)


def count_fixed(a): # written by roippi
  print "RUNNING count_fixed, written by roippi..."
  N = len(a)
  cnt = 0
  for i in range(N):
    for j in range(i+1, N):
      for k in range(j+1, N):
        if a[i] + a[j] + a[k] == 0:
          cnt += 1
  return cnt


def count_enumerate(a): # written by roippi
  print "RUNNING count_enumerate, written by roippi..."
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
def run_timed(a, cnt_fnc=count_enumerate):
  """Run ThreeSum and report the elapsed time."""
  tic = timeit.default_timer()
  cnt = cnt_fnc(a)
  sys.stdout.write('ThreeSum found {} times when run_timed on {} integers\n'.format(cnt, len(a)))
  sys.stdout.write("Elapsed HMS: {}\n".format(
    str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))))

def run_timed_fin(fin, cnt_fnc=count_enumerate):
  """Run ThreeSum using integers stored in a column in a file."""
  sys.stdout.write('\nRunning ThreeSum on data in: {}\n'.format(fin))
  run_timed(get_ints_from_file(fin), cnt_fnc)

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
    dig = int(sys.argv[1])
    a = [randrange(-2*dig, 2*dig) for i in range(dig)]
    run_timed(a)



# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Java Last updated: Tue Sep 24 09:27:51 EDT 2013.
