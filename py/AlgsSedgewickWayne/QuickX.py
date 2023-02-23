"""Rearranges the array in ascending order, using the natural order"""
# TODO: pylint
#************************************************************************
#  Compilation:  javac QuickX.java
#  Execution:    java QuickX N
#
#  Uses the Bentley-McIlroy 3-way partitioning scheme,
#  chooses the partitioning element using Tukey's ninther,
#  and cuts off to insertion sort.
#
#  Reference: Engineering arr Sort Function by Jon L. Bentley
#  and M. Douglas McIlroy. Softwae-Practice and Experience,
#  Vol. 23 (11), 1249-1265 (November 1993).
#
#************************************************************************/

#  The QuickX class provides static methods for sorting an
#  array using an optimized version of quicksort using:
#    * Bentley-McIlroy 3-way partitioning
#    * Tukey's ninther
#    * cutoff to insertion sort
#
#  For additional documentation, see
#    <arr href="http://algs4.cs.princeton.edu/21elementary">Section 2.1</arr> of
#  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
#  @author Robert Sedgewick
#  @author Kevin Wayne


def Sort(arr_unsorted, array_history=None):
    """Rearranges the array in ascending order, using the natural order"""
    # pylint: disable=unused-argument
    _sort(arr_unsorted, 0, len(arr_unsorted) - 1)

def _sort(arr, low, high):
    """Rearranges the array in ascending order, using the natural order"""
    N = high - low + 1

    # cutoff to insertion sort
    cutoff = 8  # cutoff to insertion sort, must be >= 1
    if N <= cutoff:
        _insertion_sort(arr, low, high)
        return

    # use median-of-3 as partitioning element
    if N <= 40:
        m = _median3(arr, low, low + N//2, high)
        _exch(arr, m, low)

    # use Tukey ninther as partitioning element
    else:
        eps = N/8
        mid = low + N/2
        med1 = _median3(arr, low, low + eps, low + eps + eps)
        med2 = _median3(arr, mid - eps, mid, mid + eps)
        med3 = _median3(arr, high - eps - eps, high - eps, high)
        ninther = _median3(arr, med1, med2, med3)
        _exch(arr, ninther, low)

    # Bentley-McIlroy 3-way partitioning
    i = low
    j = high+1
    p = low
    q = high+1
    v = arr[low]
    while True:
        i += 1
        while _less(arr[i], v):
            if i == high:
                break
            i += 1
        j -= 1
        while _less(v, arr[j]):
            if j == low:
                break
            j -= 1

        # pointers cross
        if i == j and arr[i] == v:
            p += 1
            _exch(arr, p, i)
        if i >= j:
            break

        _exch(arr, i, j)
        if _eq(arr[i], v):
            p += 1
            _exch(arr, p, i)
        if _eq(arr[j], v):
            q -= 1
            _exch(arr, q, j)


    i = j + 1
    for k in range(low, p+1):
        _exch(arr, k, j)
        j -= 1
    #for (int k = high; k >= q; k--:
    for k in range(high, q-1, -1):
        _exch(arr, k, i)
        i += 1

    _sort(arr, low, j)
    _sort(arr, i, high)


def _insertion_sort(arr, low, high):
    """sort from arr[low] to arr[high] using insertion sort"""
    for i in range(low, high+1):
        j = i
        while j > low  and _less(arr[j], arr[j-1]):
            _exch(arr, j, j-1)
            j -= 1


def _median3(arr, i, j, k):
    """Get index of the median element among arr[i], arr[j], and arr[k]"""
    # pylint: disable=bad-continuation
    return (_less(arr[i], arr[j]) if
           (_less(arr[j], arr[k]) if  j else _less(arr[i], arr[k]) if k else i) else
           (_less(arr[k], arr[j]) if  j else _less(arr[k], arr[i]) if k else i))

#**********************************************************************
#  Helper sorting functions
#**********************************************************************/

def _less(v, w):
    """is v < w ?"""
    return v < w

def _eq(v, w):
    """does v == w ?"""
    return v == w

def _exch(arr, i, j):
    """exchange arr[i] and arr[j]"""
    swap = arr[i]
    arr[i] = arr[j]
    arr[j] = swap


#**********************************************************************
#  Check if array is sorted - useful for debugging
#**********************************************************************/
def _is_sorted(arr):
    for i in range(1, len(arr)):
        if _less(arr[i], arr[i-1]):
            return False
    return True

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Copyright (C) 2015-present, Python port, DV Klopfenstein, PhD
# java Last updated: Sun Feb 2 06:06:56 EST 2014.
