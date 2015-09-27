#!/usr/bin/env python

import sys
import time

def runit(N):
  # What is the order of growth of the worst case running time of the
  # following code fragment as a function of N?
  #
  # N^2 + (N-1)^2 + (N-2)^2 + ... + 1
  sum = 0
  # for (int i = N; i > 0; i--)
  for i in range(N,0,-1):
      # for (int j = 0; j < i; j++)
      for j in range(i):
          #print i, j, sum
          sum += 1

def time_runit():
  for N in range(5):
    #start = time.clock()
    #runit(N)
    #print "N", N, " TIME", time.clock() - start

def getN():
  for arg in sys.argv[1:]:
    if arg.isdigit():
      return int(arg)
  raise Exception("N WAS NOT PROVIDED")

if __name__ == '__main__': 
  time_runit()

