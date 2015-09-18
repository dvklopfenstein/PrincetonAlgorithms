#!/usr/bin/env python

import sys

def run_277853s():
  N = 1
  while N<16384:
    run_277853(N)
    N = N*2

def run_277853(N):
  cnt = 0
  #for (int i = 1; i*i <= N; i = i*2)
  i = 1
  while i*i <= N:
    cnt += 1
    print N, i, cnt
    i = i*4
  #print "{:>5}=N {:>5}=cnt".format(N, cnt)

def run_605062s():
  N = 1
  while N<4096:
    run_605062(N)
    N = N*2

def run_605062(N):
  """N^(1/2).
     The body of inner loop is executed 1 + 2 + 4 + 8 + ... + sqrt(N) ~ 2 sqrt(N)
  """
  cnt = 0
  #for (int i = 1; i*i <= N; i = i*2)
  i = 1
  while i <= N:
    #for (int j = 0; j < i; j++)
    for j in range(i):
      cnt += 1
      #print i, j, cnt
    #print i
    i = i*2
  print "{:>5}=N {:>5}=cnt".format(N, cnt)

if __name__ == '__main__':
  run_277853s()
