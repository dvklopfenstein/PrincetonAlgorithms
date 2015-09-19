# Analysis of Algorithms
  * [Order of Growth Examples](#order-of-growth-examples)
  * [Memory Examples](#memory-examples)

![order of growth](./images/orderofgrowth.png)

## [Order of Growth Examples](#analysis-of-algorithms)

What is the order of growth of the worst case running time of the following code fragment
as a function of N?

```
int sum = 0;
for (int i = 1; i*i <= N; i = i*4)
    sum++;
```
[Answer 1](#oog1)

```
int sum = 0;
for (int i = 1; i*i <= N; i = i*2)
    for (int j = 0; j < i; j++)
        sum++;
```
[Answer 2](#oog2)

```
int sum = 0;
for (int i = 0; i < N*N; i++)
    for (int j = i; j < N; j++)
        sum++;
```
[Answer 3](#oog3)

## [Memory Examples](#analysis-of-algorithms)
Given the following definition of a MysteryBox object.
Using the 64-bit memory cost model from lecture, how many bytes does
each object of type MysteryBox use? Include all memory allocated when the
client calls new MysteryBox().

```
public class MysteryBox {
    private final int x0;
    private final boolean y0, y1, y2;
    private final long z0, z1, z2, z3;
    private final double[] a = new double[248];

    ...
}
```
[Answer 1](#mem1)

```
public class MysteryBox {
    private final long x0, x1;
    private final double y0, y1, y2, y3;
    private final int z0, z1;
    private final boolean[] a = new boolean[280];

    ...
}
```
[Answer 2](#mem2)

```
public class MysteryBox {
    private final int x0, x1, x2;
    private final boolean y0;
    private final double z0, z1, z2, z3;
    private final long[] a = new long[152];

    ...
}
```
[Answer 3](#mem3)

## [Order of Growth Answers](#order-of-growth-examples)

### oog1
log N => The i loops iterates ~ log_4 (N^1/2) ~ lg N times.

### oog2
N^(1/2) => The body of inner loop is executed 1 + 2 + 4 + 8 + ... + sqrt(N) ~ 2 sqrt(N) times.

### oog3
N^2 => The i loop iterates N^2 times; the body of the j loop executes only when i < N.

## [Memory Answers](#memory-examples)

### mem1
```
public class MysteryBox {                           //   16 (object overhead)
    private final int x0;                           //    4 (1 int)
    private final boolean y0, y1, y2;               //    3 (3 boolean)
    private final long z0, z1, z2, z3;              //   32 (4 long)
    private final double[] a = new double[248];     //    8 (reference to array)
                                                    // 2008 (double array of size 248)
    ...                                                   1 (padding to round up to a multiple of 8)
}                                                      ----
                                                       2072
```

### mem2
```
public class MysteryBox {                           //   16 (object overhead)
    private final long x0, x1;                      //   16 (2 long)
    private final double y0, y1, y2, y3;            //   32 (4 double)
    private final int z0, z1;                       //    8 (2 int)
    private final boolean[] a = new boolean[280];   //    8 (reference to array)
                                                    //  304 (boolean array of size 280)
    ...                                                   0 (padding to round up to a multiple of 8)
}                                                      ----
                                                        384
```

### mem3
```
public class MysteryBox {                           //   16 (object overhead)
    private final int x0, x1, x2;                   //   12 (3 int)
    private final boolean y0;                       //    1 (1 boolean)
    private final double z0, z1, z2, z3;            //   32 (4 double)
    private final long[] a = new long[152];         //    8 (reference to array)
                                                    // 1240 (long array of size 152)
    ...                                                   3 (padding to round up to a multiple of 8)
}                                                      ----
                                                       1312
```
