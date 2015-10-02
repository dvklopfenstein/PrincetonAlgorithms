#!/usr/bin/env python
"""Visualize the sizes of strings in columns from exercises (algs1:wk2/wk3)."""

from AlgsSedgewickWayne.testcode.utils import blk_visualizer

def test_849965():
  """Visualize arrays in columns."""
	# The column on the left contains an input array of 16
  # strings to be sorted; the column on the right contains the
  # strings in sorted order; each of the other 6 columns
  # contains the array at some intermediate step during either
  # insertion sort, selection sort, or shellsort (with different
  # columns potentially corresponding to different algorithms).

  # Unsorted                                         Sorted
  # col0   col1   col2   col3   col4   col5   col6   col7
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

def test_976184():
  block_str = """
    PINK   KISS   ACDC   BECK   ACDC   CAKE   ACDC   ACDC   
    TACO   FIXX   BECK   DIDO   BECK   ACDC   BECK   BECK   
    LIVE   LIVE   CAKE   JAYZ   DIDO   DIDO   CAKE   CAKE   
    BECK   BECK   DEVO   LIVE   JAYZ   BECK   DEVO   DEVO   
    TUFF   TUFF   DIDO   PINK   LIVE   KISS   DIDO   DIDO   
    JAYZ   JAYZ   JAYZ   TACO   PINK   FIXX   DOOM   DOOM   
    DIDO   DIDO   TUFF   TUFF   RUSH   DOOM   FIXX   FIXX   
    UB40   UB40   UB40   UB40   TACO   DEVO   JAYZ   JAYZ   
    RUSH   RUSH   RUSH   RUSH   TUFF   RUSH   RUSH   KISS   
    ACDC   ACDC   PINK   ACDC   UB40   JAYZ   PINK   LIVE   
    DOOM   DOOM   DOOM   DOOM   DOOM   LIVE   UB40   MOBY   
    DEVO   DEVO   TACO   DEVO   DEVO   MOBY   TACO   PINK   
    CAKE   CAKE   LIVE   CAKE   CAKE   TUFF   LIVE   RUSH   
    KISS   PINK   KISS   KISS   KISS   PINK   KISS   TACO   
    FIXX   TACO   FIXX   FIXX   FIXX   TACO   TUFF   TUFF   
    MOBY   MOBY   MOBY   MOBY   MOBY   UB40   MOBY   UB40   
"""
  blk_visualizer(block_str)

def test_131507():
  block_str = """
    moth   gnat   boar   boar   boar   bear   
    gnat   moth   calf   calf   calf   boar   
    deer   calf   deer   deer   deer   calf   
    calf   deer   gnat   gnat   duck   crow   
    lamb   boar   lamb   lamb   gnat   deer   
    boar   lamb   moth   moth   hare   duck   
    hare   duck   duck   duck   lamb   erne   
    duck   hare   erne   erne   moth   gnat   
    erne   bear   hare   hare   bear   hake   
    bear   erne   bear   bear   crow   hare   
    hake   crow   hake   crow   erne   lamb   
    crow   hake   crow   hake   hake   moth   
"""
  blk_visualizer(block_str)

def run_all():
  test_849965()
  test_976184()
  test_131507()

if __name__ == '__main__':
  run_all()
