#!/usr/bin/env python

import sys
import random

def main(prt=sys.stdout):
  """Unit tests the point data type."""
  if len(sys.argv[1:]) == 3:
    x0 = int(sys.argv[1])
    y0 = int(sys.argv[2])
    N  = int(sys.argv[3])

    # TBD....
    #StdDraw.setCanvasSize(800, 800)
    #StdDraw.setXscale(0, 100)
    #StdDraw.setYscale(0, 100)
    #StdDraw.setPenRadius(.005)
    #Point2D[] points = new Point2D[N]
    for i in range(N):
      x = random.randint(0, 100) # get random int in [0, 100)
      y = random.randint(0, 100)
      prt.write("i({}) x({}) y({})\n".format(i, x, y))
    #  points[i] = Point2D(x, y)
    #  points[i].draw()

    ## draw p = (x0, x1) in red
    #Point2D p = Point2D(x0, y0)
    #StdDraw.setPenColor(StdDraw.RED)
    #StdDraw.setPenRadius(.02)
    #p.draw()


    ## draw line segments from p to each point, one at a time, in polar order
    #StdDraw.setPenRadius()
    #StdDraw.setPenColor(StdDraw.BLUE)
    #Arrays.sort(points, p.POLAR_ORDER)
    #for i in range(N):
    #  p.drawTo(points[i])
    #  StdDraw.show(100)

if __name__ == '__main__':
  main()
