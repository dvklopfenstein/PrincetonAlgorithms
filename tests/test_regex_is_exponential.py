#!/usr/bin/env python3
"""Test various regex approaches (Python re, grep) for having exponential running time"""
# End of the Regular Expressions Lecture

from timeit import default_timer
import re
#from tempfile import NamedTemporaryFile
from tests.utils import prt_hms

def test_regex_is_exponential():
    """Test various regex approaches (Python re, grep) for having exponential running time"""
    patterns = [
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",
    ]

    # Pythonn's regex (so is grep's regex) is exponential, not len_txt*len_regex:
    # (Exponential time if add just one thing to pattern and running time doubles)
    # pylint: disable=line-too-long
    #   0:00:02.013926 FOUND(False REGEX(re.compile('(a|aa)*b')) PATTERN(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    #   0:00:05.301577 FOUND(False REGEX(re.compile('(a|aa)*b')) PATTERN(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    #   0:00:13.865646 FOUND(False REGEX(re.compile('(a|aa)*b')) PATTERN(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    #   0:00:37.574015 FOUND(False REGEX(re.compile('(a|aa)*b')) PATTERN(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    #   0:01:35.558015 FOUND(False REGEX(re.compile('(a|aa)*b')) PATTERN(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    #   0:04:13.938403 FOUND(False REGEX(re.compile('(a|aa)*b')) PATTERN(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac)
    regex = re.compile(r"(a|aa)*b")
    for pat in patterns:
        _run_re(regex, pat)


def _run_re(regex, pattern):
    tic = default_timer()
    result = regex.search(pattern)
    matched = result is not None
    prt_hms(tic, f'FOUND({matched}) REGEX({regex}) PATTERN({pattern})')
    return matched


#****************************************************************************
if __name__ == "__main__":
    test_regex_is_exponential()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2019, DV Klopfenstein, Python implementation.
