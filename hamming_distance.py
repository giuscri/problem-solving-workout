#!/usr/bin/python3

## WARNING!, HIGHLY PYTHONIC.

def hamming_distance(A, B):
    return len(''.join(bin(A ^ B)[2:].split('0')))
