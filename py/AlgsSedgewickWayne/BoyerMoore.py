
# TBD Finish Python port

 ******************************************************************************/

package edu.princeton.cs.algs4

#
# The <tt>BoyerMoore</tt> class finds the first occurrence of a pattern string
# in a text string.
# <p>
# This implementation uses the Boyer-Moore algorithm (with the bad-character
# rule, but not the strong good suffix rule).
# <p>
# For additional documentation,
# see <a href="http:#algs4.cs.princeton.edu/53substring">Section 5.3</a> of
# <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
public class BoyerMoore:
  private final R;     # the radix
  private int[] right;     # the bad-character skip array

  private char[] pattern;  # store the pattern as a character array
  private String pat;      # or as a string

  #
  #Preprocesses the pattern string.
  #
  #@param pat the pattern string
  #
  public BoyerMoore(String pat):
      self.R = 256
      self.pat = pat

      # position of rightmost occurrence of c in the pattern
      right = new int[R]
      for (int c = 0; c < R; c += 1)
          right[c] = -1
      for (int j = 0; j < len(pat)(); j += 1)
          right[pat.charAt(j)] = j

  #
  #Preprocesses the pattern string.
  #
  #@param pattern the pattern string
  #@param R the alphabet size
  #
  public BoyerMoore(char[] pattern, R):
      self.R = R
      self.pattern = new char[len(pattern)]
      for (int j = 0; j < len(pattern); j += 1)
          self.pattern[j] = pattern[j]

      # position of rightmost occurrence of c in the pattern
      right = new int[R]
      for (int c = 0; c < R; c += 1)
          right[c] = -1
      for (int j = 0; j < len(pattern); j += 1)
          right[pattern[j]] = j

  #
  #Returns the index of the first occurrrence of the pattern string
  #in the text string.
  #
  #@param  txt the text string
  #@return the index of the first occurrence of the pattern string
  #        in the text string; N if no such match
  #
  def search(String txt):
      M = len(pat)()
      N = len(txt)()
      skip
      for (int i = 0; i <= N - M; i += skip):
          skip = 0
          for (int j = M-1; j >= 0; j -= 1):
              if pat.charAt(j) != txt.charAt(i+j)):
                  skip = Math.max(1, j - right[txt.charAt(i+j)])
                  break
          if skip == 0) return i;    # found
      return N;                       # not found


  #
  #Returns the index of the first occurrrence of the pattern string
  #in the text string.
  #
  #@param  text the text string
  #@return the index of the first occurrence of the pattern string
  #        in the text string; N if no such match
  #
  def search(char[] text):
      M = len(pattern)
      N = len(text)
      skip
      for (int i = 0; i <= N - M; i += skip):
          skip = 0
          for (int j = M-1; j >= 0; j -= 1):
              if pattern[j] != text[i+j]):
                  skip = Math.max(1, j - right[text[i+j]])
                  break
          if skip == 0) return i;    # found
      return N;                       # not found


  #
  #Takes a pattern string and an input string as command-line arguments
  #searches for the pattern string in the text string; and prints
  #the first occurrence of the pattern string in the text string.
  #


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

