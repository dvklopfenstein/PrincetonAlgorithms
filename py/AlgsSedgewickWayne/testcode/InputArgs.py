#!/usr/bin/python

import sys
import os
import fileinput
import re

def cli_get_array(seqstr=None):
  """Command-line interface: reads data from arg, stdin, stream, or files."""
  if seqstr is not None:
    return arr_int_str(seqstr.split(" "))
  # >>> [file.py] "A B C D E F"
  # >>> [file.py] "1 2 3 4 5 6"
  if len(sys.argv) == 2 and not os.path.isfile(sys.argv[1]):
    a = arr_int_str(sys.argv[1].split(" "))
    if a is not None:
      return a
  # >>> echo "A B C D E F" | [file.py]
  # >>> echo "1 2 3 4 5 6" | [file.py]
  # >>> [file.py] # And then enter elems 1 at a time on stdin. End with two ctrl-Ds
  a = [w.strip(" \n\r") for t in fileinput.input() for w in t.splitlines()]
  if len(a) == 1 and re.search(r'[(\S+\s+)]+', a[0]):
    return arr_int_str(a[0].split(" "))
  # >>> test_Quick.py ../thirdparty/1Kints.txt
  if a is not None:
    return arr_int_str(a)

def arr_int_str(a):
  """Return an array of ints or strs."""
  isdigit = True 
  for elem in a:
    M = re.search(r'^([0-9.\-eE ]+)$', elem)
    if not M:
      isdigit = False
      break
  if not isdigit:
    return a
  if isdigit:
    return [int(e) for e in a]




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



if __name__ == '__main__':
  print cli_get_array("9 1 6 3 8 5 2")
