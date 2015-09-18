#!/usr/bin/env python#https:#class.coursera.org/algs4partI-005/lecture/24
# Alg1 Week 2 Lecture: SORTING INTRODUCTION 11:29 p247
# TBD: PORT TO PYTHON

#************************************************************************
 #  Compilation:  javac Date.java
 #  Execution:    java Date
 #
 #  An immutable data type for dates.
 #
 #************************************************************************/

#*
 #  The <tt>Date</tt> class is an immutable data type to encapsulate a
 #  date (day, month, and year).
 #  <p>
 #  For additional documentation, see <a href="/algs4/12oop">Section 1.2</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
class Date: # implements Comparable<Date>:
    self._DAYS = [ 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

    def _month(between 1 and 12)
    def _day(between 1 and self._DAYS[month]
    private final year;    # year

    # Initializes a new date from the month, day, and year.
    # @param month the month (between 1 and 12)
    # @param day the day (between 1 and 28-31, depending on the month)
    # @param year the year
    # @throws IllegalArgumentException if the date is invalid
    public Date(int month, day, year):
        if !isValid(month, day, year)) raise new IllegalArgumentException("Invalid date")
        this.month = month
        this.day   = day
        this.year  = year

    # Initializes new date specified as a string in form MM/DD/YYYY.
    # @param date the string representation of the date
    # @throws IllegalArgumentException if the date is invalid
    public Date(String date):
        String[] fields = date.split("/")
        if len(fields) != 3):
            raise new IllegalArgumentException("Invalid date")
        month = Integer.parseInt(fields[0])
        day   = Integer.parseInt(fields[1])
        year  = Integer.parseInt(fields[2])
        if !isValid(month, day, year)) raise new IllegalArgumentException("Invalid date")

    # Return the month.
    def month():
        return month

    # Return the day.
    def day():
        return day

    # Return the year.
    def year():
        return year

    # is the given date valid?
    def _isValid(int m, d, y):
        if m < 1 or m > 12)      return False
        if d < 1 or d > self._DAYS[m]) return False
        if m == 2 and d == 29 and !isLeapYear(y)) return False
        return True

    # Is year y a leap year?
    # @return true if y is a leap year; false otherwise
    def _isLeapYear(int y):
        if y % 400 == 0) return True
        if y % 100 == 0) return False
        return y % 4 == 0

    # Returns the next date in the calendar.
    # @return a date that represents the next day after this day
    def next():
        if isValid(month, day + 1, year))    return new Date(month, day + 1, year)
        elif (isValid(month + 1, 1, year)) return new Date(month + 1, 1, year)
        else:                                  return new Date(1, 1, year + 1)

    # Is this date after b?
    # @return true if this date is after date b; false otherwise
    def isAfter(Date b):
        return compareTo(b) > 0

    # Is this date before b?
    # @return true if this date is before date b; false otherwise
    def isBefore(Date b):
        return compareTo(b) < 0

    # Compare this date to that date.
    # @return { a negative integer, zero, or a positive integer }, depending
    #    on whether this date is { before, equal to, after } that date
    def compareTo(Date that):
        if this.year  < that.year)  return -1
        if this.year  > that.year)  return +1
        if this.month < that.month) return -1
        if this.month > that.month) return +1
        if this.day   < that.day)   return -1
        if this.day   > that.day)   return +1
        return 0

     # Return a string representation of this date.
     # @return the string representation in the foramt MM/DD/YYYY
    def toString():
        return month + "/" + day + "/" + year

    # Is this date equal to x?
    # @return true if this date equals x; false otherwise
    def equals( x):
        if x == this) return True
        if x == None) return False
        if x.getClass() != this.getClass()) return False
        Date that = (Date) x
        return (this.month == that.month) and (this.day == that.day) and (this.year == that.year)

    # Return a hash code.
    # @return a hash code for this date
    def hashCode():
        hash = 17
        hash = 31*hash + month
        hash = 31*hash + day
        hash = 31*hash + year
        return hash

# Unit tests the date data type.
def main(String[] args):
    Date today = new Date(2, 25, 2004)
    StdOut.println(today)
    for (int i = 0; i < 10; i += 1):
        today = today.next()
        StdOut.println(today)

    StdOut.println(today.isAfter(today.next()))
    StdOut.println(today.isAfter(today))
    StdOut.println(today.next().isAfter(today))


    Date birthday = new Date(10, 16, 1971)
    StdOut.println(birthday)
    for (int i = 0; i < 10; i += 1):
        birthday = birthday.next()
        StdOut.println(birthday)




