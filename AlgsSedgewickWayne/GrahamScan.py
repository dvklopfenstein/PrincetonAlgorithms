#!/usr/bin/env python

##########################################
# Alg1, Week 2 Lecture "Convex Hull
#   https://class.coursera.org/algs4partI-005/lecture/29
##########################################

# CONVEX HULL: Application of sorting for the field of computational geometry
#
# DEFINITION: CONVEX HULL is the smallest polygon which encloses all the points for
# a set of points on a plane
#
# 00:38 EQUIVALENT DEFINITIONS:
#   * Smallest convex set contining all the points.
#   * Smallest area convex polygon enclosing the points.
#   * Convex polygon enclosing the points, whose vertices are points in set.
#
# 01:40 CONVEX HULL OUTPUT: Sequence of vertics in counterclockwise order.
# (Do not include point on the boundry which are not vertices)
#
# 02:11 CONVEX HULL: MECHANICAL ALGORITHM
# Hammer nails perpendicular to the plane; stretch elastic rubber band around points.

##########################################
# CONVEX HULL APPLICATION EXAMPLES
##########################################

# 02:30 CONVEX HULL APPLICATION: MOTION PLANNING
# ROBOT MOTION PLANNING: Find shorest path in the plane from s to t
# that avoids polygon obstacle between s and t.
# 02:48 FACT: Shortest path is either straight line from s to t or
#             is is part of one of the two polygonal chains of convex hull.

# 03:08 CONVEX HULL APPLICATION: FARTHEST PAIR PROBLEM
# Given N points in the plane, find a pair of points with the largest
# Euclidean distance between them. (They will be on the convex hull)


#-----------------------------------------
# 03:43 CONVEX HULL: GEOMETRIC PROPERTIES
# FACT: Can travers the convex hull by making only clockwise turns.
# FACT: The vertices of convex hull appear in increasing order of
#       polar angle with respect to point p with lowest y-coordinate.
# The Graham Scan algorithm uses these two facts.

# GRAHAM SCAN DEMO 05:03-07:52
# * Choose point p with smallest y-coordinate.
# * Sort points by polar angle with p.
# * Consider point in order; discard unless it creates a ccw turn.

#-----------------------------------------
# 8:00 GRAHAM SCAN: IMPLMENTATION CHALLENGES
# Q: How to find point p with SMALLEST Y-COORDINATE?
# A: Define a total order, comparing by y-coordinate. [next lecture]
#
# Q: How to SORT POINTS BY POLAR ANGLE with respect to p? 08:48
# A: Define a total order *for each* point p. [next lecture]
#    Example of wanting to be able to sort the same thing in different ways
#
# Q: How to determine whether p1->p2->p3 is a COUNTERCLOCKWISE TURN? 09:15
# A: Computational geometery. [briefly on the next two slides]
#
# Q: How to SORT EFFICIENTLY? 09:35 (Convex sorting:  Where the most work is)
# A: Mergesort sorts in N*log(N) time. [next lecture]
#
# Q: How to handle DEGENERACIES (3+ points on a line)? 10:19
# A: Requires some care, but not hard [see booksite]

#-----------------------------------------
# 10:37 IMPLEMENTING CCW
# CCW: Given 3 points a, b, and c, is a->b->c a counterclockwise turn?
#   i.e. is c to the left of the ray a->b?
#       1        2       3    4    5    6
#       c               c     c    c    b
#        \               \    |    |    |
#         b     b-c       b   b    A    c
#        /       \        |   |    |    |
#       A         A       A   A    b    A
#
#      yes       no     yes   no   no   no
#                      m=Inf  <-collinear->
# TRICKY BECAUSE:
# * Infinite slope:   3 4 5 6
# * collinear points:   4 5 6
#
# LESSON: Geometric primitives are tricky to implement.
#   * Dealing with degenerate cases.
#   * Coping with floating-point precision.
#
# 12:04 THE IDEA FOR CALCULATING IF 3 POINTS ARE CCW:
# Computing slopes between a-b and a-c and comparing the slopes to see if you
# are turning counter-clockwise or clockwise

# 12:05 IMPLEMENTING CCW
# CCW. Given three points a, b, and c, is a->b->c a counterclockwise turn?
#  * Determinant (or cross product) gives 2x signed area of planar triangle.
#
#                        | ax ay 1 |
#    2 x Area(a, b, c) = | bx by 1 | = (bx - ax)(cy - ay)(cx - ax)
#                        | cx cy 1 |
#                                          (b - a) x (c - a)
#
# * If signed area > 0, then a->b->c is counterclockwise
# * If signed area < 0, then a->b->c is clockwise
# * If signed area = 0, then a->b->c are collinear
#
#         (bx, by)               (bx, by)           (bx, by)
#            o                      o                  o
#           / \                    / \                 |
#          /<--\                  /-->\            = 0 o (cx, cy)
#         /  >0 \                /  <0 \               |
#        o-------o              o-------o              o
#   (cx, cy)   (ax, ay)    (ax, ay)   (cx, cy)      (ax, ay)
#    counterclockwise          clockwise            collinear
#
#-----------------------------------------
# 12:50 GRAHAM SCAN: IMPLEMENTATION
# SIMPLIFYING ASSUMPTIONS: No 3 points on a line; at least 3 points.
#
# Stack<Point2D> hull = new Stack<Point>();
#
# # Two different ways to sort the stack:
# Arrays.sort(p, Point2D.Y_ORDER); # p[0] is not point w/lowest y-coord
# Arrays.sort(p, p[0].BY_POLAR_ORDER); # sort by polar angle w/respect to p[0]
#
# hull.push(p[0]); # <- definitely on hull
# hull.push(p[1]);
#
# for (int i = 2; i < N; i++) {
#   Point2D top = hull.pop();
#   # Do two top points plus new point make a ccw?
#   while (Point2D.ccw(hull.peek(), top, p[i] <= 0)
#     top.hull.pop();
#   hull.push(top);
#   hull.push(p[i]); # <- add p[i] to putative hull
# }
#
# RUNNING TIME: N*log(N) for sorting and linear for rest.
# PROOF: N*log(N) for sorting; each point pushed and popped at most once.

#-----------------------------------------
# 13:44 QUESTION: What is the maximum number of vertices that can be on the convex hull
# of a set of N points:
# ANSWER: linear
# EXPLANATION: If the input points are points on the circumference of a
# circle (or a regular N-gon), then all N pointw will be on the convex hull.


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
