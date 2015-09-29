#!/usr/bin/env python
"""Read seq. Print N largest items."""

import sys
import fileinput
from AlgsSedgewickWayne.Transaction import Transaction
from AlgsSedgewickWayne.MinPQ import MinPQ
from AlgsSedgewickWayne.Stack import Stack

def main(prt=sys.stdout):
  """Reads seq from stdin; takes args M; prints the M largest in decending order."""
  M = int(sys.argv[1]) # The max # of elems to be stored at one time.
  pq = MinPQ(M+1)

  for line in fileinput.input(sys.argv[2:]):
    """Read stdin until ctrl-D is seen."""
    pq.insert(Transaction(line.rstrip("\n\r")))

    # remove minimum if M+1 entries on the PQ
    if pq.size() > M: 
      pq.delMin()

  # print entries on PQ in reverse order
  stack = Stack()
  for transaction in pq:
    stack.push(transaction)
  for transaction in stack:
    prt.write("{}\n".format(transaction))

if __name__ == '__main__':
  main()

# Java last updated: Thu Sep 24 14:16:15 EDT 2015.
