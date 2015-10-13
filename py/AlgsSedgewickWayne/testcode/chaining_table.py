
import sys

def prt_chaining_symtbl(st):
  prt = sys.stdout
  prt.write("INNARDS OF SEPARATE CHAINING SYMBOL TABLE:\n")
  for idx, linkedlist in enumerate(st.st):
    prt.write("  st[{I}] {ST}\n".format(I=idx, ST=linkedlist))
    for chnum, chain_elem in enumerate(linkedlist):
      prt.write("    chain_elem[{I}] {ST}\n".format(I=chnum, ST=chain_elem))
  
