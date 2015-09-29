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

  #def hashCode():
  #  """Returns a hash code for this transaction."""
  #  hash = 17
  #  hash = 31*hash + who.hashCode()
  #  hash = 31*hash + when.hashCode()
  #  hash = 31*hash + ((Double) amount).hashCode()
  #  return hash


# Java last updated: Thu Sep 24 14:16:15 EDT 2015.
