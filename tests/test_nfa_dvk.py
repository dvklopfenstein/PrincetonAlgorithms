#!/usr/bin/env python3
"""Test non-deterministic finate state automata (machine)"""
# https://github.com/whitemech/pythomata
# http://infolab.stanford.edu/~ullman/ialc.html
# http://infolab.stanford.edu/~ullman/ialc/spr10/spr10.html#LECTURE%20NOTES

from AlgsSedgewickWayne.nfa_dvk import ReferenceItNFA


def test_reference_it_nfa():
    """Test non-deterministic finate state automata (machine)"""
    regex = "((MI*)*)"
    nfa = ReferenceItNFA(regex)

    print(nfa.recognizes("MMII"))
    print(nfa.recognizes("MII"))
    print(nfa.recognizes("MMI"))


#****************************************************************************
if __name__ == "__main__":
    test_reference_it_nfa()
