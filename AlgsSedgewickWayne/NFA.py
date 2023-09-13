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

class NFA:
    """Initializes the NFA from the specified regular expression"""

    def __init__(self, regexp):
        self.regexp = regexp
        self.len_regexp = len(regexp)    # M
        # Epsilon transition digraph (does not include
        self.digraph = self._init_digraph(regexp)
        # print(self.digraph)

    def _init_digraph(self, regexp):
        """Build epsilon transition digraph"""
        # Use stack to remember '(' to implement '*' and '|'
        ops = []
        len_regexp = self.len_regexp
        digraph = Digraph(len_regexp+1)
        exp_operations = {'(', '|'}
        exp_edgechr = {'(', '*', ')'}
        for reg_i, reg_chr in enumerate(regexp):
            # self._prt_color_regex(reg_i, reg_chr)
            left_paren = reg_i
            if reg_chr in exp_operations:
                ops.append(reg_i)
            elif reg_chr == ')':
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
            reg_i_plus1 = reg_i + 1
            if reg_i < len_regexp-1 and regexp[reg_i_plus1] == '*':
                # print(f'************ {left_paren} {reg_i_plus1}')
                # print(f'************ {reg_i_plus1} {left_paren}')
                digraph.addEdge(left_paren, reg_i_plus1)
                digraph.addEdge(reg_i_plus1, left_paren)
            if reg_chr in exp_edgechr:
                digraph.addEdge(reg_i, reg_i_plus1)
        return digraph

    def _prt_color_regex(self, reg_i, reg_chr):
        regex = list(self.regexp)
        regex[reg_i] = '\x1b[48;5;0;{FGBG};5;{COLOR};1;3;4m{ABC}\x1b[0m'.format(
            FGBG=38, COLOR=13, ABC=regex[reg_i])
        print(f'REGEX {reg_i:2}) {reg_chr} {"".join(regex)}')

    def recognizes(self, txt):
        """Does the NFA recognize txt?"""
        # Get states reachable from start by epsilon-transitions
        reachable_states = set()
        # program counter holds set of all program possible states for given regex
        # Build a DFS for all states that can be reached from state 0 by epsilon edges
        dfs_state0 = DirectedDFS(self.digraph, 0)
        for vertex in range(self.digraph.V()):
            if dfs_state0.marked(vertex):
                reachable_states.add(vertex)
        print(f'{self.len_regexp} REACHABLE STATES: {reachable_states}')

        # Compute possible NFA states for txt[i+1]
        regexp = self.regexp
        len_regexp = self.len_regexp
        for txt_chr in txt:
            matched = set()
            for vertex in reachable_states:
                # If accept-state is reached, nothing left to do
                if vertex == len_regexp:
                    continue
                # Get all states matchable after matching a text character
                if (regexp[vertex] == txt_chr or regexp[vertex] == '.'):
                    matched.add(vertex+1)

            # Follow epsilon-transitions after a character match
            dfs = DirectedDFS(self.digraph, matched)
            reachable_states = set()
            for vertex in range(self.digraph.V()):
                if dfs.marked(vertex):
                    reachable_states.add(vertex)

            # optimization if no states reachable
            if not reachable_states:
                return False

        # Accept if can end in state len_regexp
        return len_regexp in reachable_states
        ## for vertex in reachable_states:
        ##     if vertex == len_regexp:
        ##         return True
        ## return False

    def _get_reachable_states(self, matched):
        """From source states, find all reachable states"""
        reachable_states = set()
        dfs = DirectedDFS(self.digraph, matched)
        for vertex in range(self.digraph.V()):
            if dfs.marked(vertex):
                reachable_states.add(vertex)
        return reachable_states

    def wr_png(self, fout_png):
        """Create plot of state machine and save into a png file"""
        import pydot
        # 1. Create/initialize Graph
        digraph = pydot.Dot(graph_type='digraph',
                            label=f'{self.regexp} [{len(self.regexp)}]',
                            rankdir='LR')
        # 2. Create Nodes
        regchrs = list(self.regexp) + ['MATCH',]
        assert len(regchrs) == len(self.digraph.keys)
        nodes = [pydot.Node(src_v, label=f'{src_v}\n{a}') for a, src_v in zip(regchrs, self.digraph.keys)]
        #nodes = [pydot.Node(src_v, label=f'{src_v} ??') for src_v in self.digraph.keys]
        # 3. Add nodes to Graph
        prev_i = -1
        prev_chr = -1
        rngs = [('a', 'z'), ('A', 'Z'), ('0', '9')]
        az09 = set(chr(i) for a, z in rngs for i in range(ord(a), ord(z) + 1))
        ## print('ALPHANUMERIC CHRS:', sorted(az09)) 
        for reg_i, reg_chr in enumerate(self.regexp):
            node = pydot.Node(reg_i, label=f'{reg_i}\n{reg_chr}')
            digraph.add_node(node)
            if prev_chr in az09:
                digraph.add_edge(pydot.Edge(prev_i, reg_i, color='black'))
            prev_i = reg_i
            prev_chr = reg_chr
        #for node in nodes:
        #    digraph.add_node(node)
        # 4. Add Edges between Nodes to Graph
        for src_v, dst_w in self.digraph.get_edges():
            if src_v != dst_w: # Print only edges from one node to another (not to self)
                #print(f'{src_v} {dst_w}')
                digraph.add_edge(pydot.Edge(src_v, dst_w, color='red'))
        # Add invisible edge to line up states in order in plot
        for src_v, src_vp1 in zip(self.digraph.keys[:-1], self.digraph.keys[1:-2]):
            digraph.add_edge(pydot.Edge(src_v, src_vp1, color='blue', style='invis'))#'dotted'))
        digraph.write_png(fout_png)
        print(f"  WROTE: {fout_png}")


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-present, DV Klopfenstein, PhD, Python implementation.
