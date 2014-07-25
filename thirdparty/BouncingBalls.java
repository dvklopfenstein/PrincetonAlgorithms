// Algorithms, Part 1 from Princeton University
// by Kevin Wayne, Robert Sedgewick
// https://class.coursera.org/algs4partI-005 retreived July 2014
// Lecture 8 - 4 Event-driven simulation (22-38)

// GOAL: Simulate the motion of N moving particles that behave 
//       according to te laws of elastic collision.
// HARD DISC MODEL 01:29
// * Moving particles interact via elastic collisions with each other & walls
// * Each particle is a disc with known position, velocity, mass, and radius.
// * No other forces.

// SIGNIFICANCE: Relates macroscopic observable(temp, pressure, diffusion k)
// to microscopic (motion of individual atoms and molecules) dynamics
// * Maxwell-Boltzmann: distribution of speeds as a function of temperature
// * Einstein: explain Brownian motion of pollen grains.

// java BouncingBalls 100
public class BouncingBalls
{
  // PQ contains all possible collisions that might happen in the future
  // PQ contains predicted collision times
  // Warm-up: Bouncing Balls without collisions
  public static void main(String[] args)
  {
    int N = Integer.parseInt(args[0]);
    Ball[] balls = new Ball[N];
    for (int i = 0; i < N; i++)
      balls[i] = new Ball();
    // main simulation loop 03:16
    while(true)
    {
      StdDraw.clear();
      for (int i = 0; i< N; i++)
      { 
        balls[i].move(0.5);
        balls[i].draw();
      }
      StdDraw.show(50);
    }
  }
}
