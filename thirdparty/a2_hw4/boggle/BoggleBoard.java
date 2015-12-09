/******************************************************************************
 *  Compilation:  javac BoggleBoard.java
 *  Execution:    java  BoggleBoard
 *  Dependencies: StdRandom.java In.java StdOut.java
 *
 *  A data type for Boggle boards.
 *
 ******************************************************************************/

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class BoggleBoard {
    // the 16 Boggle dice (1992 version)
    private static final String[] BOGGLE_1992 = {
        "LRYTTE", "VTHRWE", "EGHWNE", "SEOTIS",
        "ANAEEG", "IDSYTT", "OATTOW", "MTOICU",
        "AFPKFS", "XLDERI", "HCPOAS", "ENSIEU",
        "YLDEVR", "ZNRNHL", "NMIQHU", "OBBAOJ"
    };

    // the 16 Boggle dice (1983 version)
    private static final String[] BOGGLE_1983 = {
        "AACIOT", "ABILTY", "ABJMOQ", "ACDEMP",
        "ACELRS", "ADENVZ", "AHMORS", "BIFORX",
        "DENOSW", "DKNOTU", "EEFHIY", "EGINTV",
        "EGKLUY", "EHINPS", "ELPSTU", "GILRUW",
    };

    // the 25 Boggle Master / Boggle Deluxe dice
    private static final String[] BOGGLE_MASTER = {
        "AAAFRS", "AAEEEE", "AAFIRS", "ADENNN", "AEEEEM",
        "AEEGMU", "AEGMNN", "AFIRSY", "BJKQXZ", "CCNSTW",
        "CEIILT", "CEILPT", "CEIPST", "DDLNOR", "DHHLOR",
        "DHHNOT", "DHLNOR", "EIIITT", "EMOTTT", "ENSSSU",
        "FIPRSY", "GORRVW", "HIPRRY", "NOOTUW", "OOOTTU"
    };

    // the 25 Big Boggle dice
    private static final String[] BOGGLE_BIG = {
        "AAAFRS", "AAEEEE", "AAFIRS", "ADENNN", "AEEEEM",
        "AEEGMU", "AEGMNN", "AFIRSY", "BJKQXZ", "CCENST",
        "CEIILT", "CEILPT", "CEIPST", "DDHNOT", "DHHLOR",
        "DHLNOR", "DHLNOR", "EIIITT", "EMOTTT", "ENSSSU",
        "FIPRSY", "GORRVW", "IPRRRY", "NOOTUW", "OOOTTU"
    };


    // letters and frequencies of letters in the English alphabet
    private static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final double[] FREQUENCIES = {
        0.08167, 0.01492, 0.02782, 0.04253, 0.12703, 0.02228,
        0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
        0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987,
        0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
        0.01974, 0.00074
    };

    private final int M;        // number of rows
    private final int N;        // number of columns
    private char[][] board;     // the M-by-N array of characters

    /**
     * Initializes a random 4-by-4 board, by rolling the Hasbro dice.
     */
    public BoggleBoard() {
        M = 4;
        N = 4;
        StdRandom.shuffle(BOGGLE_1992);
        board = new char[M][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                String letters = BOGGLE_1992[N*i+j];
                int r = StdRandom.uniform(letters.length());
                board[i][j] = letters.charAt(r);
            }
        }
    }
    
    /**
     * Initializes a board from the given filename.
     * @param filename the name of the file containing the Boggle board
     */
    public BoggleBoard(String filename) {
        In in = new In(filename);
        M = in.readInt();
        N = in.readInt();
        if (M <= 0) throw new IllegalArgumentException("number of rows must be a positive integer");
        if (N <= 0) throw new IllegalArgumentException("number of columns must be a positive integer");
        board = new char[M][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                String letter = in.readString().toUpperCase();
                if (letter.equals("QU"))
                    board[i][j] = 'Q';
                else if (letter.length() != 1)
                    throw new IllegalArgumentException("invalid character: " + letter);
                else if (ALPHABET.indexOf(letter) == -1)
                    throw new IllegalArgumentException("invalid character: " + letter);
                else 
                    board[i][j] = letter.charAt(0);
            }
        }
    }

    /**
     * Initializes a random M-by-N board, according to the frequency
     * of letters in the English language.
     * @param M the number of rows
     * @param N the number of columns
     */
    public BoggleBoard(int M, int N) {
        this.M = M;
        this.N = N;
        if (M <= 0) throw new IllegalArgumentException("number of rows must be a positive integer");
        if (N <= 0) throw new IllegalArgumentException("number of columns must be a positive integer");
        board = new char[M][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                int r = StdRandom.discrete(FREQUENCIES);
                board[i][j] = ALPHABET.charAt(r);
            }
        }
    }

    /**
     * Initializes a board from the given 2d character array,
     * with 'Q' representing the two-letter sequence "Qu".
     * @param a the 2d character array
     */
    public BoggleBoard(char[][] a) {
        this.M = a.length;
        this.N = a[0].length;
        if (M <= 0) throw new IllegalArgumentException("number of rows must be a positive integer");
        if (N <= 0) throw new IllegalArgumentException("number of columns must be a positive integer");
        board = new char[M][N];
        for (int i = 0; i < M; i++) {
            if (a[i].length != N)
                throw new IllegalArgumentException("char[][] array is ragged");
            for (int j = 0; j < N; j++) {
                if (ALPHABET.indexOf(a[i][j]) == -1)
                    throw new IllegalArgumentException("invalid character: " + a[i][j]);
                board[i][j] = a[i][j];
            }
        }
    }

    /**
     * Returns the number of rows.
     * @return number of rows
     */
    public int rows() { return M; }

    /**
     * Returns the number of columns.
     * @return number of columns
     */
    public int cols() { return N; }

    /**
     * Returns the letter in row i and column j,
     * with 'Q' representing the two-letter sequence "Qu".
     * @param i the row
     * @param j the column
     * @return the letter in row i and column j
     *    with 'Q' representing the two-letter sequence "Qu".
     */
    public char getLetter(int i, int j) {
        return board[i][j];
    }

    /**
     * Returns a string representation of the board, replacing 'Q' with "Qu".
     * @return a string representation of the board, replacing 'Q' with "Qu"
     */
    public String toString() {
        StringBuilder sb = new StringBuilder(M + " " + N + "\n");
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(board[i][j]);
                if (board[i][j] == 'Q') sb.append("u ");
                else sb.append("  ");
            }
            sb.append("\n");
        }
        return sb.toString().trim();
    }

    /**
     * Unit tests the BoggleBoard data type.
     */
    public static void main(String[] args) {

        // initialize a 4-by-4 board using Hasbro dice
        StdOut.println("Hasbro board:");
        BoggleBoard board1 = new BoggleBoard();
        StdOut.println(board1);
        StdOut.println();

        // initialize a 4-by-4 board using letter frequencies in English language
        StdOut.println("Random 4-by-4 board:");
        BoggleBoard board2 = new BoggleBoard(4, 4);
        StdOut.println(board2);
        StdOut.println();

        // initialize a 4-by-4 board from a 2d char array
        StdOut.println("4-by-4 board from 2D character array:");
        char[][] a =  {
            { 'D', 'O', 'T', 'Y' },
            { 'T', 'R', 'S', 'F' },
            { 'M', 'X', 'M', 'O' },
            { 'Z', 'A', 'B', 'W' }
        };
        BoggleBoard board3 = new BoggleBoard(a);
        StdOut.println(board3);
        StdOut.println();

        // initialize a 4-by-4 board from a file
        String filename = "board-quinquevalencies.txt";
        StdOut.println("4-by-4 board from file " + filename + ":");
        BoggleBoard board4 = new BoggleBoard(filename);
        StdOut.println(board4);
        StdOut.println();
    }
    
}
