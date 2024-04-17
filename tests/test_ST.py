#!/usr/bin/env python3
"""Test basic symbol table"""

from AlgsSedgewickWayne.ST import ST

def test_symbol_table():
    """Unit tests the ST data type."""
    st = ST()
    st.put("A", 1)
    st.put("B", 1)
    st.put("B", 2)
    st.put("B", 3)
    st.put("B", 4)

def test_symbol_table_01_08_01a():
    """Test sequence at 17:52 of 'Symbol Table APIs'"""
    seq_in = "SEARCHEXAMPLE"
    exp_out = [
        ("A", 8),
        ("C", 4),
        ("E", 12),
        ("H", 5),
        ("L", 11),
        ("M", 9),
        ("P", 10),
        ("R", 3),
        ("S", 0),
        ("X", 7),
    ]
    _run(seq_in, exp_out)
    

def _run(seq_in, exp_out):
    """Run test: Fill Symbol Table; Compare with expected results"""
    symtbl = ST()
    for idx, letter in enumerate(seq_in):
        symtbl.put(letter, idx)
     
    for act_letter, (exp_letter, exp_val) in zip(symtbl.get_keys(), exp_out):
        act_val = symtbl.get(act_letter)
        print(f'("{act_letter}", {act_val}),')
        assert act_letter == exp_letter
        assert act_val == exp_val

if __name__ == '__main__':
    #test_symbol_table()
    test_symbol_table_01_08_01a()
