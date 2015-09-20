#!/usr/bin/python

import sys
import os

def getStrArray(default_seq=None):
  argv_len = len(sys.argv)

  # If user provides an argument at runtime, it will either be:
  #   1. The name of a file whilc contains a sequence of ints (one per line)
  #   2. A string which is a sequence of either strings or ints
  if argv_len > 1:
    return get_list_from_args()

  # If the user provided a default example embedded in the code and
  # did not provide a sequence at runtime using command line arguments.
  if default_seq is not None:
    # Returns a sequence containing either ints (if all items are ints) or strings
    _prt_usage_msg(default_seq)
    print "DFLT:", default_seq
    return get_seq__int_or_str(default_seq)
  else:
    _prt_usage_msg()

  return []


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


def get_list_from_args():
  if len(sys.argv) == 2:
    arg = sys.argv[1]
    if os.path.isfile(arg):
      return get_list_from_file(arg)
    else:
      return get_seq__int_or_str(arg)
  else:
    return conv_int(sys.argv[1:])

def get_seq__int_or_str(seqstr):
  """Return a list of ints if string contains a sequence of ints."""
  return conv_int(seqstr.split())

def conv_int(lst):
  """Converts a list element to an int if it is an int. Leaves it if not."""
  get_val = lambda a: int(a) if a.isdigit() else a
  return [get_val(a) for a in lst]

def get_list_from_file(fin):
  data = []
  with open(fin) as FIN:
    for line in FIN:
      line = line.rstrip()
      val = int(line) if line.isdigit() else line
      data.append(val)
  return data

if __name__ == '__main__':
  print getStrArray("9 1 6 3 8 5 2")
