#!/usr/bin/env python

import sys
from AlgsSedgewickWayne.Date import Date

def main(prt=sys.stdout):
  """unit test for Date, ported to Python from Java."""
  today = Date(2, 25, 2004)
  prt.write("{}\n".format(today))
  for i in range(10):
      today = today.next()
      prt.write("{} {}\n".format(i, today))

  assert (today > today.next()) == False
  assert (today > today) == False
  assert (today.next() > today) == True

  birthday = Date(10, 16, 1971)
  prt.write("{}\n".format(birthday))
  for i in range(10):
    birthday = birthday.next()
    prt.write("{}\n".format(birthday))


if __name__ == '__main__':
  main()
