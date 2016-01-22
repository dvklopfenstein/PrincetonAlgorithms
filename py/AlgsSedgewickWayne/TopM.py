#!/usr/bin/env python
"""Find the largest M items in a stream of N items."""

import sys
import fileinput
from AlgsSedgewickWayne.Transaction import Transaction
from AlgsSedgewickWayne.MinPQ import MinPQ
from AlgsSedgewickWayne.Stack import Stack

def main(prt=sys.stdout):
  """Reads seq from stdin; takes args M; prints the M largest in decending order."""
  M = int(sys.argv[1]) # The max # of elems to be stored at one time.
  pq = MinPQ(M+1)

  # Read stdin until ctrl-D is seen.
  for line in fileinput.input(sys.argv[2:]):
    pq.insert(Transaction(line.rstrip("\n\r")))
    if pq.size() > M: # rm min if M+1 entries on the PQ
      pq.delMin()

  # Print entries on PQ in reverse order
  stack = Stack()
  for transaction in pq:
    stack.push(transaction)
  for transaction in stack:
    prt.write("{}\n".format(transaction))

if __name__ == '__main__':
  main()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015. DV Klopfenstein. Python implementation.  All rights reserved.
# Java last updated: Thu Sep 24 14:16:15 EDT 2015.
