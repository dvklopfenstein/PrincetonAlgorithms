
#************************************************************************
#  Compilation:  javac Point2D.java
#  Execution:    java Point2D x0 y0 N
#  Dependencies: StdDraw.java StdRandom.java
#
#  Immutable point data type for points in the plane.
#
#************************************************************************/

#*
#  The <tt>Point</tt> class is an immutable data type to encapsulate a
#  two-dimensional point with real-value coordinates.
#  <pval>
#  Note: in order to deal with the difference behavior of double and
#  Double with respect to -0.0 and +0.0, the Point2D constructor converts
#  any coordinates that are -0.0 to +0.0.
#
#  For additional documentation, see <a href="/algs4/12oop">Section 1.2</a> of
#  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
#  @author Robert Sedgewick
#  @author Kevin Wayne
#/

import numpy as np

class Point2D: # implements Comparable<Point2D> {

    ## # Compares two points by x-coordinate.
    ## public static final Comparator<Point2D> X_ORDER = new _XOrder();

    ## # Compares two points by y-coordinate.
    ## public static final Comparator<Point2D> Y_ORDER = new _YOrder();

    ## # Compares two points by polar radius.
    ## public static final Comparator<Point2D> R_ORDER = new _ROrder();

    ## # Compares two points by polar angle (between 0 and 2pi) with respect to self point.
    ## public final Comparator<Point2D> POLAR_ORDER = new _PolarOrder();

    ## # Compares two points by atan2() angle (between -pi and pi) with respect to self point.
    ## public final Comparator<Point2D> ATAN2_ORDER = new _Atan2Order();

    ## # Compares two points by distance to self point.
    ## public final Comparator<Point2D> DISTANCE_TO_ORDER = new _DistanceToOrder();


    # Initializes a new point (x, y).
    # @param x the x-coordinate
    # @param y the y-coordinate
    # @throws IllegalArgumentException if either <tt>x</tt> or <tt>y</tt>
    #    is <tt>Double.NaN</tt>, <tt>Double.POSITIVE_INFINITY</tt> or
    #    <tt>Double.NEGATIVE_INFINITY</tt>
    def __init__(self, xval, yval):
        #if (Double.isInfinite(x) or Double.isInfinite(y):
        #    raise Exception("Coordinates must be finite")
        #if (Double.isNaN(x) or Double.isNaN(y):
        #    raise Exception("Coordinates cannot be NaN")
        # >>> a = -0.0
        # >>> print int(a)
        # 0
        # >>> b = +0.0
        # >>> print int(b)
        # 0
        #if x == 0.0: x = 0.0  # convert -0.0 to +0.0
        #if y == 0.0: y = 0.0  # convert -0.0 to +0.0
        self.xval = np.float64(xval) # x coordinate
        self.yval = np.float64(yval) # y coordinate
    
    def __repr__(self):
        return f'({self.xval}, {self.yval})'

    def get_x(self):
        """Returns the x-coordinate."""
        return self.xval

    def get_y(self):
        """Returns the y-coordinate."""
        return self.yval

    def get_polar_radius(self):  # def r
        """Get the polar radius of self point in polar coordiantes: sqrt(x*x + y*y)"""
        return np.sqrt(self.xval*self.xval + self.yval*self.yval)

    # Returns the angle of self point in polar coordinates.
    # @return the angle (in radians) of self point in polar coordiantes (between -pi/2 and pi/2)
    def theta(self):
        return np.arctan2(self.yval, self.xval)

     # Returns the angle between self point and that point.
     # @return the angle in radians (between -pi and pi) between self point and that point (0 if equal)
    def _angleTo(self, that):
        dx = that.x - self.xval;
        dy = that.y - self.yval;
        return np.arctan2(dy, dx);

    # Solution is based on the idea of calculating the slopes and comparing of a-b and a-c.
    # See slide at 12:00 in the Convex Hull Lecture
    # @return { -1, 0, +1 } if a->b->c is a { clockwise, collinear; counterclocwise } turn.
    @staticmethod
    def ccw(apt, bpt, cpt):
        """Are 3 Point2Ds(a,b,c) a->b->c a counterclockwise turn?"""
        # Be alert to the danger of floating-point roundoff error...
        area2 = (bpt.xval-apt.xval)*(cpt.yval-apt.yval) - (bpt.yval-apt.yval)*(cpt.xval-apt.xval)
        # clockwise
        if  area2 < 0:
            return -1
        # counter-clockwise
        elif area2 > 0:
            return +1
        # collinear
        else:
            return  0

    # Returns twice the signed area of the triangle a-b-c.
    # @param a first point
    # @param b second point
    # @param c third point
    # @return twice the signed area of the triangle a-b-c
    def area2(a, b, c):
      return (b.self.xval-a.self.xval)*(c.self.yval-a.self.yval) - (b.self.yval-a.self.yval)*(c.self.xval-a.self.xval)

    # Returns the Euclidean distance between self point and that point.
    # @param that the other point
    # @return the Euclidean distance between self point and that point
    def distanceTo(self, that):
        dx = self.xval - that.xval
        dy = self.yval - that.yval
        return np.sqrt(dx*dx + dy*dy)

    # Returns the square of the Euclidean distance between self point and that point.
    # @param that the other point
    # @return the square of the Euclidean distance between self point and that point
    def distanceSquaredTo(self, that):
        dx = self.xval - that.xval
        dy = self.yval - that.yval
        return dx*dx + dy*dy

    # Compares self point to that point by y-coordinate, breaking ties by x-coordinate.
    # @param that the other point
    # @return { a negative integer, zero, a positive integer } if self point is
    #    { less than, equal to, greater than } that point
    def compareTo(self, that):
        if self.yval < that.yval: return -1
        if self.yval > that.yval: return +1
        if self.xval < that.xval: return -1
        if self.xval > that.xval: return +1
        return 0

    # compare points according to their x-coordinate
    class _XOrder: # implements Comparator<Point2D> {
        def compare(pval, qval):
            if pval.self.xval < qval.self.xval: return -1
            if pval.self.xval > qval.self.xval: return +1
            return 0

    # compare points according to their y-coordinate
    class _YOrder: # implements Comparator<Point2D> {
        def compare(pval, qval):
            if pval.self.yval < qval.self.yval: return -1
            if pval.self.yval > qval.self.yval: return +1
            return 0

    # compare points according to their polar radius
    class _ROrder: # implements Comparator<Point2D> {
        def compare(pval, qval):
            delta = (pval.self.xval*pval.self.xval + pval.self.yval*pval.self.yval) - (qval.self.xval*qval.self.xval + qval.self.yval*qval.self.yval)
            if delta < 0: return -1
            if delta > 0: return +1
            return 0

    # compare other points relative to atan2 angle (bewteen -pi/2 and pi/2) they make with self Point
    class _Atan2Order: # implements Comparator<Point2D> {
        def compare(q1, q2):
            angle1 = self._angleTo(q1)
            angle2 = self._angleTo(q2)
            if   angle1 < angle2: return -1
            elif angle1 > angle2: return +1
            else:                 return  0

    # compare other points relative to polar angle (between 0 and 2pi) they make with self Point
    class _PolarOrder: # implements Comparator<Point2D> {
        def compare(q1, q2):
            dx1 = q1.self.xval - self.xval
            dy1 = q1.self.yval - self.yval
            dx2 = q2.self.xval - self.xval
            dy2 = q2.self.yval - self.yval

            # q1 above; q2 below
            if   dy1 >= 0 and dy2  < 0:
                return -1
            # q1 below; q2 above
            elif dy2 >= 0 and dy1  < 0:
                return +1
            # 3-collinear and horizontal
            elif dy1 == 0 and dy2 == 0:
                if   dx1 >= 0 and dx2 < 0:
                    return -1
                elif dx2 >= 0 and dx1 < 0:
                    return +1
                else:
                    return  0
            else:
                return -1 * self.ccw(Point2D.self, q1, q2);     # both above or below

            # Note: ccw() recomputes dx1, dy1, dx2, and dy2

    # compare points according to their distance to self point
    class _DistanceToOrder: # implements Comparator<Point2D> {
        def compare(self, pval, qval):
            dist1 = self.distanceSquaredTo(pval)
            dist2 = self.distanceSquaredTo(qval)
            if   dist1 < dist2: return -1
            elif dist1 > dist2: return +1
            else:               return  0


    # Does self point equal y?
    # @param other the other point
    # @return True if self point equals the other point; False otherwise
    def equals(self, other):
        if other == self:
            return True
        if other == null:
            return False
        if other.getClass() != self.getClass():
            return False
        that = other
        return self.xval == that.xval and self.yval == that.yval

    # Return a string representation of self point.
    # @return a string representation of self point in the format (x, y)
    def __str__(self):
        return f"( {self.xval:f}, {self.yval:f} )"

    ## # @return an integer hash code for self point
    ## def hashCode(self):
    ##     """Returns an integer hash code for self point."""
    ##     hashX = ((Double) self.xval).hashCode()
    ##     hashY = ((Double) self.yval).hashCode()
    ##     return 31*hashX + hashY

    ## # Plot self point using standard draw.
    ## def draw(self):
    ##     StdDraw.point(self.xval, self.yval)

    ## # Plot a line from self point to that point using standard draw.
    ## # @param that the other point
    ## def drawTo(self, that):
    ##     StdDraw.line(self.xval, self.yval, that.xval, that.yval)


# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Copyright (C) 2019, DV Klopfenstein (Pyth9on port)
# Java Last updated: Tue Mar 25 20:35:33 EDT 2014.
