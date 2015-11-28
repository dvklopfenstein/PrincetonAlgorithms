#!/usr/bin/env python
# TBD: Finish Python port

#*****************************************************************************
 #  Compilation:  javac TrieST.java
 #  Execution:    java TrieST < words.txt
 #  Dependencies: StdIn.java
 #
 #  A string symbol table for extended ASCII strings, implemented
 #  using a 256-way trie.
 #
 #  % java TrieST < shellsST.txt 
 #  by 4
 #  sea 6
 #  sells 1
 #  she 0
 #  shells 3
 #  shore 7
 #  the 5
 #
 #*****************************************************************************/

import sys
from AlgsSedgewickWayne.TrieST import TrieSt

def main(prt=sys.stdout):
  """Unit tests the TrieST data type."""

  # build symbol table from standard input
  st = TrieST()
  for (int i = 0; !StdIn.isEmpty(); i += 1):
    String key = StdIn.readString()
    st.put(key, i)

  # print results
  if st.size() < 100:
    prt.write('keys(""):')
    for key in st.keys():
      prt.write("{} {}".format(key, st.get(key)))
    prt.write("\n")

  prt.write('longestPrefixOf("shellsort"):')
  prt.write(st.longestPrefixOf("shellsort"))
  prt.write("\n")

  prt.write('longestPrefixOf("quicksort"):')
  prt.write(st.longestPrefixOf("quicksort"))
  prt.write("\n")

  prt.write('keysWithPrefix("shor"):')
  for s in st.keysWithPrefix("shor"):
    prt.write(s)
  prt.write("\n")

  prt.write('keysThatMatch(".he.l."):')
  for s in st.keysThatMatch(".he.l."):
    prt.write(s)

if __name__ == '__main__':
  main()
