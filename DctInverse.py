"""
Author: Léon Brodbeck, Simon Durrer
Last Modified: 29.12.2023
"""

import math

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
Picture = [[0 for _ in range(8)] for _ in range(8)]

def C(p):
    return 1 / math.sqrt(2) if p == 0 else 1.0

def dct_inverse(Freq, Picture):
    for x in range(8):
        for y in range(8):
            Summe = 0.0
            for u in range(8):
                for v in range(8):
                    Summe += C(u) * C(v) * Freq[v][u] * math.cos((2.0 * x + 1.0) * u * math.pi / 16.0) * math.cos((2.0 * y + 1.0) * v * math.pi / 16.0)
            Picture[y][x] = int(round(Summe / 4.0))

def copyBildToColors(Picture, idctColors, N):
    for x in range(N):
        for y in range(N):
            val = Picture[y][x]
            idctColors[y][x] = min(255, max(0, val))

def get_char_for_value(value):
    chars = "01234567"
    index = int((255 - value) / 32)  # Scales the inverted value to an index from 0 to 7
    return chars[index]

def print_idct(idctColors, N):
    for row in idctColors:
        for value in row:
            char = get_char_for_value(value)
            print(char, end=' ')
        print()

def main():
    dct_inverse(Frequency, Picture)
    idctColors = [[0 for _ in range(8)] for _ in range(8)]
    copyBildToColors(Picture, idctColors, 8)
    print_idct(idctColors, 8)

if __name__ == "__main__":
    main()
