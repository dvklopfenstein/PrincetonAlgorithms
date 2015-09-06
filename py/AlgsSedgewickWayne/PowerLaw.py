"""For determining a formula for the runtime of a program."""

import re
import sys
import math
import pylab as plt
import numpy as np

def getData(blktxt):
  """Given a block of text with data on each line, return the numeric data.
        4096     0.003
        8192     0.013
       16384     0.053
       32768     0.227
  """
  data = []
  lines = blktxt.split('\n')
  for txt in lines:
    M = re.search(r'^\s*(\d+)\s+(\d+\.\d+)', txt)
    if M:
      data.append([int(M.group(1)), float(M.group(2))])
  return data

def est_b(data, prt=sys.stdout):
  """Doubling hypothesis: Quick way to estimate b in a power-law relationship.

  HYPOTHESIS: Running time is about a*N^b with b = lg(ratio)

  CAVEAT: Cannot identify logarithmic factors with doubling hypothesis.
  """
  lg_ratio = None
  prev = data[0]
  for D in data[1:]:
    if D[0] == 2*prev[0]:
      if prev[1] != 0:
        ratio = D[1]/prev[1]
        lg_ratio = math.log(ratio, 2)
        prt.write('{:10d} {:7.3f} ratio={:7.3f} lg(ratio)={:7.3f}\n'.format(
            D[0], D[1], ratio, lg_ratio))
      prev = D
    else:
      raise Exception("DATA IS NOT DOUBLED")
  return lg_ratio

def solve_a(data, b, prt=sys.stdout):
  """Solve for a once b is known with T(N)=a*N^b (08:36)."""
  a = []
  for D in data:
    ##a = D[1]/(float(D[0])**b)
    a.append(1/(float(D[0])**b))
    prt.write('DATA:{D:10d} {T:7.3f} FORMULA: a({a:e})*N({D:10d})^b({b:7.3f})\n'.format(
        D=D[0], T=D[1], a=a[-1], b=b))
  return sum(a)/len(a)
  ##if len(a) > 2:
  ##  return sum(a[2:])/(len(a)-2)
  ##return a[-1]

def do_plot(data, a, b):
  """Create a plot."""
  fig, ax = plt.subplots()
  X, Y = zip(*data)
  plt.plot(X, Y, 'b-o', label="data")
  X = np.linspace(0, data[-1][0], 1000)
  # print a, b
  Y = a*np.power(X, b)
  plt.plot(X, Y, 'g-', label="a*X^b")
  ax.set_xlabel('Running Time')
  ax.set_ylabel('Size of Input')
  ax.set_title('Running Time Growth')
  ax.legend()
  plt.show()

# Algorithms, Part 1 by Kevin Wayne, Robert Sedgewick at Princeton University
# Lecture Week 1 Analysis of Algorithms Introduction (8:14)

# 07:19 SCIENTIFIC METHOD
#   * OBSERVE     some feature of the natural world (Computer itself)
#   * HYPOTHESIZE a model that is consistent with the observations
#   * PREDICT     events using the hypothesis
#   * VERIFY      the predictions by making further observations
#   * VALIDATE    by repeating until the hypothesis and observations agree.
#
# Principles:
#   * Experiments must be REPRODUCIBLE
#   * Hypothesis  must be FALSIFIABLE

#   Why is my program so slow?
#   Why does it run out of memory?
#
#   N^2 unacceptable because it does not scale
#   N*log(N) is almost linear
#
# QUESTION: Suppose that N == 1,000,000. Approximately how much faster is
# an algorithm that performs N*lg(N) operations versus one that performs
# N^2 operations? Recall that lg is log_2.
#   N^2     = (10^6)^2  =   10^12
#   N*lg(N) = 10^6*(20) = 2*10^7
#
# N^2        10^12
# ------ = ------- =  .5(10^5) = 5(10^-1)(10^5) = 5(10^4) = 5*10000 = 50,000
# N lg N   2*10^7

# Week 1 Observations (10:05)
# Power Law: a*N^b (06:22)
#   Math for straight-line in log-log plots with Power Law:
#     lg(T(N)) = b*lg(N) + c
#     T(N) = a*N^b, where a = 2^c

