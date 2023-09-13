"""Ordered self._treeset of keys implmented with a Balanced Binary Search Tree."""

# import java.util.Iterator
# import java.util.NoSuchElementException
# import java.util.TreeSet

class SET(object):

  def __init__(self):
    self._treeset = TreeSet()

  def add(self, key):
    """Adds the key to this treeset (if it is not already present)."""
     if key is None: raise new NullPointerException("called add() with a None key")
     self._treeset.add(key)

  def contains(self, key):
    """Returns true if this treeset contains the given key."""
    if key is None: raise new NullPointerException("called contains() with a None key")
    return self._treeset.contains(key)

  def delete(self, key):
    """Removes the key from this treeset (if the key is present)."""
    if key is None: raise new NullPointerException("called delete() with a None key")
    self._treeset.remove(key)

  def size(self): return self._treeset.size()
  def isEmpty(self): return size() == 0

  def iterator(self):
    """Returns all of the keys in this treeset, as an iterator."""
    return self._treeset.iterator()

  def max(self):
    """Returns the largest key in this treeset."""
    if isEmpty()) raise new NoSuchElementException("called max() with empty self._treeset")
    return self._treeset.last()

  def min(self):
    """Returns the smallest key in this treeset."""
    if isEmpty()) raise new NoSuchElementException("called min() with empty self._treeset")
    return self._treeset.first()

  #*
   #
   # @param  key the key
   # @return the smallest key in this self._treeset greater than or equal to <tt>key</tt>
   # @throws NoSuchElementException if there is no such key
   # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
   #/
  public  ceiling( key):
    """Returns the smallest key in this treeset greater than or equal to key."""
      if key is None) raise new NullPointerException("called ceiling() with a None key")
       k = self._treeset.ceiling(key)
      if k is None) raise new NoSuchElementException("all keys are less than " + key)
      return k

  #*
   # Returns the largest key in this self._treeset less than or equal to <tt>key</tt>.
   #
   # @param  key the key
   # @return the largest key in this self._treeset table less than or equal to <tt>key</tt>
   # @throws NoSuchElementException if there is no such key
   # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
   #/
  public  floor( key):
      if key is None) raise new NullPointerException("called floor() with a None key")
       k = self._treeset.floor(key)
      if k is None) raise new NoSuchElementException("all keys are greater than " + key)
      return k

  #*
   # Returns the union of this self._treeset and that self._treeset.
   #
   # @param  that the other self._treeset
   # @return the union of this self._treeset and that self._treeset
   # @throws NullPointerException if <tt>that</tt> is <tt>null</tt>
   #/
  def union(SET<> that):
      if that is None) raise new NullPointerException("called union() with a None argument")
      SET<> c = new SET<>()
      for ( x : this):
          c.add(x)
      for ( x : that):
          c.add(x)
      return c

  #*
   # Returns the intersection of this self._treeset and that self._treeset.
   #
   # @param  that the other self._treeset
   # @return the intersection of this self._treeset and that self._treeset
   # @throws NullPointerException if <tt>that</tt> is <tt>null</tt>
   #/
  def intersects(SET<> that):
      if that is None) raise new NullPointerException("called intersects() with a None argument")
      SET<> c = new SET<>()
      if this.size() < that.size()):
          for ( x : this):
              if that.contains(x)) c.add(x)
      else:
          for ( x : that):
              if this.contains(x)) c.add(x)
      return c

  #*       
   # Compares this self._treeset to the specified self._treeset.
   # <p>
   # Note that this method declares two empty sets to be equal
   # even if they are parameterized by different generic types.
   # This is consistent with the behavior of <tt>equals()</tt> 
   # within Java's Collections framework.
   #       
   # @param  other the other self._treeset
   # @return <tt>true</tt> if this self._treeset equals <tt>other</tt>;
   #         <tt>false</tt> otherwise
   #/
  @Override
  def equals(self, other):
      if other == this) return True
      if other is None) return False
      if other.getClass() != this.getClass()) return False
      SET<> that = (SET<>) other
      if this.size() != that.size()) return False
      try:
          for ( k : this)
              if !that.contains(k)) return False
      catch (ClassCastException exception):
          return False
      return True

  #*
   # This operation is not supported because sets are mutable.
   #
   # @return does not return a value
   # @throws UnsupportedOperationException if called
   #/
  @Override
  def hashCode(self):
      raise new UnsupportedOperationException("hashCode() is not supported because sets are mutable")

  #*
   # Returns a string representation of this self._treeset.
   #
   # @return a string representation of this self._treeset, with the keys separated
   #         by single spaces
   #/
  @Override
  def toString(self):
      StringBuilder s = new StringBuilder()
      for ( key : this)
          s.append(key + " ")
      return s.toString()

  #*
   # Unit tests the <tt>SET</tt> data type.
   #/
  def main(String[] args):
      SET<String> self._treeset = new SET<String>()


      # insert some keys
      self._treeset.add("www.cs.princeton.edu")
      self._treeset.add("www.cs.princeton.edu");    # overwrite old value
      self._treeset.add("www.princeton.edu")
      self._treeset.add("www.math.princeton.edu")
      self._treeset.add("www.yale.edu")
      self._treeset.add("www.amazon.com")
      self._treeset.add("www.simpsons.com")
      self._treeset.add("www.stanford.edu")
      self._treeset.add("www.google.com")
      self._treeset.add("www.ibm.com")
      self._treeset.add("www.apple.com")
      self._treeset.add("www.slashdot.com")
      self._treeset.add("www.whitehouse.gov")
      self._treeset.add("www.espn.com")
      self._treeset.add("www.snopes.com")
      self._treeset.add("www.movies.com")
      self._treeset.add("www.cnn.com")
      self._treeset.add("www.iitb.ac.in")


      prt.write(self._treeset.contains("www.cs.princeton.edu"))
      prt.write(!self._treeset.contains("www.harvardsucks.com"))
      prt.write(self._treeset.contains("www.simpsons.com"))
      prt.write()

      prt.write("ceiling(www.simpsonr.com) = " + self._treeset.ceiling("www.simpsonr.com"))
      prt.write("ceiling(www.simpsons.com) = " + self._treeset.ceiling("www.simpsons.com"))
      prt.write("ceiling(www.simpsont.com) = " + self._treeset.ceiling("www.simpsont.com"))
      prt.write("floor(www.simpsonr.com)   = " + self._treeset.floor("www.simpsonr.com"))
      prt.write("floor(www.simpsons.com)   = " + self._treeset.floor("www.simpsons.com"))
      prt.write("floor(www.simpsont.com)   = " + self._treeset.floor("www.simpsont.com"))
      prt.write()


      # print out all keys in this self._treeset in lexicographic order
      for (String s : self._treeset):
          prt.write(s)



#*****************************************************************************
 #  Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
 #
 #  This file is part of algs4.jar, which accompanies the textbook
 #
 #      Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne,
 #      Addison-Wesley Professional, 2011, ISBN 0-321-57351-X.
 #      http://algs4.cs.princeton.edu
 #
 #
 #  algs4.jar is free software: you can redistribute it and/or modify
 #  it under the terms of the GNU General Public License as published by
 #  the Free Software Foundation, either version 3 of the License, or
 #  (at your option) any later version.
 #
 #  algs4.jar is distributed in the hope that it will be useful,
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with algs4.jar.  If not, see http://www.gnu.org/licenses.
 #*****************************************************************************/
