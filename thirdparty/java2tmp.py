#!/usr/bin/env python

import sys
import os
import re

def main(prt=sys.stdout):
  fin  = get_fin()
  module, fout_py, fout_test = get_fouts(fin)
  FOUT = None if fout_py is None else open(fout_py, 'w')
  TEST = None if fout_test is None else open(fout_test, 'w')
  cwdvk = "# Copyright 2015-2016, DV Klopfenstein, Python implementation. All rights reserved."
  cw = None
  #FOUT.write("#!/usr/bin/env python\n")
  with open(fin) as FIN:
    loc = "start"
    if FOUT: FOUT.write("\n# TBD Finish Python port\n\n")
    if TEST: 
      TEST.write("#!/usr/bin/env python\n")
      TEST.write("# TBD Finish Python port\n\n")
      TEST.write("import sys\n")
      TEST.write("from AlgsSedgewickWayne.{M} import {M}\n\n".format(M=module))
    for line in FIN:
      if loc == "start" and line.startswith("/*******************"):
        loc = "hdr"
      elif loc == "hdr" and line.startswith(" ********************"):
        loc = "body"
      elif loc == "body" and line.startswith("    public static void main"):
        loc = "main"
        line = "def test_0(prt=sys.stdout):\n"
      elif loc == "main" and line.startswith(" *  Copyright"):
        loc = "copyright"
        cw = line.replace("2015", "2016")
        cw = cw.replace(" * ", "#")
        cw = ''.join([cw, cwdvk])
        break
      line = line.replace("/**", "#")
      line = line.replace(" * ", "#")
      line = line.replace(" *\n", "#\n")
      line = line.replace(" */", "#")
      if chk_end(line): continue
      if line[:4] == "    ": line = line[2:]
      line = chk_if(line)
      line = line.replace('== null', 'is None')
      line = line.replace('!= null', 'is not None')
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
      line = line.replace('this', 'self')
      line = line.replace(r'//', '#')
      line = line.replace(r'&&', 'and')
      line = line.replace(r'||', 'or')
      line = line.replace(r'throw', 'raise')
      line = line.replace(r'null', 'None')
      line = chk_semi(line)
      line = chk_start(line)
      line = chk_private(line)
      line = chk_public(line)
      line = chk_else(line)
      line = re.sub(r'([a-zA-Z0-9]+)\.length', r'len(\1)', line)
      line = line.replace(' int ',' ')
      line = line.replace('else if', 'elif')
      line = line.replace('Last updated', 'Java last updated')
      line = line.replace('++', ' += 1')
      line = line.replace('--', ' -= 1')
      line = line.replace('!', 'not ')
      line = line.replace('StdOut.println', 'prt.write')
      line = line.replace('StdOut.print', 'prt.write')
      line = chk_def(line)
      if loc == "body":
        if FOUT: FOUT.write(line)
      if loc in ["hdr", "main"]:
        if TEST: TEST.write(line)

  if FOUT:
    FOUT.write('\n\n{}\n\n'.format(cw if cw is not None else cwdvk))
  if TEST:
    TEST.write('if __name__ == "__main__":\n  test_0()\n\n{}\n\n'.format(cw))
  prt.write('  READ: {}\n'.format(fin))

  module, fpy, ftst = get_foutnames(fin)
  if fout_py is not None and FOUT is not None: 
    FOUT.close()
    prt.write('  WROTE: {}\n'.format(fout_py))
  else:
    prt.write('  EXISTS: {}\n'.format(fpy))
  if fout_test is not None and TEST is not None: 
    TEST.close()
    prt.write('  WROTE: {}\n'.format(fout_test))
  else:
    prt.write('  EXISTS: {}\n'.format(ftst))


def chk_def(line):
  if "def " in line:
    pass
  return line

def chk_else(line):
 A = re.search(r'^(\s*)else(\s+)(return\s+.*)$', line)
 if A:
   return '{}else:{}{}\n'.format(A.group(1), A.group(2), A.group(3))
 return line

def chk_public(line):
 A = re.search(r'^(\s*)(public .*\S\s+)([a-zA-Z0-1_]+)\s*(\(.*)$', line)
 if A:
   return '{}def {}{}\n'.format(A.group(1), A.group(3), A.group(4))
 return line

def chk_private(line):
 A = re.search(r'^(\s*)(private .*\S\s+)([a-zA-Z0-1_]+)\s*(\(.*)$', line)
 if A:
   return '{}def _{}{}\n'.format(A.group(1), A.group(3), A.group(4))
 return line

def chk_if(line):
 A = re.search(r'^(\s*if\s+)\((.*)$', line)
 if A:
   return '{}{}\n'.format(A.group(1), A.group(2))
 return line

def chk_start(line):
 A = re.search(r'^(.*\S)(\s*{)(.*)$', line)
 if A:
   return '{}:{}\n'.format(A.group(1), A.group(3))
 return line

def chk_semi(line):
 A = re.search(r'^(.*)\s*;\s*$', line)
 if A:
   return '{}\n'.format(A.group(1))
 return line

def chk_end(line):
 A = re.search(r'^\s*}\s*$', line)
 if A:
   return True
 return False


def get_foutnames(fin):
  fout_py = os.path.basename(fin).replace(".java", ".py")
  odir = get_odir()
  return [
    os.path.splitext(fout_py)[0],
    os.path.join("../py/AlgsSedgewickWayne/" if odir is None else odir, fout_py),
    os.path.join("../tests/" if odir is None else odir, ''.join(["test_", fout_py]))]

def get_fouts(fin):
  module, fout_py, fout_test = get_foutnames(fin)
  return [
    module,
    fout_py   if not os.path.isfile(fout_py) else None,
    fout_test if not os.path.isfile(fout_py) else None]
  
def get_odir():
  for arg in sys.argv[1:]:
    mtch = re.search(r'odir=(\S+)', arg)
    if mtch:
      return mtch.group(1)
  return None


def get_fin():
  if len(sys.argv) >= 2 and os.path.isfile(sys.argv[1]) and 'java' in sys.argv[1]:
    return sys.argv[1]
  raise Exception("YOUR INPUT NEEDS TO BE A JAVA FILE")
    

if __name__ == '__main__':
  main()
