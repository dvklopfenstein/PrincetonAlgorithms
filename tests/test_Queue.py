#!/usr/bin/env python
""" Tests Queue."""

import sys
from AlgsSedgewickWayne.Queue import Queue
from AlgsSedgewickWayne.testcode.ArrayHistory import run_Queue


def test_wk2_ex_Queues_608030():
  """(seed = 608030)"""
  # Question 2
  # Suppose that an intermixed sequence of 10 enqueue and 10
  # dequeue operations are performed on a FIFO queue. The
  # enqueues add the letters 0 through 9 in order; the dequeues
  # print out the return value. Which of the following output
  # sequence(s) could occur?
  # r = run_Queue(Queue(), "0 1 2 3 4 5 6 7 8 9")
  r = run_Queue(Queue(), "0 - 1 2 - 3 4 5 6 7 8 9")
  #assert r == "0 2 1 3 7 4 9 6 8 5"

  r = run_Queue(Queue(), "0 1 2 - - - 3 4 5 - 6 - - 7 8 9")
  #assert r == "0 1 2 5 6 4 8 9 3 7"

  result = run_Queue(Queue(), "0 1 2 3 4 5 6 7 8 9 - - - - - - - - - -")
  assert result == "0 1 2 3 4 5 6 7 8 9"

  r = run_Queue(Queue(), "0 - 1 2 3 4 5 6 7 8 9")
  #assert r == "0 7 4 1 8 3 6 2 9 5"

  r = run_Queue(Queue(), "0 - 1 2 3 4 5 6 7 8 9")
  #assert r == "0 4 5 1 8 6 2 3 9 7"

def test_wk2_ex_Queues_511394():
  """(seed = 511394)"""
  # Suppose that an intermixed sequence of 10 enqueue and 10
  # dequeue operations are performed on a FIFO queue. The
  # enqueues add the letters 0 through 9 in order; the dequeues
  # print out the return value. Which of the following output
  # sequence(s) could occur?
  r = run_Queue(Queue(), "0 1 - - 2 3 4 - 5 6 7 8 9")
  #assert r == "0 1 4 9 6 8 5 2 7 3"
  #assert r == "0 1 2 3 4 5 8 9 6 7"
  #assert r == "0 1 2 4 8 6 5 9 7 3"
  #assert r == "0 1 2 3 4 7 6 8 5 9"
  #assert r == "0 1 2 3 4 5 6 7 8 9"

def run_all():
  """Run all tests."""
  test_wk2_ex_Queues_608030()
  test_wk2_ex_Queues_511394()

if __name__ == '__main__':
  if len(sys.argv) == 1:
    run_all()
  else:
    run_Queue(Queue(), sys.argv[1])
