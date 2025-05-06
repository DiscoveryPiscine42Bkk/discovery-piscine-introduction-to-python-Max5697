#!/usr/bin/python3

import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()

i = 0
while i <= 10:
    print(f"Table de {i}:", end=" ")
    b = 0
    while b <= 10:
        print(i * b, end=" ")
        b += 1
    print()
    i += 1