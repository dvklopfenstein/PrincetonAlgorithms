#!/usr/bin/env python

from AlgsSedgewickWayne.ST import ST

def main():
  """Unit tests the ST data type."""
  st = ST()
  st.put("A", 1)
  st.put("B", 1)
  st.put("B", 2)
  st.put("B", 3)
  st.put("B", 4)

if __name__ == '__main__':
  main()
