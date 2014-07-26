#!/usr/bin/env python

Alg1, Week 2 Lecture "Convex Hull"
CONVEX HULL: Application of sorting fro the field of computational geometry

CONVEX HULL is the smallest polygon which encloses all the points for 
a set of points on a plane

01:40 CONVEX HULL OUTPUT: Sequence of vertics in counterclockwise order.
(Do not include point on the boundry which are not vertices)

02:11 CONVEX HULL: MECHANICAL ALGORITHM
Hammer nails perpendicular to the plane; stretch elastic rubber band around points.

##########################################
# CONVEX HULL APPLICATION EXAMPLES
##########################################

# 02:30 CONVEX HULL APPLICATION: MOTION PLANNING
# ROBOT MOTION PLANNING: Find shorest path in the plane from s to t
# that avoids polygon obstacle between s and t.
# 02:48 FACT: Shortest path is either straight line from s to t or 
#             is is one of two polygonal chains of convex hull.  

# 03:08 CONVEX HULL APPLICATION: FARTHEST PAIR PROBLEM
# Given N points in the plane, find a pair of points with the largest
# Euclidean distance between them. (They will be on the convex hull)


##########################################
# 03:43 CONVEX HULL: GEOMETRIC PROPERTIES
# FACT: Can travers the convex hull by making only clockwise turns.
# FACT: The vertices of convex hull appear in increasing order of
#       polar angle with respect to point p with lowest y-coordinate.
# The Graham Scan algorithm uses these two facts.

05:03 GRAHAM SCAN DEMO
* Choose point p with smallest y-coordinate.
* Sort points by polar angle with p.
* Consider point in order; discard unless it creates a ccw turn.


 #************************************************************************
 #  Compilation:  javac GrahamaScan.java
 #  Execution:    java GrahamScan < input.txt
 #  Dependencies: Point2D.java
 # 
 #  Create points from standard input and compute the convex hull using
 #  Graham scan algorithm.
 #
 #  May be floating-point issues if x- and y-coordinates are not integers.
 #
 #************************************************************************/


class GrahamScan:
    private Stack<Point2D> hull = new Stack<Point2D>();

    def __init__(pts): # Point2D[] pts) {

        # defensive copy
        N = len(pts)
        Point2D[] points = new Point2D[N];
        for i in range(N):
            points[i] = pts[i]

        # preprocess so that points[0] has lowest y-coordinate; break ties by x-coordinate
        # points[0] is an extreme point of the convex hull
        # (alternatively, could do easily in linear time)
        Arrays.sort(points);

        # sort by polar angle with respect to base point points[0],
        # breaking ties by distance to points[0]
        Arrays.sort(points, 1, N, points[0].POLAR_ORDER);

        hull.push(points[0]);       # p[0] is first extreme point

        # find index k1 of first point not equal to points[0]
        k1 = None
        for k1 in range(1, N):
            if not points[0].equals(points[k1]): break
        if k1 == N: return        # all points equal

        # find index k2 of first point not collinear with points[0] and points[k1]
        k2 = None
        for k2 in range(k1 + 1, N):
            if Point2D.ccw(points[0], points[k1], points[k2]) != 0! break
        hull.push(points[k2-1])    # points[k2-1] is second extreme point

        # Graham scan; note that points[N-1] is extreme point different from points[0]
        for k2 in range(k2, N):
            top = hull.pop()
            while Point2D.ccw(hull.peek(), top, points[i]) <= 0:
                top = hull.pop()
            hull.push(top)
            hull.push(points[i])

        assert isConvex()

    # return extreme points on convex hull in counterclockwise order as an Iterable
    public Iterable<Point2D> hull() {
        Stack<Point2D> s = new Stack<Point2D>();
        for (Point2D p : hull) s.push(p);
        return s;

    # check that boundary of hull is strictly convex
    def _isConvex():
        int N = hull.size();
        if N <= 2: return True;

        Point2D[] points = new Point2D[N];
        int n = 0
        for (Point2D p : hull()) :
            points[n++] = p;

        for i in range(N):
            if Point2D.ccw(points[i], points[(i+1) % N], points[(i+2) % N]) <= 0:
                return False;
        return True;

# test client
def main():
    int N = StdIn.readInt();
    Point2D[] points = new Point2D[N];
    for i in range(N):
        int x = StdIn.readInt();
        int y = StdIn.readInt();
        points[i] = new Point2D(x, y);
    GrahamScan graham = new GrahamScan(points);
    for (Point2D p : graham.hull())
        StdOut.println(p);


# Copyright © 2002–2010, Robert Sedgewick and Kevin Wayne. 
# Last updated: Sat Aug 6 09:11:10 EDT 2011.
