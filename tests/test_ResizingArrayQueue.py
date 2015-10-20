#!/usr/bin/env python
"""Test ResizingArrayQueue.py."""

from AlgsSedgewickWayne.ResizingArrayQueue import ResizingArrayQueue
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

import sys

def run(item_list):
  """Unit tests the ResizingArrayQueue data type."""
  sys.stdout.write("\nRUNNING: {}\n".format(' '.join(item_list)))
  q = ResizingArrayQueue()
  for item in item_list:
    if item != "-":
      q.enqueue(item)
    else: sys.stdout.write("  DEQUEUE: {}\n".format(q.dequeue()))
  sys.stdout.write("({} left on queue): {}\n".format(q.size(), q))

def default_example():
  """Run simple example."""
  run(cli_get_array("a b c d - - e f - - g h i -"))
  run(cli_get_array("a - b - c d - - e f - - g h i -"))


if __name__ == '__main__':
  # If user did not provide a sequence.
  if len(sys.argv) == 1:
    default_example()
  # If user provided a sequence in the runtime arguments.
  else:
    run(cli_get_array())
