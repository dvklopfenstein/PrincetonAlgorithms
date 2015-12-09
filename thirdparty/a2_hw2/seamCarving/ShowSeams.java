/******************************************************************************
 *  Compilation:  javac ShowSeams.java
 *  Execution:    java ShowSeams input.png
 *  Dependencies: SeamCarver.java SCUtility.java
 *
 *  Read image from file specified as command line argument. Show 3 images 
 *  original image as well as horizontal and vertical seams of that image.
 *  Each image hides the previous one - drag them to see all three.
 *
 ******************************************************************************/

import edu.princeton.cs.algs4.Picture;
import edu.princeton.cs.algs4.StdOut;

public class ShowSeams {

    private static void showHorizontalSeam(SeamCarver sc) {
        Picture picture = SCUtility.toEnergyPicture(sc);
        int[] horizontalSeam = sc.findHorizontalSeam();
        Picture overlay = SCUtility.seamOverlay(picture, true, horizontalSeam);
        overlay.show();
    }


    private static void showVerticalSeam(SeamCarver sc) {
        Picture picture = SCUtility.toEnergyPicture(sc);
        int[] verticalSeam = sc.findVerticalSeam();
        Picture overlay = SCUtility.seamOverlay(picture, false, verticalSeam);
        overlay.show();
    }

    public static void main(String[] args) {
        Picture picture = new Picture(args[0]);
        StdOut.printf("image is %d columns by %d rows\n", picture.width(), picture.height());
        picture.show();        
        SeamCarver sc = new SeamCarver(picture);
        
        StdOut.printf("Displaying horizontal seam calculated.\n");
        showHorizontalSeam(sc);

        StdOut.printf("Displaying vertical seam calculated.\n");
        showVerticalSeam(sc);

    }

}
