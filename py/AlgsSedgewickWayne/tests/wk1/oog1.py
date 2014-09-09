#!/usr/bin/python

# (seed = 435338)
# What is the order of growth of the worst case running time of the following code fragment
# as a function of N?

import sys

def run(N):
  N_sqr = N*N
  sum = 0
  i = 1
  #for (int i = 1; i <= N*N; i = i*2)
  while i <= N_sqr:
    # for (int j = 0; j < i; j++)
    for j in range(i):
      sys.stdout.write('N={} N^2={} {:4}=i {:4}=j\n'.format(N, N_sqr, i, j))
      sum += 1
    i = i * 2
  sys.stdout.write('{:3} {:5} {:5}=N^2 {:5.2f}=N^(1/2)\n'.format(
    N, sum, pow(N,2), N**(1/2.0)))

if __name__ == '__main__': 
  run(1)
  run(2)
  run(4)
  run(8)
  #run(16)
  #run(32)
  #run(64)
  #run(128)

# ANSWER: N^2
# EXMPLANATION: The body of the innermost loop executes:
# 1 + 2 + 4 + 8 + ... + N^2 ~ 2 N^2 times
