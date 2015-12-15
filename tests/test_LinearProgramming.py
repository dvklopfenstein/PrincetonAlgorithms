#!/usr/bin/env python
# TBD Finish Python port

import sys
from AlgsSedgewickWayne.LinearProgramming import LinearProgramming

#****************************************************************************
# Compilation:  javac LinearProgramming.java
# Execution:    java LinearProgramming M N
# Dependencies: StdOut.java
#
# Given an M-by-N matrix A, an M-length vector b, and an
# N-length vector c, solve the  LP: max cx : Ax <= b, x >= 0 }.
# Assumes that b >= 0 so that x = 0 is a basic feasible solution.
#
# Creates an (M+1)-by-(N+M+1) simplex tableaux with the 
# RHS in column M+N, the objective function in row M, and
# slack variables in columns M through M+N-1.
#
def test_0(prt=sys.stdout):

      prt.write(" -= 1 -= 1- test 1  -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1")
      test1()
      prt.write(" -= 1 -= 1- test 2  -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1")
      test2()
      prt.write(" -= 1 -= 1- test 3  -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1")
      try:
          test3()
      catch (ArithmeticException e):
          e.printStackTrace()

      prt.write(" -= 1 -= 1- test 4  -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1")
      test4()


      prt.write(" -= 1 -= 1- test random  -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1-")
      M = Integer.parseInt(args[0])
      N = Integer.parseInt(args[1])
      double[] c = new double[N]
      double[] b = new double[M]
      double[][] A = new double[M][N]
      for (int j = 0; j < N; j += 1)
          c[j] = StdRandom.uniform(1000)
      for (int i = 0; i < M; i += 1)
          b[i] = StdRandom.uniform(1000)
      for (int i = 0; i < M; i += 1)
          for (int j = 0; j < N; j += 1)
              A[i][j] = StdRandom.uniform(100)
      LinearProgramming lp = new LinearProgramming(A, b, c)
      prt.write(lp.value())


#****************************************************************************
if __name__ == "__main__":
  test_0()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

