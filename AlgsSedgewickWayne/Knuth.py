"""Shuffling using Knuth shuffle"""

import random

def shuffle(a):
  """Rearranges an array, a, of objects in uniformly random order"""
  for i in range(1, len(a)):
    # Knuth shuffle (03:00) Linear-time shuffling algorithm
    #   * In iteration i, pick integer r between 0 and i uniformly at random.
    #   * Swap a[i] and a[r]
    # COMMON BUG:      Choosing r between 0 and N-1 => Not Uniformly Random
    # CORRECT VARIANT: Choosing r between i and N-1
    r = random.randint(0, i-1) # random # between 0 and i
    a[i], a[r] = a[r], a[i]


# Alg1 Week 2 Lecture Shuffling

# 00:11 SHUFFLE SORT: An easy application of sorting to a related problem, called shuffling
# * Generate a random real number for each array entry
#   (Useful for shuffling columns in a spreadsheet)
# * Sort the array
#
# An effective way to shuffle an array is to generate a random number
# for each entry in the array.  Then sort the array using the random
# numbers as the key.
#
# PROPOSITION: Shuffle sort produces a uniformly random premutation
# of the input array, provided no duplicate values.
# (assuming real numbers uniformly at random)
# Well shuffled:  Every possible way of shuffling the deck appears with equal probability
#
# DRAWBACK: Need to pay cost of full sort?  NO, WE DO NOT HAVE TO PAY THAT COST...

# 01:32 KNUTH SHUFFLE DEMO: (Linear time shuffling algorithm)
# * In iteration i, pick integer r between 0 and i uniformly at random.
# * Swap a[i] and a[r]
#
# 03:31 PROPOSITION: [Fisher-Yates 1938] Knuth shuffling algorithm produces a
# uniformly random permutation of the input array in linear time.
# (Assuming integers uniformly chosen at random)

# KNUTH SHUFFLE
# * In iteration i, pick integer r between 0 and i uniformly at random.
#   Common bug: between 0 and N-1 (Does NOT give a uniformly random result)
#   Correct:    between i and N-1
# * Swap a[i] and a[r]

# WAR STORY (online poker) 05:10
#
#   # Shuffling algorithm in FAQ at www.planetpoker.com
#   for i := 1 to 52 do begin
#     r := random(51) + 1; # BUG: between 1 and 51
#     swap := card[r];
#     card[r] := card[i];
#     card[i] := swap;
#   end;
#
# BUG 1: Random number r never 52 => 52nd card can't end up in 52nd place.
# BUG 2: Shuffle not uniform (because choosing between 0 and N-1 instead of
#        between i and N-1.
# BUG 3: random() uses 32-bit seed => 2^32 possible shuffles (not enough)
# BUG 4: Seed = ms since midnight => Only 86.4 million shuffles
#
# EXPLOIT: After seeing 5 cards and synchronizing with server clock,
# can determine **all** future cards in real time!!
#
# "The generation of random numbers is too important to be left to chance."
#   - Robert R. Coveyou

# 07:05 BEST PRACTICES FOR SHUFFLING (IF YOUR BUSINESS DEPENDS ON IT).
# * Use a hardware random-number generator that has passed both
#   the FIPS 140-2 and the NIST statistical test suites.
# * Continously monitor statistical properties:
#   hardware random-number generators are fragile and fail silently
# * Use an unbiased shuffling algorithm.
#

# QUESTION: How many possible permuations are there in a deck of 52 playing cards?
# ANSWER:   52!



 #************************************************************************
 #  Compilation:  javac Knuth.java
 #  Execution:    java Knuth < list.txt
 #  Dependencies: StdIn.java StdOut.java
 #  Data files:   http:#algs4.cs.princeton.edu/11model/cards.txt
 #
 #  Reads in a list of strings and prints them in random order.
 #  The Knuth (or Fisher-Yates) shuffling algorithm guarantees
 #  to rearrange the elements in uniformly random order, under
 #  the assumption that Math.random() generates independent and
 #  uniformly distributed numbers between 0 and 1.
 #
 #  % more cards.txt
 #  2C 3C 4C 5C 6C 7C 8C 9C 10C JC QC KC AC
 #  2D 3D 4D 5D 6D 7D 8D 9D 10D JD QD KD AD
 #  2H 3H 4H 5H 6H 7H 8H 9H 10H JH QH KH AH
 #  2S 3S 4S 5S 6S 7S 8S 9S 10S JS QS KS AS
 #
 #  % java Knuth < cards.txt
 #  6H
 #  9C
 #  8H
 #  7C
 #  JS
 #  ...
 #  KH
 #
 #************************************************************************/

 #*
 #  The <tt>Knuth</tt> class provides a client for reading in a
 #  sequence of strings and <em>shuffling</em> them using the Knuth (or Fisher-Yates)
 #  shuffling algorithm. This algorithm guarantees to rearrange the
 #  elements in uniformly random order, under
 #  the assumption that Math.random() generates independent and
 #  uniformly distributed numbers between 0 and 1.
 #  <p>
 #  For additional documentation, see <a href="http:#algs4.cs.princeton.edu/11model">Section 1.1</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

