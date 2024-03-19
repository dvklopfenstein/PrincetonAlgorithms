#!/usr/bin/env python3
"""Test Date class implementation"""

import sys
from AlgsSedgewickWayne.Date import Date

def test_date(prt=sys.stdout):
    """unit test for Date, ported to Python from Java."""
    start_date = Date(2, 25, 2004)
    prt.write(f"START DATE: {start_date}\n")
    for i in range(10):
        start_date = start_date.next()
        prt.write(f"{i} {start_date}\n")

    assert start_date <= start_date.next()
    assert start_date <= start_date
    assert start_date.next() > start_date
    assert start_date == start_date

    birthday = Date(10, 16, 1971)
    prt.write(f"{birthday}\n")
    for i in range(10):
        birthday = birthday.next()
        prt.write(f"{birthday}\n")


if __name__ == '__main__':
    test_date()
