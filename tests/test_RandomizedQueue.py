#!/usr/bin/env python

import sys
import fileinput
from AlgsSedgewickWayne.RandomizedQueue import RandomizedQueue

def test_4a(prt=sys.stdout):
  rq = RandomizedQueue()
  rq.enqueue(58)
  prt.write("{}\n".format(str(rq)))
  prt.write("{:>5} sample\n".format(rq.sample())) #  ==> 58
  prt.write("{:>5} isEmpty()\n".format(rq.isEmpty()))   #  ==> false
  prt.write("{:>5} deque()\n".format(rq.dequeue()))   #  ==> 58
  prt.write("{}\n".format(str(rq)))
  rq.enqueue(194)
  prt.write("{:>5} sample\n".format(rq.sample())) #  ==> 58
  rq.enqueue(200)
  rq.enqueue(201)
  rq.enqueue(202)
  rq.enqueue(203)
  prt.write("{}\n".format(str(rq)))
  rq.dequeue()
  rq.dequeue()
  prt.write("{}\n".format(str(rq)))
  for e in rq: 
    print "E  ", e
    for f in rq:
      print "  F", f
  #prt.write("{:>5} sample\n".format(rq.sample()))

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
  test_4a(prt)

def cli(prt=sys.stdout):
  if len(sys.argv) > 1:
    main(prt)
  else:
    run_all(prt)
  
if __name__ == '__main__':
  cli()
