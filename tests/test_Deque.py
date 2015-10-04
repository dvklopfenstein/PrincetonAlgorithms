#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Deque import Deque

def test_2a(prt=sys.stdout):
  deque = Deque()
  deque.isEmpty()
  deque.isEmpty()
  deque.addFirst(2)
  deque.isEmpty()
  deque.removeFirst()

def test_2b(prt=sys.stdout):
  deque = Deque()
  deque.addFirst(0)
  deque.removeFirst()

def test_10(prt=sys.stdout):
  """Check iterator after intermixed calls to addFirst(), addLast()."""
  deque = Deque()
  deque.addFirst(1)
  prt.write("{}\n".format(deque.removeFirst())) # ==> 1
  deque.addLast(3)
  deque.addFirst(4)
  deque.addFirst(5)
  deque.addFirst(6)
  deque.addLast(7)
  deque.addFirst(8)
  prt.write("{}\n".format(deque.removeLast())) #  ==> 7



#def main(prt=sys.stdout):
#  """unit testing."""
#  s = Deque()
#  while (!StdIn.isEmpty()):
#    String item = StdIn.readString()
#    if item.equals(".")) break
#    elif (!item.equals("-")) s.addFirst(item)
#    elif (!s.isEmpty()) StdOut.print(s.removeFirst() + " ")
#  prt.write("({SZ} left on stack)\n".format(SZ=s.size()))

def run_all(prt=sys.stdout):
  test_2a(prt)
  test_2b(prt)
  test_10(prt)

if __name__ == '__main__':
#  N = len(sys.argb)
#  if N == 1:
#    main()
#  else:
#    run_all()
  test_2b()
  
