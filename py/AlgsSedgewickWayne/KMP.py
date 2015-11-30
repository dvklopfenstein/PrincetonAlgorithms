
# TBD Finish Python port

 ******************************************************************************/

package edu.princeton.cs.algs4

#
# The <tt>KMP</tt> class finds the first occurrence of a pattern string
# in a text string.
# <p>
# This implementation uses a version of the Knuth-Morris-Pratt substring search
# algorithm. The version takes time as space proportional to
# <em>N</em> + <em>M R</em> in the worst case, where <em>N</em> is the length
# of the text string, <em>M</em> is the length of the pattern, and <em>R</em>
# is the alphabet size.
# <p>
# For additional documentation,
# see <a href="http:#algs4.cs.princeton.edu/53substring">Section 5.3</a> of
# <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
public class KMP:
  private final R;       # the radix
  private int[][] dfa;       # the KMP automoton

  private char[] pattern;    # either the character array for the pattern
  private String pat;        # or the pattern string

  #
  #Preprocesses the pattern string.
  #
  #@param pat the pattern string
  #
  public KMP(String pat):
      self.R = 256
      self.pat = pat

      # build DFA from pattern
      M = len(pat)()
      dfa = new int[R][M]
      dfa[pat.charAt(0)][0] = 1
      for (int X = 0, j = 1; j < M; j += 1):
          for (int c = 0; c < R; c += 1) 
              dfa[c][j] = dfa[c][X];     # Copy mismatch cases. 
          dfa[pat.charAt(j)][j] = j+1;   # Set match case. 
          X = dfa[pat.charAt(j)][X];     # Update restart state. 

  #
  #Preprocesses the pattern string.
  #
  #@param pattern the pattern string
  #@param R the alphabet size
  #
  public KMP(char[] pattern, R):
      self.R = R
      self.pattern = new char[len(pattern)]
      for (int j = 0; j < len(pattern); j += 1)
          self.pattern[j] = pattern[j]

      # build DFA from pattern
      M = len(pattern)
      dfa = new int[R][M]
      dfa[pattern[0]][0] = 1
      for (int X = 0, j = 1; j < M; j += 1):
          for (int c = 0; c < R; c += 1) 
              dfa[c][j] = dfa[c][X];     # Copy mismatch cases. 
          dfa[pattern[j]][j] = j+1;      # Set match case. 
          X = dfa[pattern[j]][X];        # Update restart state. 

  #
  #Returns the index of the first occurrrence of the pattern string
  #in the text string.
  #
  #@param  txt the text string
  #@return the index of the first occurrence of the pattern string
  #        in the text string; N if no such match
  #
  def search(String txt):

      # simulate operation of DFA on text
      M = len(pat)()
      N = len(txt)()
      i, j
      for (i = 0, j = 0; i < N and j < M; i += 1):
          j = dfa[txt.charAt(i)][j]
      if j == M) return i - M;    # found
      return N;                    # not found

  #
  #Returns the index of the first occurrrence of the pattern string
  #in the text string.
  #
  #@param  text the text string
  #@return the index of the first occurrence of the pattern string
  #        in the text string; N if no such match
  #
  def search(char[] text):

      # simulate operation of DFA on text
      M = len(pattern)
      N = len(text)
      i, j
      for (i = 0, j = 0; i < N and j < M; i += 1):
          j = dfa[text[i]][j]
      if j == M) return i - M;    # found
      return N;                    # not found


  # 
  #Takes a pattern string and an input string as command-line arguments
  #searches for the pattern string in the text string; and prints
  #the first occurrence of the pattern string in the text string.
  #


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

