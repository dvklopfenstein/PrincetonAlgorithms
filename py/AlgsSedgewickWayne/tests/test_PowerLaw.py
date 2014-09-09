#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.PowerLaw import *

class PowerLaw_Tests(unittest.TestCase):

  def test_Lecture_Observations_Question(self):
    """Question from the end of the Week 1 Lecture, Observations.

       EXPLANATION: We assume T(N) = sN^b for some constants a and b.
       As we double the size of the input N, the running time 
       approximately quadruples, indicating a algorithm or b=2.
       Plugging in T(54,000) = 20.5 and solving for a, we obtain
       a = 20.5/64,000^2 ~ 5.0 x 10-9
    """
    strData = """
       1000  0.0
       2000  0.0
       4000  0.1
       8000  0.3
      16000  1.3
      32000  5.1
      64000 20.5
    """
    data = getData(strData)
    b = est_b( data )
    a = solve_a( data, b )
    #do_plot(data, a, b)

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


  def test_week1_exerciseA_Q1(self): 
    print "\ntest_week1_exerciseA_Q1"
    # (seed = 331534)
    #         N   seconds
    # -------------------
    strData = """
      64     0.001
      128     0.008
      256     0.062
      512     0.564
     1024     5.092
     2048    48.765
     4096   439.291
     8192  3998.962
    """
    data = getData(strData) 
    b = est_b( data )
    a = solve_a( data, b )

  def test_week1_exerciseA_Q2(self): 
    print "\ntest_week1_exerciseA_Q2"
    # (seed = 331534)
    #         N   seconds
    # -------------------
    strData = """
       2     7.000 
       4    31.000 
       8   127.000 
      16   511.000 
      32  2047.000 
      64  8191.000 
     128 32767.000 
    """
    data = getData(strData) 
    b = est_b( data )
    a = solve_a( data, b )




if __name__ == '__main__':
  unittest.main()
