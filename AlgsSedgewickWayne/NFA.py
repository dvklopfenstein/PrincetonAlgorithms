"""Initializes the NFA from the specified regular expression"""
# pylint: disable=invalid-name

from AlgsSedgewickWayne.Digraph import Digraph
from AlgsSedgewickWayne.DirectedDFS import DirectedDFS

# The NFA class provides a data type for creating a
# nondeterministic finite state automaton (NFA) from a regular
# expression and testing whether a given string is matched by that regular
# expression.
# It supports the following operations:
#   * concatenation
#   * closure
#   * binary or
#   * parentheses
# It does not support:
#   * mutiway or
#   * character classes
#   * metacharacters, ie "+" (either in the text or pattern)
#   * capturing capabilities
#   * greedy or relucantant modifiers
# and other features in industrial-strength implementations
# such as {@link java.util.regex.Pattern} and:@link java.util.regex.Matcher}.
#
# This implementation builds the NFA using a digraph and a stack
# and simulates the NFA using digraph search (see the textbook for details).
# The constructor takes time proportional to len_regexp, where len_regexp
# is the number of characters in the regular expression.
# The recognizes method takes time proportional to len_regexp N,
# where N is the number of characters in the text.
#
# For additional documentation, see
# https://algs4.cs.princeton.edu/54regexp
# Section 5.4 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
#
# @author Robert Sedgewick
# @author Kevin Wayne


# pylint: disable=too-few-public-methods
class NFA:
    """Initializes the NFA from the specified regular expression"""

    def __init__(self, regexp):
        self.regexp = regexp           # regular expression
        self.len_regexp = len(regexp)  # M: number of characters in regular expression
        # Epsilon transition digraph (does not include
        self.digraph = self._init_digraph(regexp)  # digraph of epsilon transitions
        # print(self.digraph)

    def _init_digraph(self, regexp):
        """Initializes the NFA from the specified regular expression"""
        ops = []  # Operations Stack
        graph = Digraph(self.len_regexp+1)
        len_regexp = self.len_regexp
        ## for (int i = 0 i < m; i++):
        for reg_i, reg_chr in enumerate(regexp):
            left_paren = reg_i
            if reg_chr in {'(', '|'}:
                ops.append(reg_i)
            elif reg_chr == ')':
                tmp_or = ops.pop()

                # 2-way tmp_or operator
                if regexp[tmp_or] == '|':
                    left_paren = ops.pop()
                    # Add two edges to skip OR(|)
                    graph.addEdge(left_paren, tmp_or+1)
                    graph.addEdge(tmp_or, reg_i)
                elif regexp[tmp_or] == '(':
                    left_paren = tmp_or
                else:
                    assert False

            # closure operator (uses 1-character lookahead)
            if reg_i < len_regexp - 1 and regexp[reg_i + 1] == '*':
                graph.addEdge(left_paren, reg_i+1)
                graph.addEdge(reg_i+1, left_paren)
            if reg_chr in {'(', '*', ')'}:
                graph.addEdge(reg_i, reg_i+1)
        if ops:
            raise RuntimeError("Invalid regular expression")
        return graph

    def recognizes(self, txt):
        """Returns true if the text is matched by the regular expression"""
        dfs = DirectedDFS(self.digraph, 0)
        len_regexp = self.len_regexp
        num_vertices = self.digraph.num_vertices
        regexp = self.regexp
        graph = self.digraph
        reachable_states = set(vertix for vertix in range(num_vertices) if dfs.marked(vertix))

        # Compute possible NFA states for txt[i+1]
        #for (int i = 0 i < txt.length(); i++) {
        for txt_chr in txt:
            if txt_chr in {'*', '|', '(', ')'}:
                raise RuntimeError(f"text contains the metacharacter '{txt_chr}'")

            match = set()
            for vertix in reachable_states:
                if vertix == len_regexp:
                    continue
                if regexp[vertix] in {txt_chr, '.'}:
                    match.add(vertix+1)
            if not match:
                continue

            dfs = DirectedDFS(graph, match)
            reachable_states = set(vertix for vertix in range(num_vertices) if dfs.marked(vertix))

            # optimization if no states reachable
            if not reachable_states:
                return False

        # check for accept state
        return len_regexp in reachable_states


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-present, DV Klopfenstein, PhD, Python implementation.graph
