#!/usr/bin/env python

from AlgsSedgewickWayne.SequentialSearchST import SequentialSearchST
import sys
import fileinput

def main(prt=sys.stdout):
  """Read input from stdin. Stop reading by pressint ctrl-d twice.

     EXAMPLE 1:
       $ test_SequentialSearchST.py
       a
       b
       c
       <ctrl-d><ctrl-d>
       
       c 2
       b 1
       a 0

       
     EXAMPLE 2:
       $ test_SequentialSearchST.py
       a b c d e f<ctrl-d><ctrl-d>

       f 5
       e 4
       d 3
       c 2
       b 1
       a 0

     EXAMPLE 3:
       $ echo "a b c d" | test_SequentialSearchST.py
       
       d 3
       c 2
       b 1
       a 0
  """
  st = SequentialSearchST()
  items_in = [w.rstrip("\n\r") for t in fileinput.input() for w in t.split(" ")]
  prt.write("\n")
  for i, key in enumerate(items_in):
    key = key.rstrip("\n\r")
    st.put(key, i)

  for s in st.keys():
    prt.write("{} {}\n".format(s, st.get(s)))

if __name__ == '__main__':
  main()
