/******************************************************************************
 *  Compilation:  javac InteractivePercolationVisualizer.java
 *  Execution:    java InteractivePercolationVisualizer N
 *  Dependencies: PercolationVisualizer.java Percolation.java
 *                StdDraw.java StdOut.java
 *
 *  This program takes the grid size N as a command-line argument.
 *  Then, the user repeatedly clicks sites to open with the mouse.
 *  After each site is opened, it draws full sites in light blue,
 *  open sites (that aren't full) in white, and blocked sites in black.
 *
 ******************************************************************************/

import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

public class InteractivePercolationVisualizer {

    public static void main(String[] args) {
        // N-by-N percolation system (read from command-line, default = 10)
        int N = 10;          
        if (args.length == 1) N = Integer.parseInt(args[0]);

        // repeatedly open site specified my mouse click and draw resulting system
        StdOut.println(N);

        StdDraw.show(0);
        Percolation perc = new Percolation(N);
        PercolationVisualizer.draw(perc, N);
        StdDraw.show(0);

        while (true) {

            // detected mouse click
            if (StdDraw.mousePressed()) {

                // screen coordinates
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();

                // convert to row i, column j
                int i = (int) (N - Math.floor(y));
                int j = (int) (1 + Math.floor(x));

                // open site (i, j) provided it's in bounds
                if (i >= 1 && i <= N && j >= 1 && j <= N) {
                    if (!perc.isOpen(i, j)) { 
                        StdOut.println(i + " " + j);
                    }
                    perc.open(i, j);
                }

                // draw N-by-N percolation system
                StdDraw.show(0);
                PercolationVisualizer.draw(perc, N);
            }
            StdDraw.show(20);
        }
    }
}
