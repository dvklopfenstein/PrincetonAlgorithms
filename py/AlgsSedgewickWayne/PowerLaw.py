#!/usr/bin/env python

# https://class.coursera.org/algs4partI-005
# Algorithms, Part 1 by Kevin Wayne, Robert Sedgewick at Princeton University
# Week 1 "Quick Union Improvements(13:02) lecture at 4:03

# Week 1 Analysis of Algoithms Introduction (8:14)
# Scientific Method
#   * Observe some feature of the natural world (Computer itself)
#   * Hypothesize a model that is consistent with the observations
#   * Predict events using the hypothesis
#   * Verify the predictions by making further observations
#   * Validate by repeating until the hypothesis and observations agree.
# 
# Principles:
#   * Experiments must be reproducible
#   * Hypothesis must be falsifiable

#   Why is my program so slow?
#   Why does it run out of memory?
#   
#   N^2 unacceptable because it does not scale
#   N*log(N) is almost linear
#   
# Suppose that N =1,000,000. Approximately how much faster is an algorithm that
# performs N*lg(N) operations versus one that performs N^2 operations? Recall that
# lg is log_2.
#   N^2     = (10^6)^2  =   10^12  -> .5*10^5 = (.5)*10^1)*(10^4) = 5*10000 = 50,000!!!
#   M*lg(N) = 10^6*(20) = 2*10^7

# Week 1 Observations (10:05)
# Power Law: a*N^b (06:22)
#   Math for straight-line in log-log plots with Power Law:
#     lg(T(N)) = b*lg(N) + c
#     T(N) = a*N^b, where a = 2^c

import re
import sys
import math
import pylab as plt
from matplotlib.lines import Line2D
import unittest


def getData( blktxt ):
  data = []
  txt = blktxt.split('\n')
  for T in txt:
    M = re.search(r'^\s*(\d+)\s+(\d+\.\d+)',T)
    if M:
      data.append([int(M.group(1)), float(M.group(2))])
  return data

def est_b( data ):
  """Doubling hypothesis: Quick way to estimate b in a power-law relationship.
  
  HYPOTHESIS: Running time is about a*N^b with b = lg(ratio)

  CAVEAT: Cannot identify logarithmic factors with doubling hypothesis.
  """
  prev = data[0]
  for D in data[1:]:
    if D[0] == 2*prev[0]:
      if prev[1] != 0: 
        ratio = D[1]/prev[1]
        lg_ratio = math.log(ratio,2)
        sys.stdout.write('%10d %7.3f ratio=%7.3f lg(ratio)=%7.3f\n'%(D[0], D[1], ratio, lg_ratio))
      prev = D
    else:
      raise Exception("DATA IS NOT DOUBLED")
  return lg_ratio
 
def solve_a(data, b):
  """Solve for a once b is known with T(N)=a*N^b (08:36)."""
  for D in data:
    #a = D[1]/(float(D[0])**b)
    a = (float(D[0])**b)
    sys.stdout.write('DATA:%10d %7.3f FORMULA: a(%e)*N(%10d)^b(%7.3f)\n'%(D[0], D[1], a, D[0], b))

def do_plot(data, a, b):
  print Line2D.markers
  fig, ax = plt.subplots()
  X, Y = zip(*data)
  plt.plot(X,Y,'b-o')
  ax.set_xlabel('Running Time')
  ax.set_ylabel('Size of Input')
  ax.set_title('Running Time Growth')
  plt.show()

class PowerLaw_Tests(unittest.TestCase):

  def test_week1_exercise_Q1(self): # Lecture: Quick-Union Improvements 1:22
    # seed = 254585
    # estimate b: 7:58
    #        N   seconds
    # -------------------
    strData = """
          16384     0.000
          32768     0.001
          65536     0.001
         131072     0.004
         262144     0.009
         524288     0.023
        1048576     0.059
        2097152     0.152
        4194304     0.389
        8388608     0.996
       16777216     2.553
       33554432     6.540
       67108864    16.756
      134217728    42.927
      268435456   109.962
      536870912   281.688
    """
    data = getData(strData) 
    b = est_b( data )
    a = solve_a( data, b )
    #do_plot(data, a, b)
    #self.failUnless( o.ID == [6,2,6,4,6,6,6,2,4,4] )

  def test_week1_exercise_Q1b(self): # Lecture: Quick-Union Improvements 1:22
    # seed = 686658
    #         N   seconds
    # -------------------
    strData = """
           64     0.001
          128     0.006
          256     0.072
          512     0.713
         1024     6.837
         2048    68.530
         4096   666.576
         8192  6594.977
    """
    data = getData(strData) 
    b = est_b( data )
    a = solve_a( data, b )

  def test_week1_exercise_Q1c(self): # Lecture: Quick-Union Improvements 1:22
    print "\ntest_week1_exercise_Q1c"
    # (seed = 410426)
    #         N   seconds
    # -------------------
    strData = """
        32768     0.000
        65536     0.000
       131072     0.001
       262144     0.003
       524288     0.008
      1048576     0.022
      2097152     0.057
      4194304     0.148
      8388608     0.386
     16777216     1.008
     33554432     2.632
     67108864     6.872
    134217728    17.944
    268435456    46.850
    536870912   122.325
    """
    data = getData(strData) 
    b = est_b( data )
    a = solve_a( data, b )

  def test_week1_exercise_Q1d(self): # Lecture: Quick-Union Improvements 1:22
    print "\ntest_week1_exercise_Q1d"
    # (seed = 262435)
    #         N   seconds
    # -------------------
    strData = """
       256     0.000
       512     0.001
      1024     0.005
      2048     0.028
      4096     0.146
      8192     0.812
     16384     4.448
     32768    24.280
     65536   134.049
    131072   728.101
    262144  3978.674
    """
    data = getData(strData) 
    b = est_b( data )
    a = solve_a( data, b )

def main():
  unittest.main()

if __name__ == '__main__':
  main()
