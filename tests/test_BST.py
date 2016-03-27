#!/usr/bin/env python
"""Test Binary Search Tree (BST)."""

import sys
from AlgsSedgewickWayne.BST import BST
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

#****************************************************************************
# Compilation:  javac BST.java
# Execution:    java BST
# Dependencies: StdIn.java StdOut.java Queue.java
# Data files:   http:#algs4.cs.princeton.edu/32bst/tinyST.txt  
#
# A symbol table implemented with a binary search tree.
#
# % more tinyST.txt
# S E A R C H E X A M P L E
# 
# % java BST < tinyST.txt
# A 8
# C 4
# E 12
# H 5
# L 11
# M 9
# P 10
# R 3
# S 0
# X 7
#
def test_0(prt=sys.stdout):
    item_list = cli_get_array("tinyST.txt")
    print item_list
    st = BST()
    for i, key in enumerate(item_list):
        st.put(key, i)
        png = "BST_{I}_{K}.png".format(I=i, K=key)
        st.wr_png(png)

    prt.write("LEVEL ORDER:\n")
    for s in st.levelOrder():
        prt.write("{S} {ST}\n".format(S=s, ST=st.get(s)))

    prt.write("\n")

    prt.write("KEYS:\n")
    for s in st.keys():
        prt.write("{S} {ST}\n".format(S=s, ST=st.get(s)))

    st.wr_png("tinyST.png")

#****************************************************************************
if __name__ == "__main__":
    test_0()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne. All rights reserved.
# Copyright 2015-2016, DV Klopfenstein, Python implementation. All rights reserved.

