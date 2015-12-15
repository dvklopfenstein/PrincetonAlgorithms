
# TBD Finish Python port

 ******************************************************************************/

package edu.princeton.cs.algs4

#
# The <tt>LinearProgramming</tt> class represents a data type for solving a
# linear program of the form: max cx : Ax <= b, x >= 0 }, where A is a M-by-N
# matrix, b is an M-length vector, and c is an N-length vector. For simplicity,
# we assume that A is of full rank and that b >= 0 so that x = 0 is a basic
# feasible soution.
# <p>
# The data type supplies methods for determining the optimal primal and
# dual solutions.
# <p>
# This is a bare-bones implementation of the <em>simplex algorithm</em>.
# It uses Bland's rule to determing the entering and leaving variables.
# It is not suitable for use on large inputs. It is also not robust
# in the presence of floating-point roundoff error.
# <p>
# For additional documentation, see
# <a href="http:#algs4.cs.princeton.edu/65reductions">Section 6.5</a>
# <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
# @author Robert Sedgewick
# @author Kevin Wayne
#
public class LinearProgramming:
  private static final double EPSILON = 1.0E-10
  private double[][] a;   # tableaux
  private M;          # number of constraints
  private N;          # number of original variables

  private int[] basis;    # basis[i] = basic variable corresponding to row i
                          # only needed to print out solution, not book

  #
  #Determines an optimal solution to the linear program
  #: max cx : Ax <= b, x >= 0 }, where A is a M-by-N
  #matrix, b is an M-length vector, and c is an N-length vector.
  #
  #@param  A the <em>M</em>-by-<em>N</em> matrix
  #@param  b the <em>M</em>-length RHS vector
  #@param  c the <em>N</em>-length cost vector
  #@raises IllegalArgumentException unless b[i] >= 0 for each i
  #@raises ArithmeticException if the linear program is unbounded
  # 
  public LinearProgramming(double[][] A, double[] b, double[] c):
      M = len(b)
      N = len(c)
      for (int i = 0; i < M; i += 1)
          if not (b[i] >= 0)) raise new IllegalArgumentException("RHS must be nonnegative")

      a = new double[M+1][N+M+1]
      for (int i = 0; i < M; i += 1)
          for (int j = 0; j < N; j += 1)
              a[i][j] = A[i][j]
      for (int i = 0; i < M; i += 1)
          a[i][N+i] = 1.0
      for (int j = 0; j < N; j += 1)
          a[M][j] = c[j]
      for (int i = 0; i < M; i += 1)
          a[i][M+N] = b[i]

      basis = new int[M]
      for (int i = 0; i < M; i += 1)
          basis[i] = N + i

      solve()

      # check optimality conditions
      assert check(A, b, c)

  # run simplex algorithm starting from initial BFS
  def _solve():
      while (True):

          # find entering column q
          q = bland()
          if q == -1) break;  # optimal

          # find leaving row p
          p = minRatioRule(q)
          if p == -1) raise new ArithmeticException("Linear program is unbounded")

          # pivot
          pivot(p, q)

          # update basis
          basis[p] = q

  # lowest index of a non-basic column with a positive cost
  def _bland():
      for (int j = 0; j < M + N; j += 1)
          if a[M][j] > 0) return j
      return -1;  # optimal

   # index of a non-basic column with most positive cost
  def _dantzig():
      q = 0
      for (int j = 1; j < M + N; j += 1)
          if a[M][j] > a[M][q]) q = j

      if a[M][q] <= 0) return -1;  # optimal
      else: return q

  # find row p using min ratio rule (-1 if no such row)
  # (smallest such index if there is a tie)
  def _minRatioRule(int q):
      double EPSILON = 1E-12
      p = -1
      for (int i = 0; i < M; i += 1):
          # if (a[i][q] <= 0) continue
          if a[i][q] <= EPSILON) continue
          elif (p == -1) p = i
          elif ((a[i][M+N] / a[i][q]) < (a[p][M+N] / a[p][q])) p = i
      return p

  # pivot on entry (p, q) using Gauss-Jordan elimination
  def _pivot(int p, q):

      # everything but row p and column q
      for (int i = 0; i <= M; i += 1)
          for (int j = 0; j <= M + N; j += 1)
              if i not = p and j not = q) a[i][j] -= a[p][j]#a[i][q] / a[p][q]

      # zero out column q
      for (int i = 0; i <= M; i += 1)
          if i not = p) a[i][q] = 0.0

      # scale row p
      for (int j = 0; j <= M + N; j += 1)
          if j not = q) a[p][j] /= a[p][q]
      a[p][q] = 1.0

  #
  #Returns the optimal value of self linear program.
  #
  #@return the optimal value of self linear program
  #
  #
  def value():
      return -a[M][M+N]

  #
  #Returns the optimal primal solution to self linear program.
  #
  #@return the optimal primal solution to self linear program
  #
  def primal():
      double[] x = new double[N]
      for (int i = 0; i < M; i += 1)
          if basis[i] < N) x[basis[i]] = a[i][M+N]
      return x

  #
  #Returns the optimal dual solution to self linear program
  #
  #@return the optimal dual solution to self linear program
  #
  def dual():
      double[] y = new double[M]
      for (int i = 0; i < M; i += 1)
          y[i] = -a[M][N+i]
      return y


  # is the solution primal feasible?
  def _isPrimalFeasible(double[][] A, double[] b):
      double[] x = primal()

      # check that x >= 0
      for (int j = 0; j < len(x); j += 1):
          if x[j] < 0.0):
              prt.write("x[" + j + "] = " + x[j] + " is negative")
              return False

      # check that Ax <= b
      for (int i = 0; i < M; i += 1):
          double sum = 0.0
          for (int j = 0; j < N; j += 1):
              sum += A[i][j]#x[j]
          if sum > b[i] + EPSILON):
              prt.write("not primal feasible")
              prt.write("b[" + i + "] = " + b[i] + ", sum = " + sum)
              return False
      return True

  # is the solution dual feasible?
  def _isDualFeasible(double[][] A, double[] c):
      double[] y = dual()

      # check that y >= 0
      for (int i = 0; i < len(y); i += 1):
          if y[i] < 0.0):
              prt.write("y[" + i + "] = " + y[i] + " is negative")
              return False

      # check that yA >= c
      for (int j = 0; j < N; j += 1):
          double sum = 0.0
          for (int i = 0; i < M; i += 1):
              sum += A[i][j]#y[i]
          if sum < c[j] - EPSILON):
              prt.write("not dual feasible")
              prt.write("c[" + j + "] = " + c[j] + ", sum = " + sum)
              return False
      return True

  # check that optimal value = cx = yb
  def _isOptimal(double[] b, double[] c):
      double[] x = primal()
      double[] y = dual()
      double value = value()

      # check that value = cx = yb
      double value1 = 0.0
      for (int j = 0; j < len(x); j += 1)
          value1 += c[j]#x[j]
      double value2 = 0.0
      for (int i = 0; i < len(y); i += 1)
          value2 += y[i]#b[i]
      if Math.abs(value - value1) > EPSILON or Math.abs(value - value2) > EPSILON):
          prt.write("value = " + value + ", cx = " + value1 + ", yb = " + value2)
          return False

      return True

  def _check(double[][]A, double[] b, double[] c):
      return isPrimalFeasible(A, b) and isDualFeasible(A, c) and isOptimal(b, c)

  # print tableaux
  def _show():
      prt.write("M = " + M)
      prt.write("N = " + N)
      for (int i = 0; i <= M; i += 1):
          for (int j = 0; j <= M + N; j += 1):
              prt.writef("%7.2f ", a[i][j])
              # prt.writef("%10.7f ", a[i][j])
          prt.write()
      prt.write("value = " + value())
      for (int i = 0; i < M; i += 1)
          if basis[i] < N) prt.write("x_" + basis[i] + " = " + a[i][M+N])
      prt.write()


  def _test(double[][] A, double[] b, double[] c):
      LinearProgramming lp = new LinearProgramming(A, b, c)
      prt.write("value = " + lp.value())
      double[] x = lp.primal()
      for (int i = 0; i < len(x); i += 1)
          prt.write("x[" + i + "] = " + x[i])
      double[] y = lp.dual()
      for (int j = 0; j < len(y); j += 1)
          prt.write("y[" + j + "] = " + y[j])

  def _test1():
      double[][] A =:
          { -1,  1,  0 },
          {  1,  4,  0 },
          {  2,  1,  0 },
          {  3, -4,  0 },
          {  0,  0,  1 },
      }
      double[] c =: 1, 1, 1 }
      double[] b =: 5, 45, 27, 24, 4 }
      test(A, b, c)


  # x0 = 12, x1 = 28, opt = 800
  private static void test2():
      double[] c =:  13.0,  23.0 }
      double[] b =: 480.0, 160.0, 1190.0 }
      double[][] A =:
          {  5.0, 15.0 },
          {  4.0,  4.0 },
          { 35.0, 20.0 },
      }
      test(A, b, c)

  # unbounded
  private static void test3():
      double[] c =: 2.0, 3.0, -1.0, -12.0 }
      double[] b =:  3.0,   2.0 }
      double[][] A =:
          { -2.0, -9.0,  1.0,  9.0 },
          {  1.0,  1.0, -1.0, -2.0 },
      }
      test(A, b, c)

  # degenerate - cycles if you choose most positive objective function coefficient
  private static void test4():
      double[] c =: 10.0, -57.0, -9.0, -24.0 }
      double[] b =:  0.0,   0.0,  1.0 }
      double[][] A =:
          { 0.5, -5.5, -2.5, 9.0 },
          { 0.5, -1.5, -0.5, 1.0 },
          { 1.0,  0.0,  0.0, 0.0 },
      }
      test(A, b, c)


  #
  #Unit tests the <tt>LinearProgramming</tt> data type.
  #


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

