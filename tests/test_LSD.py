#!/usr/bin/env python

#*****************************************************************************
 #  Compilation:  javac LSD.java
 #  Execution:    java LSD < input.txt
 #  Dependencies: StdIn.java StdOut.java 
 #
 #  LSD radix sort
 #
 #    - Sort a String[] array of N extended ASCII strings (R = 256), each of length W.
 #
 #    - Sort an int[] array of N 32-bit integers, treating each integer as 
 #      a sequence of W = 4 bytes (R = 256).
 #
 #  Uses extra space proportional to N + R.
 #
 #
 #  % java LSD < words3.txt
 #  all
 #  bad
 #  bed
 #  bug
 #  dad
 #  ...
 #  yes
 #  yet
 #  zoo
 #
 #*****************************************************************************/

from AlgsSedgewickWayne.LSD import sort
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array
import sys
import itertools

def main(seqinfo, prt=sys.stdout):
  """LSD radix sorts fixed-length strings and prints them in ascending order."""
  a = cli_get_array(seqinfo)
  a = list(itertools.chain(*a)) # Flatten list 
  N = len(a)
  sort(a) # sort the strings
  prt.write("{}\n".format(' '.join(a)))

if __name__ == '__main__':
  main("../thirdparty/words3.txt")
