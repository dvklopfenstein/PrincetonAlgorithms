#!/usr/bin/env python#*****************************************************************************
 #  Compilation:  javac BTree.java
 #  Execution:    java BTree
 #  Dependencies: StdOut.java
 #
 #  B-tree.
 #
 #  Limitations
 #  -----------
 #   -  Assumes M is even and M >= 4
 #   -  should b be an array of children or list (it would help with
 #      casting to make it a list)
 #
 #*****************************************************************************/

package edu.princeton.cs.algs4


public class BTree< extends Comparable<>, Value>:
    private static final M = 4;    # max children per B-tree node = M-1

    private  root;             # root of the B-tree
    private HT;                # height of the B-tree
    private N;                 # number of key-value pairs in the B-tree

    # helper B-tree node data type
    private static final class:
        private m;                             # number of children
        private Entry[] children = new Entry[M];   # the array of children

        # create a node with k children
        private (int k):
            m = k

    # internal nodes: only use key and next
    # external nodes: only use key and value
    private static class Entry:
        private key
        private  value
        private  next;     # helper field to iterate over array entries
        public Entry(key,  value,  next):
            this.key   = key
            this.value = value
            this.next  = next

    # constructor
    public BTree():
        root = new (0)
 
    # return number of key-value pairs in the B-tree
    def size(): return N; }

    # return height of B-tree
    def height(): return HT; }


    # search for given key, return associated value; return None if no such key
    def search(root, key, HT); }
    def _search( x,  key, ht):
        Entry[] children = x.children

        # external node
        if ht == 0):
            for (int j = 0; j < x.m; j += 1):
                if eq(key, children[j].key)) return (Value) children[j].value

        # internal node
        else:
            for (int j = 0; j < x.m; j += 1):
                if j+1 == x.m or less(key, children[j+1].key))
                    return search(children[j].next, key, ht-1)
        return None


    # insert key-value pair
    # add code to check for duplicate keys
    def put( key, Value value):
         u = insert(root, key, value, HT)
        N += 1
        if u == None) return

        # need to split root
         t = new (2)
        t.children[0] = new Entry(root.children[0].key, None, root)
        t.children[1] = new Entry(u.children[0].key, None, u)
        root = t
        HT += 1


    private  insert( h,  key, Value value, ht):
        j
        Entry t = new Entry(key, value, None)

        # external node
        if ht == 0):
            for (j = 0; j < h.m; j += 1):
                if less(key, h.children[j].key)) break

        # internal node
        else:
            for (j = 0; j < h.m; j += 1):
                if (j+1 == h.m) or less(key, h.children[j+1].key)):
                     u = insert(h.children[j += 1].next, key, value, ht-1)
                    if u == None) return None
                    t.key = u.children[0].key
                    t.next = u
                    break

        for (int i = h.m; i > j; i -= 1)
            h.children[i] = h.children[i-1]
        h.children[j] = t
        h.m += 1
        if h.m < M) return None
        else:         return split(h)

    # split node in half
    private  split( h):
         t = new (M/2)
        h.m = M/2
        for (int j = 0; j < M/2; j += 1)
            t.children[j] = h.children[M/2+j]
        return t

    # for debugging
    def toString():
        return toString(root, HT, "") + "\n"
    def _toString( h, ht, String indent):
        StringBuilder s = new StringBuilder()
        Entry[] children = h.children

        if ht == 0):
            for (int j = 0; j < h.m; j += 1):
                s.append(indent + children[j].key + " " + children[j].value + "\n")
        else:
            for (int j = 0; j < h.m; j += 1):
                if j > 0) s.append(indent + "(" + children[j].key + ")\n")
                s.append(toString(children[j].next, ht-1, indent + "     "))
        return s.toString()


    # comparison functions - make instead of  to avoid casts
    def _less(k1, k2):
        return k1.compareTo(k2) < 0

    def _eq(k1, k2):
        return k1.compareTo(k2) == 0


   #**************************************************************************
    #  Test client.
    #**************************************************************************/
    def main(String[] args):
        BTree<String, String> st = new BTree<String, String>()

#      st.put("www.cs.princeton.edu", "128.112.136.12")
        st.put("www.cs.princeton.edu", "128.112.136.11")
        st.put("www.princeton.edu",    "128.112.128.15")
        st.put("www.yale.edu",         "130.132.143.21")
        st.put("www.simpsons.com",     "209.052.165.60")
        st.put("www.apple.com",        "17.112.152.32")
        st.put("www.amazon.com",       "207.171.182.16")
        st.put("www.ebay.com",         "66.135.192.87")
        st.put("www.cnn.com",          "64.236.16.20")
        st.put("www.google.com",       "216.239.41.99")
        st.put("www.nytimes.com",      "199.239.136.200")
        st.put("www.microsoft.com",    "207.126.99.140")
        st.put("www.dell.com",         "143.166.224.230")
        st.put("www.slashdot.org",     "66.35.250.151")
        st.put("www.espn.com",         "199.181.135.201")
        st.put("www.weather.com",      "63.111.66.11")
        st.put("www.yahoo.com",        "216.109.118.65")


        prt.write("cs.princeton.edu:  " + st.get("www.cs.princeton.edu"))
        prt.write("hardvardsucks.com: " + st.get("www.harvardsucks.com"))
        prt.write("simpsons.com:      " + st.get("www.simpsons.com"))
        prt.write("apple.com:         " + st.get("www.apple.com"))
        prt.write("ebay.com:          " + st.get("www.ebay.com"))
        prt.write("dell.com:          " + st.get("www.dell.com"))
        prt.write()

        prt.write("size:    " + st.size())
        prt.write("height:  " + st.height())
        prt.write(st)
        prt.write()


#*****************************************************************************
 #  Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
 #
 #  This file is part of algs4.jar, which accompanies the textbook
 #
 #      Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne,
 #      Addison-Wesley Professional, 2011, ISBN 0-321-57351-X.
 #      http://algs4.cs.princeton.edu
 #
 #
 #  algs4.jar is free software: you can redistribute it and/or modify
 #  it under the terms of the GNU General Public License as published by
 #  the Free Software Foundation, either version 3 of the License, or
 #  (at your option) any later version.
 #
 #  algs4.jar is distributed in the hope that it will be useful,
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with algs4.jar.  If not, see http://www.gnu.org/licenses.
 #*****************************************************************************/
