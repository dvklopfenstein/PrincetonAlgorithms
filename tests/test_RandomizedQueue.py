#!/usr/bin/env python

import sys
import fileinput
from AlgsSedgewickWayne.RandomizedQueue import RandomizedQueue
import numpy as np

def test_4a(prt=sys.stdout):
  rq = RandomizedQueue()
  rq.enqueue(0)
  prt.write("{}\n".format(str(rq)))
  prt.write("{:>5} sample\n".format(rq.sample())) #  ==> 58
  prt.write("{:>5} isEmpty()\n".format(rq.isEmpty()))   #  ==> false
  prt.write("{:>5} deque()\n".format(rq.dequeue()))   #  ==> 58
  prt.write("{}\n".format(str(rq)))
  rq.enqueue(1)
  prt.write("{:>5} sample\n".format(rq.sample())) #  ==> 58
  rq.enqueue(2)
  rq.enqueue(3)
  rq.enqueue(4)
  rq.enqueue(5)
  prt.write("{}\n".format(str(rq)))
  rq.dequeue()
  rq.dequeue()
  prt.write("{}\n".format(str(rq)))
  for e in rq: 
    prt.write("E  {}\n".format(e))
    for f in rq:
      prt.write("F  {}\n".format(e))

def test_ed(prt=sys.stdout):
  rq = RandomizedQueue()
  for e in range(16): rq.enqueue(e)
  for e in range(16): rq.dequeue()

def test_red(N=20, prt=sys.stdout):
  rq = RandomizedQueue()
  cmds = [
    lambda e: rq.enqueue(e), 
    lambda e: rq.size() if rq.isEmpty() else rq.dequeue()]
  C = len(cmds)
  for e in range(N):
    cmds[np.random.randint(0, C)](e)
  prt.write("PRINTING {} ITEMS:\n".format(rq.size()))
  rq.prt(">>")
  for e in rq:
    prt.write("{}\n".format(e))



def main(prt=sys.stdout): # unit testing
  q = RandomizedQueue()
  #a = [w.rstrip("\n\r") for t in fileinput.input() for w in t.split(" ")]
  for item in fileinput.input():
    """Read stdin until ctrl-D is seen."""
    item = item.rstrip("\n\r")
    if item.equals("."): break
    elif not item.equals("-"): q.enqueue(item)
    elif not q.isEmpty(): prt.write("{}\n".format(q))
  prt.write("({SZ} left on queue)\n".format(SZ=q.size()))

def run_all(prt=sys.stdout):
  #test_4a(prt)
  #test_ed(prt)
  test_red(10, prt)

def cli(prt=sys.stdout):
  if len(sys.argv) > 1:
    main(prt)
  else:
    run_all(prt)
  
if __name__ == '__main__':
  cli()
