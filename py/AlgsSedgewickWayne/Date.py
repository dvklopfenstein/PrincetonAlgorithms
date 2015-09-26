# TBD: Finish Python port.

class Date(object):
"""an immutable data type to encapsulate a date (day, month, and year)."""
    private static final int[] DAYS =: 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 }

    def _month(between 1 and 12)
    def _day(between 1 and DAYS[month]
    private final year;    # year

   #*
     # Initializes a new date from the month, day, and year.
     # @param month the month (between 1 and 12)
     # @param day the day (between 1 and 28-31, depending on the month)
     # @param year the year
     # @throws IllegalArgumentException if this date is invalid
     #/
    public Date(int month, day, year):
        if !isValid(month, day, year)) raise new IllegalArgumentException("Invalid date")
        this.month = month
        this.day   = day
        this.year  = year

    #*
     # Initializes new date specified as a string in form MM/DD/YYYY.
     # @param date the string representation of this date
     # @throws IllegalArgumentException if this date is invalid
     #/
    public Date(String date):
        String[] fields = date.split("/")
        if len(fields) != 3):
            raise new IllegalArgumentException("Invalid date")
        month = Integer.parseInt(fields[0])
        day   = Integer.parseInt(fields[1])
        year  = Integer.parseInt(fields[2])
        if !isValid(month, day, year)) raise new IllegalArgumentException("Invalid date")

    #*
     # Return the month.
     # @return the month (an integer between 1 and 12)
     #/
    def month():
        return month

    #*
     # Returns the day.
     # @return the day (an integer between 1 and 31)
     #/
    def day():
        return day

    #*
     # Returns the year.
     # @return the year
     #/
    def year():
        return year


    # is the given date valid?
    def _isValid(int m, d, y):
        if m < 1 or m > 12)      return False
        if d < 1 or d > DAYS[m]) return False
        if m == 2 and d == 29 and !isLeapYear(y)) return False
        return True

    # is y a leap year?
    def _isLeapYear(int y):
        if y % 400 == 0) return True
        if y % 100 == 0) return False
        return y % 4 == 0

    #*
     # Returns the next date in the calendar.
     #
     # @return a date that represents the next day after this day
     #/
    def next():
        if isValid(month, day + 1, year))    return new Date(month, day + 1, year)
        elif (isValid(month + 1, 1, year)) return new Date(month + 1, 1, year)
        else:                                  return new Date(1, 1, year + 1)

    #*
     # Compares two dates chronologically.
     #
     # @param  that the other date
     # @return <tt>true</tt> if this date is after that date; <tt>false</tt> otherwise
     #/
    def isAfter(Date that):
        return compareTo(that) > 0

    #*
     # Compares two dates chronologically.
     #
     # @param  that the other date
     # @return <tt>true</tt> if this date is before that date; <tt>false</tt> otherwise
     #/
    def isBefore(Date that):
        return compareTo(that) < 0

    #*
     # Compares two dates chronologically.
     #
     # @return the value <tt>0</tt> if the argument date is equal to this date;
     #         a negative integer if this date is chronologically less than
     #         the argument date; and a positive ineger if this date is chronologically
     #         after the argument date
     #/
    @Override
    def compareTo(Date that):
        if this.year  < that.year)  return -1
        if this.year  > that.year)  return +1
        if this.month < that.month) return -1
        if this.month > that.month) return +1
        if this.day   < that.day)   return -1
        if this.day   > that.day)   return +1
        return 0

    #*
     # Returns a string representation of this date.
     #
     # @return the string representation in the format MM/DD/YYYY
     #/
    @Override
    def toString():
        return month + "/" + day + "/" + year

    #*
     # Compares this date to the specified date.
     #
     # @param  other the other date
     # @return <tt>true</tt> if this date equals <tt>other</tt>; <tt>false</tt> otherwise
     #/
    @Override
    def equals( other):
        if other == this) return True
        if other == None) return False
        if other.getClass() != this.getClass()) return False
        Date that = (Date) other
        return (this.month == that.month) and (this.day == that.day) and (this.year == that.year)

    #*
     # Returns an integer hash code for this date.
     #
     # @return a hash code for this date
     #/
    @Override
    def hashCode():
        hash = 17
        hash = 31*hash + month
        hash = 31*hash + day
        hash = 31*hash + year
        return hash

def main():
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

# Java last updated: Thu Sep 24 14:16:15 EDT 2015.
