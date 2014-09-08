#!/usr/bin/env python
#************************************************************************
 #  Compilation:  javac ThreeSumFast.java
 #  Execution:    java ThreeSumFast input.txt
 #  Dependencies: StdOut.java In.java Stopwatch.java
 #  Data files:   http://algs4.cs.princeton.edu/14analysis/1Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/2Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/4Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/8Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/16Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/32Kints.txt
 #                http://algs4.cs.princeton.edu/14analysis/1Mints.txt
 #
 #  A program with N^2 log N running time. Read in N integers
 #  and counts the number of triples that sum to exactly 0.
 #
 #  Limitations
 #  -----------
 #     - we ignore integer overflow
 #     - doesn't handle case when input has duplicates
 #
 #
 #  % java ThreeSumFast 1Kints.txt
 #  70
 #  
 #  % java ThreeSumFast 2Kints.txt
 #  528
 #                
 #  % java ThreeSumFast 4Kints.txt
 #  4039
 # 
 #  % java ThreeSumFast 8Kints.txt
 #  32074
 #
 #  % java ThreeSumFast 16Kints.txt
 #  255181
 #
 #  % java ThreeSumFast 32Kints.txt
 #  2052358
 #
 #************************************************************************/

import java.util.Arrays

#*
 #  The <tt>ThreeSumFast</tt> class provides static methods for counting
 #  and printing the number of triples in an array of distinct integers that
 #  sum to 0 (ignoring integer overflow).
 #  <p>
 #  This implementation uses sorting and binary search and takes time 
 #  proportional to N^2 log N, where N is the number of integers.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/14analysis">Section 1.4</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
public class ThreeSumFast:

    # returns True if the sorted array a[] contains any duplicated integers
    def _containsDuplicates(int[] a):
        for (int i = 1; i < len(a); i++)
            if a[i] == a[i-1]) return True
        return False

    #*
     # Prints to standard output the (i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0.
     # @param a the array of integers
     # @throws IllegalArgumentException if the array contains duplicate integers
     #/
    def printAll(int[] a):
        N = len(a)
        Arrays.sort(a)
        if containsDuplicates(a)) raise new IllegalArgumentException("array contains duplicate integers")
        for (int i = 0; i < N; i++):
            for (int j = i+1; j < N; j++):
                k = Arrays.binarySearch(a, -(a[i] + a[j]))
                if k > j) StdOut.println(a[i] + " " + a[j] + " " + a[k])

    #*
     # Returns the number of triples (i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0.
     # @param a the array of integers
     # @return the number of triples (i, j, k) with i < j < k such that a[i] + a[j] + a[k] == 0
     #/
    def count(int[] a):
        N = len(a)
        Arrays.sort(a)
        if containsDuplicates(a)) raise new IllegalArgumentException("array contains duplicate integers")
        cnt = 0
        for (int i = 0; i < N; i++):
            for (int j = i+1; j < N; j++):
                k = Arrays.binarySearch(a, -(a[i] + a[j]))
                if k > j) cnt++
        return cnt

    #*
     # Reads in a sequence of distinct integers from a file, specified as a command-line argument;
     # counts the number of triples sum to exactly zero; prints out the time to perform
     # the computation.
     #/
    def main(String[] args): 
        In in = new In(args[0])
        int[] a = in.readAllInts()
        cnt = count(a)
        StdOut.println(cnt)


# Copyright © 2002–2010, Robert Sedgewick and Kevin Wayne. 
# Java last updated: Tue Sep 24 09:30:55 EDT 2013.
