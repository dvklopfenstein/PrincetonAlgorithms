/******************************************************************************
 *  Compilation:  javac SCUtility.java
 *  Execution:    none
 *  Dependencies: SeamCarver.java
 *
 *  Some utility functions for testing SeamCarver.java.
 *
 ******************************************************************************/

import java.awt.Color;

import edu.princeton.cs.algs4.Picture;
import edu.princeton.cs.algs4.StdRandom;

public class SCUtility {


    // create random W-by-H array of tiles
    public static Picture randomPicture(int W, int H) {
        Picture p = new Picture(W, H);
        for (int i = 0; i < W; i++)
            for (int j = 0; j < H; j++) {
                int r = StdRandom.uniform(255);
                int g = StdRandom.uniform(255);
                int b = StdRandom.uniform(255);
                Color c = new Color(r, g, b);
                p.set(i, j, c);
            }
        return p;
    }


    public static double[][] toEnergyMatrix(SeamCarver sc) {
        double[][] returnDouble = new double[sc.width()][sc.height()];
        for (int i = 0; i < sc.width(); i++)
            for (int j = 0; j < sc.height(); j++)
                returnDouble[i][j] = sc.energy(i, j);
    
        return returnDouble;        
    }

    // displays grayvalues as energy (converts to picture, calls show)
    public static void showEnergy(SeamCarver sc) {
        doubleToPicture(toEnergyMatrix(sc)).show();
    }

    public static Picture toEnergyPicture(SeamCarver sc) {
        double[][] energyMatrix = toEnergyMatrix(sc);
        return doubleToPicture(energyMatrix);
    }

    // converts a double matrix of values into a normalized picture
    // values are normalized by the maximum grayscale value (ignoring border pixels)
    public static Picture doubleToPicture(double[][] grayValues) {

        // each 1D array in the matrix represents a single column, so number
        // of 1D arrays is the width, and length of each array is the height
        int width = grayValues.length;
        int height = grayValues[0].length;

        Picture picture = new Picture(width, height);

        // maximum grayscale value (ignoring border pixels)
        double maxVal = 0;
        for (int i = 1; i < width-1; i++)
            for (int j = 1; j < height-1; j++)
                if (grayValues[i][j] > maxVal)
                    maxVal = grayValues[i][j];
            
        if (maxVal == 0)
            return picture; //return black picture

        for (int i = 0; i < width; i++)
            for (int j = 0; j < height; j++) {
                float normalizedGrayValue = (float) grayValues[i][j] / (float) maxVal;
                if (normalizedGrayValue >= 1.0f) normalizedGrayValue = 1.0f;
                picture.set(i, j, new Color(normalizedGrayValue, normalizedGrayValue, normalizedGrayValue));
            }

        return p;
    }


    // This method is useful for debugging seams. It overlays red
    // pixels over the calculate seam. Due to the lack of a copy
    // constructor, it also alters the original picture.

    public static Picture seamOverlay(Picture p, boolean horizontal, int[] seamIndices) {
        Picture overlaid = new Picture(p.width(), p.height());

        for (int i = 0; i < p.width(); i++)
            for (int j = 0; j < p.height(); j++)
                overlaid.set(i, j, p.get(i, j));
        
        int width = p.width();
        int height = p.height();

        //if horizontal seam, then set one pixel in every column
        if (horizontal)
            for (int i = 0; i < width; i++)
                overlaid.set(i, seamIndices[i], Color.RED);
        else // if vertical, put one pixel in every row
            for (int j = 0; j < height; j++)
                overlaid.set(seamIndices[j], j, Color.RED);

        return overlaid;
    }

}
