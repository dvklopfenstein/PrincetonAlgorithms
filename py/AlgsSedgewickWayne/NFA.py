"""Initializes the NFA from the specified regular expression"""
# pylint: disable=invalid-name

from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.Stack import Stack
from AlgsSedgewickWayne.DirectedDFS import DirectedDFS

#
# The >NFA> class provides a data type for creating a
# nondeterministic finite state automaton (NFA) from a regular
# expression and testing whether a given string is matched by that regular
# expression.
# It supports the following operations: concatenation,
# closure>, binary or, and parentheses.
# It does not support <em>mutiway or</em>, <em>character classes</em>,
# metacharacters (either in the text or pattern),
# capturing capabilities, greedy or relucantant
# modifiers, and other features in industrial-strength implementations
# such as {@link java.util.regex.Pattern} and:@link java.util.regex.Matcher}.
#
# This implementation builds the NFA using a digraph and a stack
# and simulates the NFA using digraph search (see the textbook for details).
# The constructor takes time proportional to len_regexp, where len_regexp
# is the number of characters in the regular expression.
# The recognizes method takes time proportional to len_regexp N,
# where N is the number of characters in the text.
#
# For additional documentation,
# see https://algs4.cs.princeton.edu/54regexp Section 5.4 of
# Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
#
# @author Robert Sedgewick
# @author Kevin Wayne

class NFA:
    """Initializes the NFA from the specified regular expression"""

    def __init__(self, regexp):
        self.regexp = regexp
        self.len_regexp = len(regexp)    # M
        self.digraph = self._init_digraph()

    def _init_digraph(self):
        """Build epsilon transition digraph"""
        # Use stack to remember '(' to implement '*' and '|'
        ops = Stack()
        len_regexp = self.len_regexp
        digraph = Digraph(len_regexp+1)
        regexp = self.regexp
        for reg_i in range(len_regexp):
            left_paren = reg_i
            if regexp[reg_i] == '(' or regexp[reg_i] == '|':
                ops.push(reg_i)
            elif regexp[reg_i] == ')':
                tmpor = ops.pop()
                # 2-way or operator
                if regexp[tmpor] == '|':
                    left_paren = ops.pop()
                    digraph.addEdge(left_paren, tmpor+1)
                    digraph.addEdge(tmpor, reg_i)
                elif regexp[tmpor] == '(':
                    left_paren = tmpor
                else:
                    assert False

            # closure operator (uses 1-character lookahead)
            if reg_i < len_regexp-1 and regexp[reg_i+1] == '*':
                digraph.addEdge(left_paren, reg_i+1)
                digraph.addEdge(reg_i+1, left_paren)
            if regexp[reg_i] == '(' or regexp[reg_i] == '*' or regexp[reg_i] == ')':
                digraph.addEdge(reg_i, reg_i+1)
        return digraph

    def recognizes(self, txt):
        """Does the NFA recognize txt?"""
        # Get states reachable fron start by epsilon-transitions
        # Build a DFS for all states that can be reached from state 0
        dfs = DirectedDFS(self.digraph, 0)
        # program counter holds set of all program possible states for given regex
        program_ctr = set()
        #### for (int vertex = 0; vertex < digraph.V(); vertex += 1)
        for vertex in range(self.digraph.V()):
            if dfs.marked(vertex):
                program_ctr.add(vertex)

        # Compute possible NFA states for txt[i+1]
        regexp = self.regexp
        len_regexp = self.len_regexp
        for txt_chr in txt:
            matched = set()
            for vertex in program_ctr:
                # If accept-state is reached, nothing left to do
                if vertex == len_regexp:
                    continue
                # Get all states matchable after matching a text character
                if (regexp[vertex] == txt_chr or regexp[vertex] == '.'):
                    matched.add(vertex+1)

            # Follow epsilon-transitions after a character match
            dfs = DirectedDFS(self.digraph, matched)
            program_ctr = set()
            for vertex in range(self.digraph.V()):
                if dfs.marked(vertex):
                    program_ctr.add(vertex)

            # optimization if no states reachable
            if not program_ctr:
                return False

        # Accept if can end in state len_regexp
        for vertex in program_ctr:
            if vertex == len_regexp:
                return True
        return False


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-present, DV Klopfenstein, PhD, Python implementation.
