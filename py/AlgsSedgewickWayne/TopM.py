#!/usr/bin/env python
"""Read seq. Print N largest items."""

import sys
import fileinput
from AlgsSedgewickWayne.MinPQ import MinPQ
from AlgsSedgewickWayne.Transaction import Transaction

def main(prt=sys.stdout):
  """Reads seq from stdin; takes args M; prints the M largest in decending order."""
  M = int(sys.argv[1]) if len(sys.argv) > 1 else 1
  prt.write("M({})\n".format(M))
  pq = MinPQ(M+1)

  for line in fileinput.input():
    """Read stdin until ctrl-D is seen."""
    transaction = Transaction(line.rstrip("\n\r"))
  #    pq.insert(transaction)

  #    # remove minimum if M+1 entries on the PQ
  #    if pq.size() > M) 
  #        pq.delMin()
  #}   # top M entries are on the PQ

  ## print entries on PQ in reverse order
  #Stack<Transaction> stack = new Stack<Transaction>()
  #for (Transaction transaction : pq)
  #    stack.push(transaction)
  #for (Transaction transaction : stack)
  #    StdOut.println(transaction)

if __name__ == '__main__':
  main()

# Java last updated: Thu Sep 24 14:16:15 EDT 2015.
