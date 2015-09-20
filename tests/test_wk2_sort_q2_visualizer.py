#!/usr/bin/env python

from AlgsSedgewickWayne.testcode.utils import blk_visualizer

def test_849965():
  """Visualize arrays in columns."""
	# The column on the left contains an input array of 16
  # strings to be sorted; the column on the right contains the
  # strings in sorted order; each of the other 6 columns
  # contains the array at some intermediate step during either
  # insertion sort, selection sort, or shellsort (with different
  # columns potentially corresponding to different algorithms).

  block_str = """
    slug   loon   crab   mule   carp   carp   carp   carp   
    crab   crab   hawk   crab   crab   crab   crab   crab   
    lynx   carp   lynx   lynx   hawk   frog   frog   frog   
    toad   frog   slug   toad   lynx   hawk   hawk   hawk   
    wren   mule   toad   wren   slug   loon   loon   loon   
    hawk   hawk   wren   hawk   toad   lynx   lynx   lynx   
    carp   lynx   carp   carp   wolf   mink   mink   mink   
    wolf   toad   wolf   wolf   wren   wolf   mule   mule   
    loon   worm   loon   loon   loon   wren   wren   pony   
    pony   pony   pony   pony   pony   pony   pony   slug   
    swan   mink   swan   swan   swan   swan   swan   swan   
    frog   tuna   frog   frog   frog   toad   toad   toad   
    worm   wren   worm   worm   worm   worm   worm   tuna   
    mule   slug   mule   slug   mule   mule   wolf   wolf   
    mink   swan   mink   mink   mink   slug   slug   worm   
    tuna   wolf   tuna   tuna   tuna   tuna   tuna   wren   
"""
  blk_visualizer(block_str)

def run_all():
  test_849965()

if __name__ == '__main__':
  run_all()
