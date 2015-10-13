#!/usr/bin/env python#*****************************************************************************
 #  Compilation:  javac SET.java
 #  Execution:    java SET
 #  Dependencies: StdOut.java
 #  
 #  Set implementation using Java's TreeSet library.
 #  Does not allow duplicates.
 #
 #  % java SET
 #  128.112.136.11
 #  208.216.181.15
 #  null
 #
 #*****************************************************************************/

package edu.princeton.cs.algs4

import java.util.Iterator
import java.util.NoSuchElementException
import java.util.TreeSet

#*
 #  The <tt>SET</tt> class represents an ordered set of comparable keys.
 #  It supports the usual <em>add</em>, <em>contains</em>, and <em>delete</em>
 #  methods. It also provides ordered methods for finding the <em>minimum</em>,
 #  <em>maximum</em>, <em>floor</em>, and <em>ceiling</em> and set methods
 #  for <em>union</em>, <em>intersection</em>, and <em>equality</em>.
 #  <p>
 #  Even though this implementation include the method <tt>equals()</tt>, it
 #  does not support the method <tt>hashCode()</tt> because sets are mutable.
 #  <p>
 #  This implementation uses a balanced binary search tree. It requires that
 #  the key type implements the <tt>Comparable</tt> interface and calls the
 #  <tt>compareTo()</tt> and method to compare two keys. It does not call either
 #  <tt>equals()</tt> or <tt>hashCode()</tt>.
 #  The <em>add</em>, <em>contains</em>, <em>delete</em>, <em>minimum</em>,
 #  <em>maximum</em>, <em>ceiling</em>, and <em>floor</em> methods take
 #  logarithmic time in the worst case.
 #  The <em>size</em>, and <em>is-empty</em> operations take constant time.
 #  Construction takes constant time.
 #  <p>
 #  This implementation uses a balanced binary search tree. It requires that
 #  For additional documentation, see
 #  <a href="http://algs4.cs.princeton.edu/35applications">Section 3.5</a> of
 #  <i>Algorithms in Java, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #
 #  @param <Key> the generic type of a key in this set
 #/

public class SET< extends Comparable<>> implements Iterable<>:
    private TreeSet<> set

    #*
     # Initializes an empty set.
     #/
    public SET():
        set = new TreeSet<>()

    #*
     # Adds the key to this set (if it is not already present).
     #
     # @param  key the key to add
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def add( key):
        if key is None) raise new NullPointerException("called add() with a None key")
        set.add(key)


    #*
     # Returns true if this set contains the given key.
     #
     # @param  key the key
     # @return <tt>true</tt> if this set contains <tt>key</tt> and
     #         <tt>false</tt> otherwise
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def contains( key):
        if key is None) raise new NullPointerException("called contains() with a None key")
        return set.contains(key)

    #*
     # Removes the key from this set (if the key is present).
     #
     # @param  key the key
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def delete( key):
        if key is None) raise new NullPointerException("called delete() with a None key")
        set.remove(key)

    #*
     # Returns the number of keys in this set.
     #
     # @return the number of keys in this set
     #/
    def size():
        return set.size()

    #*
     # Returns true if this set is empty.
     #
     # @return <tt>true</tt> if this set is empty, and <tt>false</tt> otherwise
     #/
    def isEmpty():
        return size() == 0
 
    #*
     # Returns all of the keys in this set, as an iterator.
     # To iterate over all of the keys in a set named <tt>set</tt>, use the
     # foreach notation: <tt>for (Key key : set)</tt>.
     #
     # @return an iterator to all of the keys in this set
     #/
    def iterator():
        return set.iterator()

    #*
     # Returns the largest key in this set.
     #
     # @return the largest key in this set
     # @throws NoSuchElementException if this set is empty
     #/
    public  max():
        if isEmpty()) raise new NoSuchElementException("called max() with empty set")
        return set.last()

    #*
     # Returns the smallest key in this set.
     #
     # @return the smallest key in this set
     # @throws NoSuchElementException if this set is empty
     #/
    public  min():
        if isEmpty()) raise new NoSuchElementException("called min() with empty set")
        return set.first()


    #*
     # Returns the smallest key in this set greater than or equal to <tt>key</tt>.
     #
     # @param  key the key
     # @return the smallest key in this set greater than or equal to <tt>key</tt>
     # @throws NoSuchElementException if there is no such key
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    public  ceiling( key):
        if key is None) raise new NullPointerException("called ceiling() with a None key")
         k = set.ceiling(key)
        if k is None) raise new NoSuchElementException("all keys are less than " + key)
        return k

    #*
     # Returns the largest key in this set less than or equal to <tt>key</tt>.
     #
     # @param  key the key
     # @return the largest key in this set table less than or equal to <tt>key</tt>
     # @throws NoSuchElementException if there is no such key
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    public  floor( key):
        if key is None) raise new NullPointerException("called floor() with a None key")
         k = set.floor(key)
        if k is None) raise new NoSuchElementException("all keys are greater than " + key)
        return k

    #*
     # Returns the union of this set and that set.
     #
     # @param  that the other set
     # @return the union of this set and that set
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
     # Returns the intersection of this set and that set.
     #
     # @param  that the other set
     # @return the intersection of this set and that set
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
     # Compares this set to the specified set.
     # <p>
     # Note that this method declares two empty sets to be equal
     # even if they are parameterized by different generic types.
     # This is consistent with the behavior of <tt>equals()</tt> 
     # within Java's Collections framework.
     #       
     # @param  other the other set
     # @return <tt>true</tt> if this set equals <tt>other</tt>;
     #         <tt>false</tt> otherwise
     #/
    @Override
    def equals( other):
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
    def hashCode():
        raise new UnsupportedOperationException("hashCode() is not supported because sets are mutable")

    #*
     # Returns a string representation of this set.
     #
     # @return a string representation of this set, with the keys separated
     #         by single spaces
     #/
    @Override
    def toString():
        StringBuilder s = new StringBuilder()
        for ( key : this)
            s.append(key + " ")
        return s.toString()

    #*
     # Unit tests the <tt>SET</tt> data type.
     #/
    def main(String[] args):
        SET<String> set = new SET<String>()


        # insert some keys
        set.add("www.cs.princeton.edu")
        set.add("www.cs.princeton.edu");    # overwrite old value
        set.add("www.princeton.edu")
        set.add("www.math.princeton.edu")
        set.add("www.yale.edu")
        set.add("www.amazon.com")
        set.add("www.simpsons.com")
        set.add("www.stanford.edu")
        set.add("www.google.com")
        set.add("www.ibm.com")
        set.add("www.apple.com")
        set.add("www.slashdot.com")
        set.add("www.whitehouse.gov")
        set.add("www.espn.com")
        set.add("www.snopes.com")
        set.add("www.movies.com")
        set.add("www.cnn.com")
        set.add("www.iitb.ac.in")


        prt.write(set.contains("www.cs.princeton.edu"))
        prt.write(!set.contains("www.harvardsucks.com"))
        prt.write(set.contains("www.simpsons.com"))
        prt.write()

        prt.write("ceiling(www.simpsonr.com) = " + set.ceiling("www.simpsonr.com"))
        prt.write("ceiling(www.simpsons.com) = " + set.ceiling("www.simpsons.com"))
        prt.write("ceiling(www.simpsont.com) = " + set.ceiling("www.simpsont.com"))
        prt.write("floor(www.simpsonr.com)   = " + set.floor("www.simpsonr.com"))
        prt.write("floor(www.simpsons.com)   = " + set.floor("www.simpsons.com"))
        prt.write("floor(www.simpsont.com)   = " + set.floor("www.simpsont.com"))
        prt.write()


        # print out all keys in this set in lexicographic order
        for (String s : set):
            prt.write(s)



#*****************************************************************************
 #  Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
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
