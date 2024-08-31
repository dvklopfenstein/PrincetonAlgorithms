#!/usr/bin/env python3
"""Test QuickFind from Dynamic connectivity lecture."""

# Written by DV Klopfenstein

from AlgsSedgewickWayne.QuickFindUF import QuickFindUF
from AlgsSedgewickWayne.testcode.utils import hl_idnum
from AlgsSedgewickWayne.testcode.utils import hl_idroot

def test_union_find():
    """Test 1."""
    alg = QuickFindUF(10)
    _union(alg, 4, 3)

def _union(alg, pid, qid):
    _prt_before('PID', alg, pid, bgcolor=0, fgcolor=9)
    _prt_before('QID', alg, qid, bgcolor=0, fgcolor=11)
    alg.union(pid, qid)
    _prt_before('QID', alg, pid, bgcolor=0, fgcolor=10)

def _prt_before(idstr, alg, idnum, bgcolor=0, fgcolor=15):
    id_root = alg.idvals[idnum]
    print(f'{idstr}({idnum}) ROOT IS {id_root}')
    print('ROOT:  ', hl_idroot(idnum, alg.idvals, bgcolor, fgcolor))
    print(f'{idstr}:   ', hl_idnum( idnum, alg.idvals, fgcolor, bgcolor))


if __name__ == '__main__':
    test_union_find()
