#!/usr/bin/python

import sys
import os
import inspect

def getStrArray(default_seq=None):
  if default_seq is not None and len(sys.argv) == 1:
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    print "You may provide a list of elements on the command line:"
    print '  {} "{}"\n'.format(mod.__file__, default_seq)
    print "DFLT:", default_seq
    return chk_digits(default_seq.split())
  for arg in sys.argv[1:]:
    if os.path.isfile(arg):
      return get_ints_from_file(arg)
    else:
      return chk_digits(arg.split())

def chk_digits(lst):
  intlist = [int(a) for a in lst if a.isdigit()]
  return intlist if len(lst) == len(intlist) else lst
    
def get_ints_from_file(fin):
  data = []
  with open(fin) as FIN:
    for line in FIN:
      data.append(int(line))
  return data
  

if __name__ == '__main__':
  print getStrArray("9 1 6 3 8 5 2")
