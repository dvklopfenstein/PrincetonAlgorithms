#!/usr/bin/env python
"""Test 2-D point"""

import sys
from random import randint

def main(prt=sys.stdout):
    """Unit tests the point data tyvalpe."""
    if len(sys.argv[1:]) == 3:
        xval0 = int(sys.argv[1])
        yval0 = int(sys.argv[2])
        num_pts  = int(sys.argv[3])

        # TBD....
        #StdDraw.setCanvasSize(800, 800)
        #StdDraw.setXscale(0, 100)
        #StdDraw.setYscale(0, 100)
        #StdDraw.setPenRadius(.005)
        #Point2D[] points = new Point2D[num_pts]
        for i in range(num_pts):
            xval = randint(0, 100) # get random int in [0, 100)
            yval = randint(0, 100)
            prt.write(f"i({i}) xval({xval}) yval({yval})\n")
        #  points[i] = Point2D(xval, yval)
        #  points[i].draw()

        ## draw pt2d = (xval0, xval1) in red
        #Point2D pt2d = Point2D(xval0, yval0)
        #StdDraw.setPenColor(StdDraw.RED)
        #StdDraw.setPenRadius(.02)
        #pt2d.draw()


        ## draw line segments from pt2d to each point, one at a time, in polar order
        #StdDraw.setPenRadius()
        #StdDraw.setPenColor(StdDraw.BLUE)
        #Arrayvals.sort(points, pt2d.POLAR_ORDER)
        #for i in range(num_pts):
        #  pt2d.drawTo(points[i])
        #  StdDraw.show(100)

if __name__ == '__main__':
    main()
