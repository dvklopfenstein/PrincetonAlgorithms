#!/usr/bin/env python3
"""Test brute-force search for a substring"""

from timeit import default_timer
from AlgsSedgewickWayne.substrsrc_bruteforce import search as search_bf
from AlgsSedgewickWayne.substrsrc_bruteforce_alt import search as search_bf_alt
from AlgsSedgewickWayne.KMP import KMP
from AlgsSedgewickWayne.KMP import search as search_kmp
from tests.utils import prt_hms

def test_substrsrc_bruteforce():
    """Test brute-force search for a substring"""
    num_runs = 1000000

    # 2 min, 36 sec into lecture
    # pylint: disable=bad-whitespace
    #      00000000001
    #      01234567890
    txt = 'ABACADABRAC'
    pat =       'ABRA'
    _chk_all(txt, 'BBBBBB', -1)
    _chk_all(txt, pat, 6)
    _timeit_all(txt, pat, num_runs)

    # 4 min, 09 sec into lecture
    # Fine in many contexts and actually is the one Java's indexOf uses
    # but the problem is it can be slow if there is a lot of repeatitive
    # characters in the text and the pattern
    #
    #      0123456789
    txt = 'AAAAAAAAAB'
    pat =      'AAAAB'
    _chk_all(txt, pat, 5)
    _timeit_all(txt, pat, num_runs)

    # Knuth-Morris-Pratt substring search
    #      0000000000111111
    #      0123456789012345
    txt = 'ABAAAABAAAAAAAAA'
    pat =       'BAAAAAAAAA'
    _chk_all(txt, pat, 6)
    _timeit_all(txt, pat, num_runs)


# -----------------------------------------------------------------------
def _timeit_all(txt, pat, num_runs):
    """Time all string searches for pattern in text"""
    ##return
    _timeit(txt, pat, num_runs, search_bf)
    _timeit(txt, pat, num_runs, search_bf_alt)
    _timekmp(txt, pat, num_runs)

def _timekmp(txt, pat, num_runs):
    """Time the Knuth-Morris-Pratt substring search"""
    tic = default_timer()
    kmp = KMP(pat)
    for _ in range(num_runs):
        kmp.search(txt)
    prt_hms(tic, 'AlgsSedgewickWayne.KMP (init DFA once)')
    _timeit(txt, pat, num_runs, search_kmp)
    print('')

def _timeit(txt, pat, num_runs, fncname):
    """Time the brute-force algorithm"""
    ##return
    tic = default_timer()
    for _ in range(num_runs):
        fncname(pat, txt)
    prt_hms(tic, fncname.__module__)

def _chk_all(txt, pat, exp):
    """Check for expected matching index into text for all functions"""
    _chk(txt, pat, exp, search_bf)
    _chk(txt, pat, exp, search_bf_alt)
    _chk(txt, pat, exp, search_kmp)

def _chk(txt, pat, exp, fncname):
    """Check for expected matching index into text"""
    name = fncname.__module__
    print(f'TXT:{txt:20} PAT:{pat:10} {name}')
    act = fncname(pat, txt)
    assert act == exp, f'ACT({act}) != EXP({exp}) TEXT({txt}) PAT({pat}) {name}'


if __name__ == '__main__':
    test_substrsrc_bruteforce()
