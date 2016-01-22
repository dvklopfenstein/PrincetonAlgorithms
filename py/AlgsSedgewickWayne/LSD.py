"""sorting an array of W-character strings or 32-bit integers using LSD radix sort."""
# TBD Finish Python port

import collections as cx
import numpy as np

def key_idx_cnt(a):
  """Rearranges the array of W-character strings in ascending order."""
  N = len(a)
  R = 256   # extend ASCII alphabet size
  aux = [None for _ in range(N+1)]

  # compute frequency counts
  words, count = [list(v) for v in zip(*sorted(cx.Counter(a).most_common()))]

  # compute cumulates
  count = np.cumsum(count)

  # move data
  for i, (word, cnt) in enumerate(zip(words, count)):
    aux[cnt] = word
    count[i] += 1

  # copy back
  for i, v in enumerate(aux[1:]): 
    a[i] = v

# #*
#   # Rearranges the array of 32-bit integers in ascending order.
#   # This is about 2-3x faster than Arrays.sort().
#   #
#   # @param a the array to be sorted
#   #/
#def sort(int[] a):
#    BITS = 32;                 # each is 32 bits 
#    W = BITS / BITS_PER_BYTE;  # each is 4 bytes
#    R = 1 << BITS_PER_BYTE;    # each bytes is between 0 and 255
#    MASK = R - 1;              # 0xFF
#
#    N = len(a)
#    int[] aux = new int[N]
#
#    for (int d = 0; d < W; d += 1):         
#
#        # compute frequency counts
#        int[] count = new int[R+1]
#        for (int i = 0; i < N; i += 1):           
#            c = (a[i] >> BITS_PER_BYTE*d) & MASK
#            count[c + 1] += 1
#
#        # compute cumulates
#        for (int r = 0; r < R; r += 1)
#            count[r+1] += count[r]
#
#        # for most significant byte, 0x80-0xFF comes before 0x00-0x7F
#        if d == W-1):
#            shift1 = count[R] - count[R/2]
#            shift2 = count[R/2]
#            for (int r = 0; r < R/2; r += 1)
#                count[r] += shift1
#            for (int r = R/2; r < R; r += 1)
#                count[r] -= shift2
#
#        # move data
#        for (int i = 0; i < N; i += 1):
#            c = (a[i] >> BITS_PER_BYTE*d) & MASK
#            aux[count[c] += 1] = a[i]
#
#        # copy back
#        for (int i = 0; i < N; i += 1)
#            a[i] = aux[i]

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
