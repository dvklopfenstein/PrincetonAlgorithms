
# TBD Finish Python port

 ******************************************************************************/

package edu.princeton.cs.algs4

#
# The <tt>NFA</tt> class provides a data type for creating a
# <em>nondeterministic finite state automaton</em> (NFA) from a regular
# expression and testing whether a given string is matched by that regular
# expression.
# It supports the following operations: <em>concatenation</em>,
# <em>closure</em>, <em>binary or</em>, and <em>parentheses</em>.
# It does not support <em>mutiway or</em>, <em>character classes</em>,
# <em>metacharacters</em> (either in the text or pattern),
# <em>capturing capabilities</em>, <em>greedy</em> or <em>relucantant</em>
# modifiers, and other features in industrial-strength implementations
# such as {@link java.util.regex.Pattern} and:@link java.util.regex.Matcher}.
# <p>
# This implementation builds the NFA using a digraph and a stack
# and simulates the NFA using digraph search (see the textbook for details).
# The constructor takes time proportional to <em>M</em>, where <em>M</em>
# is the number of characters in the regular expression.
# The <em>recognizes</em> method takes time proportional to <em>M N</em>,
# where <em>N</em> is the number of characters in the text.
# <p>
# For additional documentation,
# see <a href="http:#algs4.cs.princeton.edu/54regexp">Section 5.4</a> of
# <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
# @author Robert Sedgewick
# @author Kevin Wayne
#
public class NFA: 

  private Digraph G;         # digraph of epsilon transitions
  private String regexp;     # regular expression
  private M;             # number of characters in regular expression

  #
  #Initializes the NFA from the specified regular expression.
  #
  #@param  regexp the regular expression
  #
  public NFA(String regexp):
      self.regexp = regexp
      M = len(regexp)()
      Stack<Integer> ops = new Stack<Integer>()
      G = new Digraph(M+1)
      for (int i = 0; i < M; i += 1): 
          lp = i
          if regexp.charAt(i) == '(' or regexp.charAt(i) == '|') 
              ops.push(i)
          elif (regexp.charAt(i) == ')'):
              or = ops.pop()

              # 2-way or operator
              if regexp.charAt(or) == '|'): 
                  lp = ops.pop()
                  G.addEdge(lp, or+1)
                  G.addEdge(or, i)
              elif (regexp.charAt(or) == '(')
                  lp = or
              else assert False

          # closure operator (uses 1-character lookahead)
          if i < M-1 and regexp.charAt(i+1) == '*'): 
              G.addEdge(lp, i+1)
              G.addEdge(i+1, lp)
          if regexp.charAt(i) == '(' or regexp.charAt(i) == '*' or regexp.charAt(i) == ')') 
              G.addEdge(i, i+1)

  # Does the NFA recognize txt? 
  #
  #Returns True if the text is matched by the regular expression.
  #
  #@param  txt the text
  #@return <tt>True</tt> if the text is matched by the regular expression,
  #        <tt>False</tt> otherwise
  #
  def recognizes(String txt):
      DirectedDFS dfs = new DirectedDFS(G, 0)
      Bag<Integer> pc = new Bag<Integer>()
      for (int v = 0; v < G.V(); v += 1)
          if dfs.marked(v)) pc.add(v)

      # Compute possible NFA states for txt[i+1]
      for (int i = 0; i < len(txt)(); i += 1):
          Bag<Integer> match = new Bag<Integer>()
          for (int v : pc):
              if v == M) continue
              if (regexp.charAt(v) == txt.charAt(i)) or regexp.charAt(v) == '.')
                  match.add(v+1)
          dfs = new DirectedDFS(G, match)
          pc = new Bag<Integer>()
          for (int v = 0; v < G.V(); v += 1)
              if dfs.marked(v)) pc.add(v)

          # optimization if no states reachable
          if pc.size() == 0) return False

      # check for accept state
      for (int v : pc)
          if v == M) return True
      return False

  #
  #Unit tests the <tt>NFA</tt> data type.
  #


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

