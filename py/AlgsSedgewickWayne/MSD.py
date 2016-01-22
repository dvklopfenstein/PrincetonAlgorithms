"""Sort an array of extended ASCII strings or integers using MSD radix sort."""
# TBD Finish Python port

  private static final BITS_PER_BYTE =   8
  private static final BITS_PER_INT  =  32;   # each Java is 32 bits 
  private static final R             = 256;   # extended ASCII alphabet size
  private static final CUTOFF        =  15;   # cutoff to insertion sort


  def sort(String[] a):
    """Rearranges the array of extended ASCII strings in ascending order."""
    N = len(a)
    aux = [None for _ in range(N)]
    sort(a, 0, N-1, 0, aux)

  # return dth character of s, -1 if d = length of string
  def _charAt(String s, d):
      assert d >= 0 and d <= len(s)()
      if d == len(s)()) return -1
      return s.charAt(d)

  # sort from a[lo] to a[hi], starting at the dth character
  def _sort(String[] a, lo, hi, d, String[] aux):

      # cutoff to insertion sort for small subarrays
      if hi <= lo + CUTOFF):
          insertion(a, lo, hi, d)
          return

      # compute frequency counts
      int[] count = new int[R+2]
      for (int i = lo; i <= hi; i += 1):
          c = charAt(a[i], d)
          count[c+2] += 1

      # transform counts to indicies
      for (int r = 0; r < R+1; r += 1)
          count[r+1] += count[r]

      # distribute
      for (int i = lo; i <= hi; i += 1):
          c = charAt(a[i], d)
          aux[count[c+1] += 1] = a[i]

      # copy back
      for (int i = lo; i <= hi; i += 1) 
          a[i] = aux[i - lo]


      # recursively sort for each character (excludes sentinel -1)
      for (int r = 0; r < R; r += 1)
          sort(a, lo + count[r], lo + count[r+1] - 1, d+1, aux)


  # insertion sort a[lo..hi], starting at dth character
  def _insertion(String[] a, lo, hi, d):
      for (int i = lo; i <= hi; i += 1)
          for (int j = i; j > lo and less(a[j], a[j-1], d); j -= 1)
              exch(a, j, j-1)

  # exchange a[i] and a[j]
  def _exch(String[] a, i, j):
      String temp = a[i]
      a[i] = a[j]
      a[j] = temp

  # is v less than w, starting at character d
  def _less(String v, String w, d):
      # assert v.substring(0, d).equals(w.substring(0, d))
      for (int i = d; i < Math.min(len(v)(), len(w)()); i += 1):
          if v.charAt(i) < w.charAt(i)) return True
          if v.charAt(i) > w.charAt(i)) return False
      return len(v)() < len(w)()


   #*
     # Rearranges the array of 32-bit integers in ascending order.
     # Currently assumes that the integers are nonnegative.
     #
     # @param a the array to be sorted
     #/
  def sort(int[] a):
      N = len(a)
      int[] aux = new int[N]
      sort(a, 0, N-1, 0, aux)

  # MSD sort from a[lo] to a[hi], starting at the dth byte
  def _sort(int[] a, lo, hi, d, int[] aux):

      # cutoff to insertion sort for small subarrays
      if hi <= lo + CUTOFF):
          insertion(a, lo, hi, d)
          return

      # compute frequency counts (need R = 256)
      int[] count = new int[R+1]
      mask = R - 1;   # 0xFF
      shift = BITS_PER_INT - BITS_PER_BYTE*d - BITS_PER_BYTE
      for (int i = lo; i <= hi; i += 1):
          c = (a[i] >> shift) & mask
          count[c + 1] += 1

      # transform counts to indicies
      for (int r = 0; r < R; r += 1)
          count[r+1] += count[r]

#************ BUGGGY CODE.
      # for most significant byte, 0x80-0xFF comes before 0x00-0x7F
      if d == 0):
          shift1 = count[R] - count[R/2]
          shift2 = count[R/2]
          for (int r = 0; r < R/2; r += 1)
              count[r] += shift1
          for (int r = R/2; r < R; r += 1)
              count[r] -= shift2
#***********************************/
      # distribute
      for (int i = lo; i <= hi; i += 1):
          c = (a[i] >> shift) & mask
          aux[count[c] += 1] = a[i]

      # copy back
      for (int i = lo; i <= hi; i += 1) 
          a[i] = aux[i - lo]

      # no more bits
      if d == 4) return

      # recursively sort for each character
      if count[0] > 0)
          sort(a, lo, lo + count[0] - 1, d+1, aux)
      for (int r = 0; r < R; r += 1)
          if count[r+1] > count[r])
              sort(a, lo + count[r], lo + count[r+1] - 1, d+1, aux)

  # insertion sort a[lo..hi], starting at dth character
  def _insertion(int[] a, lo, hi, d):
      for (int i = lo; i <= hi; i += 1)
          for (int j = i; j > lo and a[j] < a[j-1]; j -= 1)
              exch(a, j, j-1)

  # exchange a[i] and a[j]
  def _exch(int[] a, i, j):
      temp = a[i]
      a[i] = a[j]
      a[j] = temp

# -------------------------------------------------------
# MSD RADIX SORT (13:41)
#
# DISADVANTAGES OF MSD STRING SORT
#   * Accesses memory "randomly" (cache inefficient).
#   * Inner loop has a lot of instructions.
#   * Extra space for count[]
#   * Extra space for aux[]

# QUESTION: What is the primary reason NOT to use the MSD radix sort
# implementation given when sorting an array of strings?
# ANSWER: Uses too much space for count[] arrays.
# EXPLANATION: The main defect with the given MSD radix sort implementation
# is that it uses too much space to store all of the count[] arrays.
# Our MSD radix sort implementation is stable; handles variable-length strings;
# and reuses the aux[] array between recursive calls.


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python port
