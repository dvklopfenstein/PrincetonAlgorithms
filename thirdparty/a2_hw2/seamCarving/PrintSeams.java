/******************************************************************************
 *  Compilation:  javac PrintSeams.java
 *  Execution:    java PrintSeams input.png
 *  Dependencies: SeamCarver.java
 *
 *  Read image from file specified as command-line argument. Print square
 *  of energies of pixels, a vertical seam, and a horizontal seam.
 *
 *  % java PrintSeams 6x5.png
 *  6x5.png (6-by-5 image)
 *
 *  The table gives the dual-gradient energies of each pixel.
 *  The asterisks denote a minimum energy vertical or horizontal seam.
 *
 *  Vertical seam: { 3 4 3 2 1 }
 *  1000.00  1000.00  1000.00  1000.00* 1000.00  1000.00  
 *  1000.00   237.35   151.02   234.09   107.89* 1000.00  
 *  1000.00   138.69   228.10   133.07*  211.51  1000.00  
 *  1000.00   153.88   174.01*  284.01   194.50  1000.00  
 *  1000.00  1000.00* 1000.00  1000.00  1000.00  1000.00  
 *  Total energy = 2414.973496
 *  
 *  
 *  Horizontal seam: { 2 2 1 2 1 2 }
 *  1000.00  1000.00  1000.00  1000.00  1000.00  1000.00 
 *  1000.00   237.35   151.02*  234.09   107.89* 1000.00  
 *  1000.00*  138.69*  228.10   133.07*  211.51  1000.00*  
 *  1000.00   153.88   174.01   284.01   194.50  1000.00  
 *  1000.00  1000.00  1000.00  1000.00  1000.00  1000.00  
 *  Total energy = 2530.681960
 *
 ******************************************************************************/

import edu.princeton.cs.algs4.Picture;
import edu.princeton.cs.algs4.StdOut;

public class PrintSeams {
    private static final boolean HORIZONTAL   = true;
    private static final boolean VERTICAL     = false;

    private static void printSeam(SeamCarver carver, int[] seam, boolean direction) {
        double totalSeamEnergy = 0.0;

        for (int row = 0; row < carver.height(); row++) {
            for (int col = 0; col < carver.width(); col++) {
                double energy = carver.energy(col, row);
                String marker = " ";
                if ((direction == HORIZONTAL && row == seam[col]) ||
                    (direction == VERTICAL   && col == seam[row])) {
                    marker = "*";
                    totalSeamEnergy += energy;
                }
                StdOut.printf("%7.2f%s ", energy, marker);
            }
            StdOut.println();
        }                
        // StdOut.println();
        StdOut.printf("Total energy = %f\n", totalSeamEnergy);
        StdOut.println();
        StdOut.println();
    }

    public static void main(String[] args) {
        Picture picture = new Picture(args[0]);
        StdOut.printf("%s (%d-by-%d image)\n", args[0], picture.width(), picture.height());
        StdOut.println();
        StdOut.println("The table gives the dual-gradient energies of each pixel.");
        StdOut.println("The asterisks denote a minimum energy vertical or horizontal seam.");
        StdOut.println();

        SeamCarver carver = new SeamCarver(picture);
        
        StdOut.printf("Vertical seam: { ");
        int[] verticalSeam = carver.findVerticalSeam();
        for (int x : verticalSeam)
            StdOut.print(x + " ");
        StdOut.println("}");
        printSeam(carver, verticalSeam, VERTICAL);

        StdOut.printf("Horizontal seam: { ");
        int[] horizontalSeam = carver.findHorizontalSeam();
        for (int y : horizontalSeam)
            StdOut.print(y + " ");
        StdOut.println("}");
        printSeam(carver, horizontalSeam, HORIZONTAL);

    }

}
