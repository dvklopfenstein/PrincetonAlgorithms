# TBD: amount: -0.0 check

from AlgsSedgewickWayne.Date import Date


class Transaction(object):
  """encapsulate a commercial transaction with a customer name, date, and amount."""

  def __init__(self, tr_who, when=None, amount=None):
    if when is None and amount is None:
      who, when, amount = tr_who.split()
      amount = float(amount)
    if amount == float('NaN') or amount == float('Inf'):
      raise Exception("Amount cannot be NaN or infinite")
    #if amount == 0.0) this.amount = 0.0;  # to handle -0.0
    self.who    = who        # customer (string)
    self.when   = Date(when) # date     (Date)
    self.amount = amount     # amount   (double)

  def __str__(self):
    return "{:<10} {:10} {:8.2f}".format(self.who, self.when, self.amount)

  def __lt__(self, that):
    return self.amount < that.amount

  def __gt__(self, that):
    return self.amount > that.amount

  # @return { a negative integer, zero, a positive integer}, depending
  #         on whether the amount of this transaction is { less than,
  #         equal to, or greater than } the amount of that transaction
  def compareTo(self, that):
    """Compares two transactions by amount."""
    return ((self > that) - (self < that))

  def __eq__(self, other):
    if other is self: return True
    if other is None: return False
    if type(other).__name__ != type(self).__name__: return False
    return ((self.amount == that.amount) and 
            (self.who    == that.who)    and 
            (self.when   == that.when))

  def hashCode(self):
    """Returns a hash code for this transaction."""
    hash_val = 17 # 17: nonzero constant, 31: small prime
    hash_val = 31*hash_val + hash(self.who)
    hash_val = 31*hash_val + hash(self.when)
    hash_val = 31*hash_val + hash(self.amount)
    return hash_val


# Algs 1, Week 6 Lecture: Hash Functions (18:13)
#
# QUESTION: Can we do better for search and insert than the logorithmic performance of ST(Search Trees)?
# ANSWER: Yes, with hashing. (if we don't need ordered operations)

# HASHING: BASIC PLAN
# HASH FUNCTION: Method for computing array index from key.
#           ____
#    key -> |  | -> table index
#           |__|
# ISSUES:
#   * Computing the has function.
#   * Equalit test: Method for checking whether two keys are equal.
#   * Collision resolution: Algorithm and data structure
#     to handle two keys that hash to the same array index.

# COMPUTING THE HAS FUNCTION
# IDEALISTIC GOAL: Scramble the keys uniformly to produce a table index.
#   * Efficiently computable.
#   * Each table index equally likely for each key.
#     This is a thouroughly researched problem, still problematic in practical applications

# JAVA'S HASH CODE CONVENTIONS
# All Java classes inherit a method, hashCode(), which returns a 32-bit int.
# 
# REQUIREMENT: if x.equals(y), then (x.hashCode() == y.hashCode())
# HIGHLY DESIREABLE: If !x.equals(y), then (x.hashCode() != y.hashCode())
# DEFAULT IMPLEMENTATION: Memory address of x.
# 
# Python example:
#   >>> a = 0
#   >>> b = 0.0
#   >>> print a == b
#   True
#   >>> print hash(a) == hash(b)
#   True
#   >>> print hash(a)
#   0
#   >>> print hash(b)
#   0

# HASH CODE DESIGN  @ 12:22
# "STANDARD" RECIPE FOR USER-DEFINED TYPES.
#   * Combine each significant field using the 31x + y rule.
#   * If field is a primative type, use wrapper type: hashCode()
#   * If field is null, return 0.
#   * If field is a reference type, use Java's hashCode(). (applies rule recursively)
#   * If field is an array, apply to each entry. <- or use Arrays.deepHashCode()

# MODULAR HASHING
#   HASH CODE: An int between -2^31 and 2^31-1
#   HASH FUNCTION: An int between 0 andd M-1 (for use as array index).
#
# Correct: (1-in-a-billion bug: -2^31
#   private int hash(Key key) { reutrn (key.hashCode() & 0x7fffffff)%M; }
#
# If M is prime, increased liklihood of having equal likelhood ...

# UNIFORM HASHING ASSUMPTION: 16:40
#
# BIRTHDAY PROBLEM: Expect two balls in the same bin after ~sqrt(pi*M/2) tosses
# COUPON COLLECTOR: Expect every bin has >= 1 ball after ~M ln M tosses.
# LOAD BALANCING: After M tosses, expect most laoded bin has theta(log M/log log M) balls.








# Java last updated: Thu Sep 24 14:16:15 EDT 2015.
