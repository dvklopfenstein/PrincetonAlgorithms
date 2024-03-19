#!/usr/bin/env python
"""Test Knuth Shuffle: An application of sort"""

import sys
from AlgsSedgewickWayne.knuth_shuffle import shuffle
from AlgsSedgewickWayne.testcode.InputArgs import cli_get_array

# Reads in a sequence of strings from standard input, shuffles
# them, and prints out the results.
def test_knuth_shuffle():
    """Test Knuth Shuffle: An application of sort"""

    # read in the data
    arr = cli_get_array("a b c d e f")

    # shuffle the array
    shuffle(arr)

    # print results.
    sys.stdout.write(f"{' '.join(str(i) for i in arr)}\n")


if __name__ == '__main__':
    test_knuth_shuffle()
