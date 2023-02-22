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

    # -----------------------------------------------------------------
    # Testing the speed of an NFA for regular expression pattern matching
    #
    # pylint: disable=line-too-long
    #
    # H:Min:Seconds  Description
    # -:--:--------- -------------------------------------------------------------------------------
    # 0:00:00.000399 Python NFA: FOUND(False) REGEX((a|aa)*b) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    # 0:00:00.000360 Python NFA: FOUND(False) REGEX((a|aa)*b) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    # 0:00:00.000410 Python NFA: FOUND(False) REGEX((a|aa)*b) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    # 0:00:00.000392 Python NFA: FOUND(False) REGEX((a|aa)*b) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    # 0:00:00.000407 Python NFA: FOUND(False) REGEX((a|aa)*b) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    # 0:00:00.000446 Python NFA: FOUND(False) REGEX((a|aa)*b) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    regexp = "(a|aa)*b"
    _prt_hdr()
    for txt in txts:
        _run_nfa(regexp, txt)

    # -----------------------------------------------------------------
    # Testing the speed of Python re for regular expression pattern matching
    #
    # Pythonn's regex (so is grep's regex) is exponential, not len_txt*len_regex:
    # (Exponential time if add just one thing to txt and running time doubles)
    #
    # H:Min:Seconds  Description
    # -:--:--------- -------------------------------------------------------------------------------
    #   0:00:02.013926 FOUND(False REGEX(re.compile('(a|aa)*b')) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    #   0:00:05.301577 FOUND(False REGEX(re.compile('(a|aa)*b')) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    #   0:00:13.865646 FOUND(False REGEX(re.compile('(a|aa)*b')) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    #   0:00:37.574015 FOUND(False REGEX(re.compile('(a|aa)*b')) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    #   0:01:35.558015 FOUND(False REGEX(re.compile('(a|aa)*b')) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    #   0:04:13.938403 FOUND(False REGEX(re.compile('(a|aa)*b')) TXT(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    regex = re.compile(r"(a|aa)*b")
    for txt in txts:
        _run_re(regex, txt)

def _run_nfa(regexp, txt):
    tic = default_timer()
    nfa = NFA(regexp)
    matched = nfa.recognizes(txt)

    prt_hms(tic, f'{str(matched):5} Python NFA("{regexp}")            {txt}')
    return matched

def _run_re(regexp, txt):
    """Speed test Python's regex package (re)"""
    tic = default_timer()
    result = regexp.search(txt)
    matched = result is not None
    prt_hms(tic, f'{str(matched):5} Python re({regexp}) {txt}')
    return matched

def _prt_hdr():
    print('H MM SECONDS  Result Searching method                  Text on which to test for regex pattern')
    print('- -- -------- ------ --------------------------------  ----------------------------------------')


#****************************************************************************
if __name__ == "__main__":
    test_regex_is_exponential()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2019, DV Klopfenstein, PhD, Python implementation.
