#!/usr/bin/env python

#*****************************************************************************
 #  Compilation: javac MSD.java
 #  Execution:   java MSD < input.txt
 #  Dependencies: StdIn.java StdOut.java 
 #
 #  Sort an array of strings or integers using MSD radix sort.
 #
 #  % java MSD < shells.txt 
 #  are
 #  by
 #  sea
 #  seashells
 #  seashells
 #  sells
 #  sells
 #  she
 #  she
 #  shells
 #  shore
 #  surely
 #  the
 #  the
 #
 #*****************************************************************************/

import sys
from AlgsSedgewickWayne.MSD import sort
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

def main(seqinfo, prt=sys.stdout):
  """MSD radix sorts sequence of extended ASCII strings and prints in ascending order."""
  a = cli_get_array(seqinfo)
  N = len(a)
  sort(a)
  prt.write("{}\n".format(a))

if __name__ == '__main__':
  main("../thirdparty/shells.txt")
