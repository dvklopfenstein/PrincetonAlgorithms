#!/usr/bin/env python3
"""Test Knuth-Morris-Pratt substring search algorithm"""
# pylint: disable=invalid-name

from sys import stdout
from sys import argv
from AlgsSedgewickWayne.KMP import KMP

def test_0(pat, txt, prt=stdout):
    """Test Knuth-Morris-Pratt substring search algorithm.

    Searches for the pattern in the text; prints the 1st occurrence.
    Execution:    test_KMP.py pattern text

    Reads in two strings, the pattern and the input text, and
    searches for the pattern in the input text using the
    KMP algorithm.

    >>> test_0("abracadabra", "abacadabrabracabracadabrabrabracad")
    text:    abacadabrabracabracadabrabrabracad
    pattern:               abracadabra

    >>> test_0("rab", "abacadabrabracabracadabrabrabracad")
    text:    abacadabrabracabracadabrabrabracad
    pattern:         rab

    >>> test_0("bcara", "abacadabrabracabracadabrabrabracad")
    text:    abacadabrabracabracadabrabrabracad
    pattern:                                   bcara

    >>> test_0("rabrabracad", "abacadabrabracabracadabrabrabracad ")
    text:    abacadabrabracabracadabrabrabracad
    pattern:                        rabrabracad

    >>> test_0("abacad", "abacadabrabracabracadabrabrabracad")
    text:    abacadabrabracabracadabrabrabracad
    pattern: abacad
    """

    kmp = KMP(pat)
    kmp.prt_dfa(prt)
    offset = kmp.search(txt)

    # print results
    ret = [f"text:    {txt}\n"]
    ret.append(f"pattern: {' '*offset}{pat}\n")
    prt.write(f"{''.join(ret)}\n")
    return ''.join(ret)


def cli():
    """Run substring test using pattern and text from arguments"""
    num_args = len(argv)
    if num_args == 3:
        test_0(pat=argv[1], txt=argv[2], prt=stdout)
    else:
        test_0(pat="ababac", txt="aabdacaababacdaa", prt=stdout)

#****************************************************************************
if __name__ == "__main__":
    cli()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2019, DV Klopfenstein, Python implementation.
