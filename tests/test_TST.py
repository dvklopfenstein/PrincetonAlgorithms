#!/usr/bin/env python


#*****************************************************************************
 #  Compilation:  javac TST.java
 #  Execution:    java TST < words.txt
 #  Dependencies: StdIn.java
 #
 #  Symbol table with string keys, implemented using a ternary search
 #  trie (TST).
 #
 #
 #  % java TST < shellsST.txt
 #  keys(""):
 #  by 4
 #  sea 6
 #  sells 1
 #  she 0
 #  shells 3
 #  shore 7
 #  the 5
 #
 #  longestPrefixOf("shellsort"):
 #  shells
 #
 #  keysWithPrefix("shor"):
 #  shore
 #
 #  keysThatMatch(".he.l."):
 #  shells
 #
 #  % java TST
 #  theory the now is the time for all good men
 #
 #  Remarks
 #  --------
 #    - can't use a key that is the empty string ""
 #
 #*****************************************************************************/

import sys
from AlgsSedgewickWayne.TST import TST
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

def main(fin, prt=sys.stdout):
  """Unit tests the TST data type."""

  # build symbol table from standard input
  arr = cli_get_array(fin)
  print arr
  st = TST()
  for i, key in enumerate(arr):
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

  prt.write('keysWithPrefix("shor"):')
  for s in st.keysWithPrefix("shor"):
    prt.write(s)
  prt.write("\n")

  prt.write('keysThatMatch(".he.l."):')
  for s in st.keysThatMatch(".he.l."):
    prt.write(s)


if __name__ == '__main__':
  main("../thirdparty/shellsST.txt")
