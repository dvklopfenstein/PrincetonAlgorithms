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

if __name__ == '__main__':
    test_symbol_table()
