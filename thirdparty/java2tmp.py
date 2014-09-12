#!/usr/bin/env python

import sys
import os
import re

def main():
  fin  = get_fin()
  fout = get_fout( fin )
  FOUT = sys.stdout if fout is None else open(fout, 'w')
  FOUT.write("#!/usr/bin/env python")
  with open(fin) as FIN:
    for line in FIN:
      if chk_com(FOUT, r'^(\s*)\/\*(.*)$', line): continue
      if chk_com(FOUT, r'^(\s*)\*(.*)$',   line): continue
      if chk_end(FOUT, line): continue
      line = chk_if(FOUT, line)
      line = line.replace('true',  'True')
      line = line.replace('false', 'False')
      line = line.replace('Comparable[] ', '')
      line = line.replace('Comparable ', '')
      line = line.replace('Object[] ', '')
      line = line.replace('Object', '')
      line = line.replace('Key[] ', '')
      line = line.replace('Key', '')
      line = line.replace('Node[] ', '')
      line = line.replace('Node', '')
      line = line.replace(r'//', '#')
      line = line.replace(r'&&', 'and')
      line = line.replace(r'||', 'or')
      line = line.replace(r'throw', 'raise')
      line = line.replace(r'null', 'None')
      line = chk_semi(FOUT, line)
      line = chk_start(FOUT, line)
      line = chk_private(FOUT, line)
      line = chk_public(FOUT, line)
      line = chk_else(FOUT, line)
      line = re.sub(r'([a-zA-Z0-9]+)\.length', r'len(\1)', line)
      line = line.replace(' int ',' ')
      line = line.replace('else if', 'elif')
      line = line.replace('Last updated', 'Java last updated')
      line = line.replace('++', ' += 1')
      line = line.replace('--', ' -= 1')
      FOUT.write(line)

  print 'READ ', fin

  if fout is not None: 
    FOUT.close()
    print 'WROTE', fout
  else:
    print "VIEW ", get_foutname( fin )

def chk_else(FOUT, line):
 A = re.search(r'^(\s*)else(\s+)(return\s+.*)$', line)
 if A:
   return '{}else:{}{}\n'.format(A.group(1), A.group(2), A.group(3))
 return line

def chk_public(FOUT, line):
 A = re.search(r'^(\s*)(public .*\S\s+)([a-zA-Z0-1_]+)\s*(\(.*)$', line)
 if A:
   return '{}def {}{}\n'.format(A.group(1), A.group(3), A.group(4))
 return line

def chk_private(FOUT, line):
 A = re.search(r'^(\s*)(private .*\S\s+)([a-zA-Z0-1_]+)\s*(\(.*)$', line)
 if A:
   return '{}def _{}{}\n'.format(A.group(1), A.group(3), A.group(4))
 return line

def chk_if(FOUT, line):
 A = re.search(r'^(\s*if\s+)\((.*)$', line)
 if A:
   return '{}{}\n'.format(A.group(1), A.group(2))
 return line

def chk_start(FOUT, line):
 A = re.search(r'^(.*\S)(\s*{)(.*)$', line)
 if A:
   return '{}:{}\n'.format(A.group(1), A.group(3))
 return line

def chk_semi(FOUT, line):
 A = re.search(r'^(.*)\s*;\s*$', line)
 if A:
   return '{}\n'.format(A.group(1))
 return line


def chk_end(FOUT, line):
 A = re.search(r'^\s*}\s*$', line)
 if A:
   return True
 return False

def chk_com(FOUT, pat, line):
 A = re.search(pat, line)
 if A:
   FOUT.write('{}{}{}\n'.format(A.group(1), '#', A.group(2)))
   return True
 return False


def get_foutname(fin):
  return os.path.join("../py/AlgsSedgewickWayne/", fin.replace(".java", ".py"))

def get_fout(fin):
  fout = get_foutname(fin)
  if not os.path.isfile(fout):
    return fout
  return None
  

def get_fin():
  if len(sys.argv) >= 2 and os.path.isfile(sys.argv[1]) and 'java' in sys.argv[1]:
    return sys.argv[1]
  raise Exception("YOUR INPUT NEEDS TO BE A JAVA FILE")
    

if __name__ == '__main__':
  main()
