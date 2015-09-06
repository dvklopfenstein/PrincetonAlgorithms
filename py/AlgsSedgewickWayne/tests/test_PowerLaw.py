#!/usr/bin/env python
"""For determining co-efficient b in PowerLaw"""

from AlgsSedgewickWayne.PowerLaw import getData
from AlgsSedgewickWayne.PowerLaw import est_b
from AlgsSedgewickWayne.PowerLaw import solve_a
from AlgsSedgewickWayne.PowerLaw import do_plot


def test_Lecture_Observations_Question():
  """Question from the end of the Week 1 Lecture, Observations.

     EXPLANATION: We assume T(N) = aN^b for some constants a and b.
     As we double the size of the input N, the running time
     approximately quadruples, indicating a algorithm or b=2.
     Plugging in T(64,000) = 20.5 and solving for a, we obtain
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
  b = est_b(data)
  a = solve_a(data, b)
  do_plot(data, a, b)



def test_week1_ex_Q1_398112(): # Lecture: Quick-Union Improvements 1:22
  """seed = 398112 """
  # estimate b: 7:58
  #        N   seconds
  # -------------------
  strData = """
      128     0.000
      256     0.001
      512     0.006
     1024     0.029
     2048     0.158
     4096     0.852
     8192     4.561
    16384    24.586
    32768   129.467
    65536   697.828
   131072  3730.438
  """
  data = getData(strData)
  est_b(data)

def test_week1_ex_Q1_990354(): # Lecture: Quick-Union Improvements 1:22
  """seed = 990354 """
  # estimate b: 7:58
  #        N   seconds
  # -------------------
  strData = """
      256     0.000
      512     0.001
     1024     0.005
     2048     0.022
     4096     0.099
     8192     0.467
    16384     2.133
    32768     9.998
    65536    46.309
   131072   214.246
   262144   998.222
   524288  4622.897
  """
  data = getData(strData)
  est_b(data)

def test_week1_ex_Q1_130450(): # Lecture: Quick-Union Improvements 1:22
  """seed = 130450 """
  # estimate b: 7:58
  #        N   seconds
  # -------------------
  strData = """
       1024     0.000
       2048     0.001
       4096     0.003
       8192     0.013
      16384     0.053
      32768     0.227
      65536     0.953
     131072     3.998
     262144    16.756
     524288    70.385
    1048576   295.766
    2097152  1243.879
  """
  data = getData(strData)
  est_b(data)

def test_week1_exercise_Q1(): # Lecture: Quick-Union Improvements 1:22
  """seed = 254585 """
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
  b = est_b(data)
  a = solve_a(data, b)
  do_plot(data, a, b)

def test_week1_exercise_Q1b(): # Lecture: Quick-Union Improvements 1:22
  """seed = 686658 """
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
  b = est_b(data)
  solve_a(data, b)

def test_week1_exercise_Q1c(): # Lecture: Quick-Union Improvements 1:22
  """seed = 410426 """
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
  b = est_b(data)
  solve_a(data, b)

def test_week1_exercise_Q1d(): # Lecture: Quick-Union Improvements 1:22
  """seed = 262435 """
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
  b = est_b(data)
  solve_a(data, b)


def test_week1_exerciseA_Q1():
  """seed = 331534 """
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
  b = est_b(data)
  solve_a(data, b)

def test_week1_exerciseA_Q2():
  """seed = 331534 """
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
  b = est_b(data)
  solve_a(data, b)


if __name__ == '__main__':
  test_week1_exercise_Q1d()
