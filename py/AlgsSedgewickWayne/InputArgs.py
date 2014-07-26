#!/usr/bin/python

import sys
import os

def getStrArray():
  if len(sys.argv) == 1:
    raise Exception("YOU MUST PROVIDE A LIST OF ELEMENTS")
  for arg in sys.argv[1:]:
    if os.path.isfile(arg):
      raise Exception("TIME TO IMPLEMENT READING DATA FROM A FILE")
    else:
      return arg.split()
  

if __name__ == '__main__':
  print getStrArray()
