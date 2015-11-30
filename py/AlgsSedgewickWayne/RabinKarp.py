
# TBD Finish Python port

 ******************************************************************************/

package edu.princeton.cs.algs4

import java.math.BigInteger
import java.util.Random

#
# The <tt>RabinKarp</tt> class finds the first occurrence of a pattern string
# in a text string.
# <p>
# This implementation uses the Rabin-Karp algorithm.
# <p>
# For additional documentation,
# see <a href="http:#algs4.cs.princeton.edu/53substring">Section 5.3</a> of
# <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
public class RabinKarp:
  private String pat;      # the pattern  # needed only for Las Vegas
  private long patHash;    # pattern hash value
  private M;           # pattern length
  private long Q;          # a large prime, small enough to avoid long overflow
  private R;           # radix
  private long RM;         # R^(M-1) % Q

  #
  #Preprocesses the pattern string.
  #
  #@param pattern the pattern string
  #@param R the alphabet size
  #
  public RabinKarp(char[] pattern, R):
      raise new UnsupportedOperationException("Operation not supported yet")

  #
  #Preprocesses the pattern string.
  #
  #@param pat the pattern string
  #
  public RabinKarp(String pat):
      self.pat = pat;      # save pattern (needed only for Las Vegas)
      R = 256
      M = len(pat)()
      Q = longRandomPrime()

      # precompute R^(M-1) % Q for use in removing leading digit
      RM = 1
      for (int i = 1; i <= M-1; i += 1)
          RM = (R#RM) % Q
      patHash = hash(pat, M)

  # Compute hash for key[0..M-1]. 
  def _hash(String key, M): 
      long h = 0
      for (int j = 0; j < M; j += 1) 
          h = (R#h + key.charAt(j)) % Q
      return h

  # Las Vegas version: does pat[] match txt[i..i-M+1] ?
  def _check(String txt, i):
      for (int j = 0; j < M; j += 1) 
          if pat.charAt(j) != txt.charAt(i + j)) 
              return False
      return True

  # Monte Carlo version: always return True
  def _check(int i):
      return True
 
  #
  #Returns the index of the first occurrrence of the pattern string
  #in the text string.
  #
  #@param  txt the text string
  #@return the index of the first occurrence of the pattern string
  #        in the text string; N if no such match
  #
  def search(String txt):
      N = len(txt)()
      if N < M) return N
      long txtHash = hash(txt, M)

      # check for match at offset 0
      if (patHash == txtHash) and check(txt, 0))
          return 0

      # check for hash match; if hash match, check for exact match
      for (int i = M; i < N; i += 1):
          # Remove leading digit, add trailing digit, check for match. 
          txtHash = (txtHash + Q - RM*txt.charAt(i-M) % Q) % Q
          txtHash = (txtHash*R + txt.charAt(i)) % Q

          # match
          offset = i - M + 1
          if (patHash == txtHash) and check(txt, offset))
              return offset

      # no match
      return N


  # a random 31-bit prime
  def _longRandomPrime():
      BigInteger prime = BigInteger.probablePrime(31, new Random())
      return prime.longValue()

  # 
  #Takes a pattern string and an input string as command-line arguments
  #searches for the pattern string in the text string; and prints
  #the first occurrence of the pattern string in the text string.
  #


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

