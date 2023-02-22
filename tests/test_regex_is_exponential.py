#!/usr/bin/env python3
"""Test various regex approaches (Python re, grep) for having exponential running time"""
# End of the Regular Expressions Lecture

from timeit import default_timer
import re
#from tempfile import NamedTemporaryFile
from tests.utils import prt_hms
from AlgsSedgewickWayne.NFA import NFA

def test_regex_is_exponential():
    """Test various regex approaches (Python re, grep) for having exponential running time"""
    txts = [
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
    ]

    # H MM SECONDS  Result Searching method              Text on which to test for regex pattern
    # - -- -------- ------ ----------------------------- ----------------------------------------
    # 0:00:00.000399 False Python NFA("(a|aa)*b")        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    # 0:00:00.000374 False Python NFA("(a|aa)*b")        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    # 0:00:00.000388 False Python NFA("(a|aa)*b")        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    # 0:00:00.000489 False Python NFA("(a|aa)*b")        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    # 0:00:00.000469 False Python NFA("(a|aa)*b")        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    # 0:00:00.000423 False Python NFA("(a|aa)*b")        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    regexp = "(a|aa)*b"
    _prt_hdr()
    for txt in txts:
        _run_nfa(regexp, txt)

    # H MM SECONDS  Result Searching method              Text on which to test for regex pattern
    # - -- -------- ------ ----------------------------- ----------------------------------------
    # 0:00:02.130942 False Python re.compile('(a|aa)*b') aaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    # 0:00:05.454958 False Python re.compile('(a|aa)*b') aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    # 0:00:15.768528 False Python re.compile('(a|aa)*b') aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    # 0:00:38.932166 False Python re.compile('(a|aa)*b') aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    # 0:01:45.282705 False Python re.compile('(a|aa)*b') aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    # 0:05:02.419219 False Python re.compile('(a|aa)*b') aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
    regex = re.compile(r"(a|aa)*b")
    for txt in txts:
        _run_re(regex, txt)

def _run_nfa(regexp, txt):
    tic = default_timer()
    nfa = NFA(regexp)
    matched = nfa.recognizes(txt)

    prt_hms(tic, f'{str(matched):5} Python NFA("{regexp}")        {txt}')
    return matched

def _run_re(regexp, txt):
    """Speed test Python's regex package (re)"""
    tic = default_timer()
    result = regexp.search(txt)
    matched = result is not None
    prt_hms(tic, f'{str(matched):5} Python {regexp} {txt}')
    return matched

def _prt_hdr():
    print('H MM SECONDS  Result Searching method              Text on which to test for regex pattern')
    print('- -- -------- ------ ----------------------------  ----------------------------------------')


#****************************************************************************
if __name__ == "__main__":
    test_regex_is_exponential()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2019, DV Klopfenstein, PhD, Python implementation.
