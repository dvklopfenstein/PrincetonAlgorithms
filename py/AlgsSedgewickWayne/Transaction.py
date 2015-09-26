# TBD: when:   Finish date object
# TBD: amount: -0.0 check and Nan and Inf check

from datetime import date

class Transaction(object):
  """encapsulate a commercial transaction with a customer name, date, and amount."""

  def __init__(self, tr_who, when=None, amount=None):
    if when is None and amount is None:
      who, when, amount = tr_who.split()
      amount = float(amount)
    #if Double.isNaN(amount) or Double.isInfinite(amount))
    #  raise new IllegalArgumentException("Amount cannot be NaN or infinite")
    self.who    = who    # customer (string)
    self.when   = when   # date     (Date)
    self.amount = amount # amount   (double)

    #public Transaction(String who, Date when, double amount):
    #    if Double.isNaN(amount) or Double.isInfinite(amount))
    #        raise new IllegalArgumentException("Amount cannot be NaN or infinite")
    #    this.who    = who
    #    this.when   = when
    #    if amount == 0.0) this.amount = 0.0;  # to handle -0.0
    #    else               this.amount = amount

    #public Transaction(String transaction):
    #    String[] a = transaction.split("\\s+")
    #    who    = a[0]
    #    when   = new Date(a[1])
    #    double value = Double.parseDouble(a[2])
    #    if value == 0.0) amount = 0.0;  # convert -0.0 0.0
    #    else              amount = value
    #    if Double.isNaN(amount) or Double.isInfinite(amount))
    #        raise new IllegalArgumentException("Amount cannot be NaN or infinite")

  def __str__(self):
    return "{:<10} {:10} {:8.2f}".format(self.who, self.when, self.amount)

  def __lt__(self, that):
    return this.amount < that.amount

  def __gt__(self, that):
    return this.amount > that.amount

  # @return { a negative integer, zero, a positive integer}, depending
  #         on whether the amount of this transaction is { less than,
  #         equal to, or greater than } the amount of that transaction
  def compareTo(self, that):
    """Compares two transactions by amount."""
    return ((self > that) - (self < that))

  def __eq__(self, other):
    if other is self: return True
    if other is None: return False
    if type(other).__name__ != type(this).__name__: return False
    return ((this.amount == that.amount) and 
            (this.who    == that.who)    and 
            (this.when   == that.when))

  #def hashCode():
  #  """Returns a hash code for this transaction."""
  #  hash = 17
  #  hash = 31*hash + who.hashCode()
  #  hash = 31*hash + when.hashCode()
  #  hash = 31*hash + ((Double) amount).hashCode()
  #  return hash


# Java last updated: Thu Sep 24 14:16:15 EDT 2015.
