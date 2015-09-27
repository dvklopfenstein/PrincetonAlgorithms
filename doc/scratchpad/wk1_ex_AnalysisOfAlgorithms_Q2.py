#!/usr/bin/env python

# https://class.coursera.org/algs4partI-005/quiz/attempt?quiz_id=141
# Algorithms, Part 1 
# by Kevin Wayne, Robert Sedgewick
# Princeton University
# 
# Week 1 Exercises: "Analysis of Algorithms" Question 2

import sys
import unittest

# def Ex2(N): # 09:01 Lec 3-3 Math Models
#   int count = 0;
#   for (int i=0; i<N; i++)
#     for (int j=i+1; j<N; j++)
#       # Each array access is (N 3) = N(N-1)/2! ~ N^2
#       # 3 array access is (1/2)*N^3
#       if (a[i] + a[j] == 0) # ~ N^2 Array Accesses
#         count++;

# def Ex3(N): # 10:01 Lec 3-3 Math Models
#   int count = 0;
#   for (int i=0; i<N; i++)
#     for (int j=i+1; j<N; j++)
#       for (int k=j+1; k<N; k++)
#         # Each array access is (N 3) = N(N-1)(N-2)/3! ~ (1/6)*N^3
#         # 3 array access is (1/2)*N^3
#         if (a[i] + a[j] + a[k] == 0) # (1/2)*N^3 Array Accesses
#           count++;
    
# Estimate a discrete sum?
# A1) Take a discrete mathematics course.
# A2) Replace the sum with an integral, and use calculus!
# Ex1: 1 + 2 + ... + N            SUM(i)[i=1..N] ~ integral(x dx) ~ (1/2)N^2
# Ex2: 1 + 1/2 + 1/3 + ... + 1/N  SUM(1/i)[i=1..N] ~ integral(1/x dx) = ln N
# Ex3: 3-sum triple loop  SUM[i=1..N]SUM[j=i..N]SUM[k=j..N] ... ~ (1/6)N^3

# Week 1 Lecture 3 - 4 Order of Growth Classifications (14-39)
#        
#                                                            T(2N)/T(N)
# -------- ------------- ----------------------------------- ---------
# 2^N      exponential   [see combinational search lecture]  T(N)
# 
# N^3      cubic         for (int i=0; i<N; i++)             8
#                          for (int j=0; j<N; j++)
#                            for (int k=0; k<N; k++)
# 
# N^2      quadratic     for (int i=0; i<N; i++)             4
#                          for (int j=0; j<N; j++)
# 
# N log N  linearithmic  [see mergesort lecture]            ~2
# N        linear        for (int i=0; i<N; i++): ...        2
# 
# log N    logarithmic   while (N>1): N=N/2                 ~1
# 1        constant      a = b + c                           1

# BINARY SEARCH: Lec 3 - 4 Order of Growth Classifications 08:26
# * 1st binary search published in 1946; first bug-free one in 1962
# * Bug in Java's Arrays.binarySearch() discovered in 2006
# 
# public static int binarySEarch( int[] a, int key)
# {
#   # Region of current interest is between lo and hi
#   int lo = 0; hi = a.length-1;
#   while (lo <= hi)
#   {
#     int mid = lo + (hi=lo)/2;
#     # one "3-way compare"
#     if      (key < a[mid]) hi = mid - 1;
#     else if (key > a[mid] lo = mid + 1;
#     else return mid;
#   }
#   return -1;
# }
# INVARIANT: If key appears in the array a[], then a[lo]<=key<=a[hi].
# MATHEMATICAL ANALYSIS:
# PROPOSITION: Binary serch uses at most 1 + lg N compares to search in a 
#              sorted array of size N
# DEF T(N) = # compares to binary search in a sorted subarray of size <= N.
# BINARY SEARCH RECURRENCE. T(N) <= T(N/2) + 1 for N>1, with T(1)=1.
#   T(N/2) => left or right half
#   1      => possible to implement with one 2-way compare (instead of 3-way)
# PROOF SKETCH:
#   T(N) <= T(N/2) + 1               Given
#        <= T(N/4) + 1 + 1           APPLY RECURRENCE TO FIRST TERM
#        <= T(N/8) + 1 + 1 + 1       APPLY RECURRENCE TO FIRST TERM
#        ...
#        <= T(N/N) + 1 + 1 + ... + 1 Stop applying, T(1)=1
#        = 1 + lg N


# AN N^2 log N ALGORITHM FOR 3-SUM
# 
# SORTING-BASED ALGORITHM: 13:08
# * Sort the N (distinct) numbers.   30 -40 -20 -10 40  0 10  5
# * For each pair of numbers a[i] and a[j], binary search for -(a[i]+a[j])
# 
# ANALYSIS: Order of growth is N^2 log N
# * Step 1: N^2 with INSERTION SORT.
# * Step 2: N^2 log N with BINARY SEARCH.
# 
# MUCH BETTER PERFORMANCE!
# * Old: N=8000 time=51.1
# * New: N=8000 time=0.96


###################################################################
# (seed = 868190)
# int sum = 0;
# for (int i = 0; i*i*i < N; i++)
#     for (int j = i+1; j*j*j < N; j++)
#         for (int k = j+1; k*k*k < N; k++)
#             sum++;
# THE ANSWER IS N!!!!!!!!!!!!!  Hurray!!!
#      The i loop iterates N^(1/3) times; 
#      the j loop iterates N^(1/3) times; 
#      the k loop iterates N^(1/3) times.


###################################################################
# (seed = 20279)
# What is the order of growth of the worst case running time
# of the following code fragment as a function of N?
# 
# int sum = 0;
# for (int i = 1; i <= N; i++)
#     for (int j = 1; j <= i*N; j++)
#         sum++;
# The answer is : N^3
# 
# The body of the innermost loop executes N + 2N + 3N + 4N + ... + N^2 ~ 1/2 N^3 times.

###################################################################
def Q2_238926(N):
  """Question 2 (seed = 238926) Worst Case Running Time.
     What is the order of growth of the worst case running time
     of the following code fragment as a function of N?
     NO: log_2(N) * log_2(N) * N*N
     ANSWER: N^3
       The i loop iterates N^(1/2) times; 
       the j loop iterates 2 N^(1/2) times; 
       the k loop iterates N^2 times.
  """
  sum = 0
  i = 0
  N_SQR = N*N
  while i*i < N: # log_2(N)
    j = 0
    while j*j < 4*N: # 4*log_2(N)
      sys.stdout.write('N=%d N*N=%d i=%-3d i*i=%-2d j=%-3d j*j=%-2d\n'%(N,N_SQR,i,i*i,j,j*j))
      k = 0
      while k < N_SQR:  # N*N
        sum += 1
        #sys.stdout.write('k=%-3d sum=%-d\n'%(k,sum))
        k += 1
      j += 1
    i += 1

class Q2_Tests(unittest.TestCase):

  def test_B(self):
    Q2_238926(4)

if __name__ == '__main__':
  unittest.main()
