"""Knuth-Morris-Pratt finds the 1st occurrence of a pattern in a text string wo/backing-up."""

import collections as cx

class KMP(object): # O ~ txtlen + patlen * alphabet-size (wc)
  """finds the first occurrence of a pattern string in a text string."""

  def __init__(self, pat):
    """Preprocesses the pat string."""
    self._pat = list(pat)
    self._M = len(self._pat)
    self._miss = [0 for i in range(self._M)]

    # build DFA (Deterministic finite state automatom) from pat
    self._dfa = cx.defaultdict(lambda: [0 for i in range(self._M)])
    self._dfa[self._pat[0]][0] = 1
    X = 0
    for j, letter in enumerate(self._pat[1:], 1):
      for c in self._dfa.keys():
        self._dfa[c][j] = self._dfa[c][X] # Copy mismatch cases. 
      self._dfa[letter][j] = j+1      # Set match case. 
      X = self._dfa[letter][X]        # Update restart state. 

  def search(self, txt):
    """Returns the idx of the 1st occurrrence of the pattern string in the text string."""
    # simulate operation of DFA on text
    M = self._M
    N = len(txt)
    i = 0
    j = 0
    while i < N and j < M:
      j = self._dfa.get(txt[i], self._miss)[j]
      i += 1
    if j == M: return i - M # found
    return N                # not found, return text size

  def prt_dfa(self, prt):
    """Print DFA (Deterministic finite state automatom) from pat."""
    prt.write("     {}\n".format(' '.join(self._pat)))
    prt.write("     {} <- Current State\n".format(' '.join(str(i) for i in range(self._M))))
    for pat_letter, state_nxt in sorted(self._dfa.items()): 
      prt.write("{} -> {}\n".format(pat_letter, ' '.join(str(s) for s in state_nxt)))

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.

