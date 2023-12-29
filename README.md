# TI-nspire CX II-T Inverse Discrete Cosine Transform (IDCT)

This repository contains Python scripts for performing Inverse Discrete Cosine Transformations, optimized for the TI-nspire CX II-T calculator.

## Inverse Discrete Cosine Transform (IDCT)

`DctInverse.py` performs the Inverse Discrete Cosine Transform on an 8x8 matrix of frequency values and prints the resulting matrix in a readable format.

### Customization

- Change the values of the frequency matrix to perform the IDCT on different data.

### Use on TI-nspire CX CAS
Download the .py and .tns files from the repository.
Transfer these files to your calculator using the TI-nspire CX CAS Student Software.
Open the files on the calculator to run the scripts.
For more details on the use and customization of the scripts, see the comments in the code.

### Detailed Calculation Output

The output of the IDCT is a matrix of color values. The values are constrained to be between 0 and 255, and are rounded to the nearest integer. The output matrix is printed in a readable format.

### Credit to for supporting:

https://github.com/SimonDurrer

### Example
**Input:**
```python
# 8x8 Frequency Matrix
Frequency = [
    [1024, 512, 0, 0, 0, 0, 0, 0],
    [512, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
```

**Output:**
```python
0 0 0 0 1 2 3 3 
0 0 0 1 2 3 3 4 
0 0 0 1 2 3 4 5 
0 1 1 2 3 5 5 6 
1 2 2 3 5 6 6 7 
2 3 3 5 6 7 7 7 
3 3 4 5 6 7 7 7 
3 4 5 6 7 7 7 7 