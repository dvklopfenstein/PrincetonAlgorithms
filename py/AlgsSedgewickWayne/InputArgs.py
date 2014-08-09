#!/usr/bin/python

import sys
import os
import inspect

def getStrArray(default_seq):
  if len(sys.argv) == 1:
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    print "You may provide a list of elements on the command line:"
    print '  {} "{}"\n'.format(mod.__file__, default_seq)
    print "DFLT:", default_seq
    return chk_digits(default_seq.split())
  for arg in sys.argv[1:]:
    if os.path.isfile(arg):
      raise Exception("TIME TO IMPLEMENT READING DATA FROM A FILE")
    else:
      return chk_digits(arg.split())

def chk_digits(lst):
  intlist = [int(a) for a in lst if a.isdigit()]
  return intlist if len(lst) == len(intlist) else lst
    

if __name__ == '__main__':
  print getStrArray("9 1 6 3 8 5 2")
