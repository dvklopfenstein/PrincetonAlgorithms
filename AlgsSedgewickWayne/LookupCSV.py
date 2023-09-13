# TBD: Do Python Implementation

from AlgsSedgewickWayne.ST import ST
import sys
import fileinput

def main():
  keyField = int(sys.argv[1])
  valField = int(sys.argv[2])

  st = ST()

  # Command-line interface: reads data from stdin, stream, or files
  items_in = [w.rstrip("\n\r") for t in fileinput.input() for w in t.split(" ")]
  # read in the data from csv file
  In in = new In(args[0])
  while (in.hasNextLine()):
    String line = in.readLine()
    String[] tokens = line.split(",")
    String key = tokens[keyField]
    String val = tokens[valField]
    st.put(key, val)

  while (!StdIn.isEmpty()):
    String s = StdIn.readString()
    if st.contains(s)) prt.write(st.get(s))
    else                prt.write("Not found")

if __name__ == '__main__':
  main()

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015,      DV Klopfenstein, Python port
