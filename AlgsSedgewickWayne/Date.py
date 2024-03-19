"""An example of an immutable type which can be used as a key for a Symbol Table."""

from datetime import date, timedelta
import re

class Date:
    """an immutable data type to encapsulate a date (day, month, and year)."""

    def __init__(self, str_month, day=None, year=None):
        """Initializes new date specified as a string in form MM/DD/YYYY."""
        if day is None and year is None:
            self.date = self._init_w_str(str_month)
        else:
            self.date = self._init_w_ints(year, str_month, day)

    def month(self):
        """Return month integer"""
        return self.date.month

    def day(self):
        """Return day integer"""
        return self.date.day

    def year(self):
        """Return year integer"""
        return self.date.year

    @staticmethod
    def is_leap_year(year):
        """is year a leap year?"""
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return year % 4 == 0

    def next(self):
        """return a date that represents the next day after this day"""
        nxt = self.date + timedelta(days=1)
        return Date(nxt.month, nxt.day, nxt.year)

    def __gt__(self, that):
        """return True if this date is after that date; False otherwise."""
        return self.date > that.date

    def __ge__(self, that):
        """return True if this date is the same or after that date; False otherwise."""
        return self.date >= that.date

    def __lt__(self, that):
        """return True if this date is before that date; False otherwise."""
        return self.date < that.date

    def __le__(self, that):
        """return True if this date is the same or before that date; False otherwise."""
        return self.date <= that.date

    def __str__(self):
        """Returns a string representation of this date."""
        return "{self.month()}/{self.day()}/{self.year()}"

    def __eq__(self, other):
        """return True if this date equals other; False otherwise."""
        if other is self:
            return True
        if other is None:
            return False
        if type(other).__name__ != type(self).__name__:
            return False
        return self.date == other.date

    #d  ef hashCode():
    #    """Returns an integer hash code for this date."""
    #    hash = 17
    #    hash = 31*hash + month
    #    hash = 31*hash + day
    #    hash = 31*hash + year
    #    return hash

    @staticmethod
    def java_string_hashcode(txt):
        """Returns same result as java'txt String.hashCode()"""
        # From: https://gist.github.com/hanleybrand/5224673#file-java_string_hashcode-py
        hashcode = 0
        for letter in txt:
            hashcode = (31 * hashcode + ord(letter)) & 0xFFFFFFFF
        return ((hashcode + 0x80000000) & 0xFFFFFFFF) - 0x80000000

    def _init_w_str(self, date_str):
        """Get date from the string representation of this date."""
        mtch = re.match(r'(\d{1,2})/(\d{1,2})/(\d{4})', date_str) # MM/DD/YYYY
        if mtch:
            return date(int(mtch.group(3)), int(mtch.group(1)), int(mtch.group(2)))
        raise RuntimeError("Invalid date. Expected MM/DD/YYYY")

    def _init_w_ints(self, year, month, day):
        """Init date object from int values."""
        try:
            return date(year, month, day)
        except Exception as exc:
            # pylint: disable=line-too-long
            raise RuntimeError(f"COULD NOT CREATE date(year={year}, month={month}, day={day})") from exc

# Java last updated: Thu Sep 24 14:16:15 EDT 2015.
