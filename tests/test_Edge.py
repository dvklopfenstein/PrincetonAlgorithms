#!/usr/bin/env python
"""Unit tests the Edge data type"""
# pylint: disable=invalid-name

from sys import stdout
from AlgsSedgewickWayne.Edge import Edge


def main():
    """Unit tests the Edge data type"""
    edge = Edge(v=12, w=34, weight=5.67)
    stdout.write(str(edge))
    assert edge.either() == 12
    assert edge.other(12) == 34
    assert edge.other(34) == 12

    edge_smaller = Edge(v=1, w=2, weight=1.0)
    edge_larger = Edge(v=1, w=2, weight=10.0)

    # edge is larger than edge_smaller
    assert edge.compare_to(edge_smaller) == 1

    # edge is smaller than edge_larger
    assert edge.compare_to(edge_larger) == -1

    # edge is equal in weight to itself
    assert edge.compare_to(edge) == 0


if __name__ == '__main__':
    main()
