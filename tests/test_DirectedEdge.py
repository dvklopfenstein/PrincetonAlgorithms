#!/usr/bin/env python3
"""Test directed edge"""

from AlgsSedgewickWayne.DirectedEdge import DirectedEdge


def test_directed_edge():
    """Test directed edge"""
    edge = DirectedEdge(12, 34, 5.67)
    txt = str(edge)
    assert txt == "12 -> 34  5.67"
    print(txt)


if __name__ == '__main__':
    test_directed_edge()
