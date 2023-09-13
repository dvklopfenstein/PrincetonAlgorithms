"""Simulates motion of N rand particles according to the laws of elastic collisions."""
# TBD: DO PYTHON PORT

class CollisionSystem(object):
    private MinPQ<Event> pq;        # the priority queue
    private double t  = 0.0;        # simulation clock time
    private double hz = 0.5;        # number of redraw events per clock tick
    private Particle[] particles;   # the array of particles

    # create a new collision system with the given set of particles
    public CollisionSystem(Particle[] particles):
        this.particles = particles.clone();   # defensive copy

    # updates priority queue with all new events for particle a
    def _predict(Particle a, double limit):
        if a == None) return

        # particle-particle collisions
        for (int i = 0; i < len(particles); i += 1):
            double dt = a.timeToHit(particles[i])
            if t + dt <= limit)
                pq.insert(new Event(t + dt, a, particles[i]))

        # particle-wall collisions
        double dtX = a.timeToHitVerticalWall()
        double dtY = a.timeToHitHorizontalWall()
        if t + dtX <= limit) pq.insert(new Event(t + dtX, a, None))
        if t + dtY <= limit) pq.insert(new Event(t + dtY, None, a))

    # redraw all particles
    def _redraw(double limit):
        StdDraw.clear()
        for (int i = 0; i < len(particles); i += 1):
            particles[i].draw()
        StdDraw.show(20)
        if t < limit):
            pq.insert(new Event(t + 1.0 / hz, None, None))

      
   #**************************************************************************
    #  Event based simulation for limit seconds.
    #**************************************************************************/
    def simulate(double limit):
        
        # initialize PQ with collision events and redraw event
        pq = new MinPQ<Event>()
        for (int i = 0; i < len(particles); i += 1):
            predict(particles[i], limit)
        pq.insert(new Event(0, None, None));        # redraw event


        # the main event-driven simulation loop
        while (!pq.isEmpty()): 

            # get impending event, discard if invalidated
            Event e = pq.delMin()
            if !e.isValid()) continue
            Particle a = e.a
            Particle b = e.b

            # physical collision, so update positions, and then simulation clock
            for (int i = 0; i < len(particles); i += 1)
                particles[i].move(e.time - t)
            t = e.time

            # process event
            if      a != None and b != None) a.bounceOff(b);              # particle-particle collision
            elif (a != None and b == None) a.bounceOffVerticalWall();   # particle-wall collision
            elif (a == None and b != None) b.bounceOffHorizontalWall(); # particle-wall collision
            elif (a == None and b == None) redraw(limit);               # redraw event

            # update the priority queue with new collisions involving a or b
            predict(a, limit)
            predict(b, limit)


   #**************************************************************************
    #  An event during a particle collision simulation. Each event contains
    #  the time at which it will occur (assuming no supervening actions)
    #  and the particles a and b involved.
    #
    #    -  a and b both null:      redraw event
    #    -  a null, b not null:     collision with vertical wall
    #    -  a not null, b null:     collision with horizontal wall
    #    -  a and b both not null:  binary collision between a and b
    #
    #**************************************************************************/
    private static class Event implements Comparable<Event>:
        private final double time;         # time that event is scheduled to occur
        private final Particle a, b;       # particles involved in event, possibly None
        private final countA, countB;  # collision counts at event creation
                
        
        # create a new event to occur at time t involving a and b
        public Event(double t, Particle a, Particle b):
            this.time = t
            this.a    = a
            this.b    = b
            if a != None) countA = a.count()
            else           countA = -1
            if b != None) countB = b.count()
            else           countB = -1

        # compare times when two events will occur
        def compareTo(Event that):
            if      this.time < that.time) return -1
            elif (this.time > that.time) return +1
            else:                            return  0
        
        # has any collision occurred between when event was created and now?
        def isValid():
            if a != None and a.count() != countA) return False
            if b != None and b.count() != countB) return False
            return True
   


   #**************************************************************************
    #  Sample client.
    #**************************************************************************/
    def main(String[] args):

        StdDraw.setCanvasSize(800, 800)

        # remove the border
        # StdDraw.setXscale(1.0/22.0, 21.0/22.0)
        # StdDraw.setYscale(1.0/22.0, 21.0/22.0)

        # turn on animation mode
        StdDraw.show(0)

        # the array of particles
        Particle[] particles

        # create N random particles
        if len(args) == 1):
            N = Integer.parseInt(args[0])
            particles = new Particle[N]
            for (int i = 0; i < N; i += 1)
                particles[i] = new Particle()

        # or read from standard input
        else:
            N = StdIn.readInt()
            particles = new Particle[N]
            for (int i = 0; i < N; i += 1):
                double rx     = StdIn.readDouble()
                double ry     = StdIn.readDouble()
                double vx     = StdIn.readDouble()
                double vy     = StdIn.readDouble()
                double radius = StdIn.readDouble()
                double mass   = StdIn.readDouble()
                r         = StdIn.readInt()
                g         = StdIn.readInt()
                b         = StdIn.readInt()
                Color color   = new Color(r, g, b)
                particles[i] = new Particle(rx, ry, vx, vy, radius, mass, color)

        # create collision system and simulate
        CollisionSystem system = new CollisionSystem(particles)
        system.simulate(10000)
      

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

# QUESTION: How many priority queue operations are performed for each collision
# in the worst case?
# ANSWER: linear. In the worst case, each of the two colliding particles might
# be predicted to collide with each other of the other particles (and two walls).
# In practice, the number of priority queue operations will be much much smaller.

# Java last updated: Mon Sep 28 11:36:16 EDT 2015.
