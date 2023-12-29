# DctInverse
Python implementation of Inverse Discrete Cosine Transform (IDCT).

This module demonstrates the basic implementation of the Inverse Discrete Cosine Transform (IDCT).
It includes functions to compute the IDCT for an 8x8 matrix, copy the transformed values to a new matrix
while constraining the values, and print the resulting matrix in a readable format.

Functions:
    C(p): Calculates the coefficient for the IDCT.
    dct_inverse(Freq, Bild): Performs the inverse DCT on a given 8x8 frequency matrix.
    copyBildToColors(Bild, idctColors, N): Copies and constrains the values from the Bild matrix to idctColors.
    get_char_for_value(value): Maps a numeric value to a character for visualization.
    print_idct(idctColors, N): Prints the IDCT color matrix.
    main(): Main function to run the IDCT process.
