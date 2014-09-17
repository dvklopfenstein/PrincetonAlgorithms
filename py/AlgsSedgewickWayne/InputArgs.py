#!/usr/bin/python

import sys
import os

def getStrArray(default_seq=None):
  argv_len = len(sys.argv)

  # If user provides an argument at runtime, it will either be:
  #   1. The name of a file whilc contains a sequence of ints (one per line)
  #   2. A string which is a sequence of either strings or ints
  if argv_len > 1:
    for arg in sys.argv[1:]:
      if os.path.isfile(arg):
        return get_ints_from_file(arg)
      else:
        return get_seq__int_or_str(arg.split())

  # If the user provided a default example embedded in the code and 
  # did not provide a sequence at runtime using command line arguments.
  if default_seq is not None:
    # Returns a sequence containing either ints (if all items are ints) or strings
    _prt_usage_msg(default_seq)
    print "DFLT:", default_seq
    return get_seq__int_or_str(default_seq.split())
  else:
    _prt_usage_msg()


def _prt_usage_msg(default_seq="a f b d g e c"):
  import inspect
  # Get the name of the calling script (or module, i.e. mod)
  frm = inspect.stack()[2]
  mod = inspect.getmodule(frm[0])
  # Let the user know that they can provide a sequence at run-time.
  print """
    You may provide a list of elements on the command line.  For example:
 
      {CMD} "{SEQ}"

  """.format(CMD=mod.__file__, SEQ=default_seq)



def get_seq__int_or_str(lst):
  """Return a list of ints if string contains a sequence of ints."""
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
