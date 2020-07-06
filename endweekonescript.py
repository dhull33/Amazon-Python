#!/usr/bin/env python3
"""
Author: David Hull

This module will finds the nth largest prime number using Wilson's Theorem and Converse. Which states that a natural
number n is prime if and only if (n-1)! ≡ -1 (mod n).

Given the nature of factorials the time it takes to find larger primes increases very quickly. However, it does work
and is very reliable.
"""

import math


def is_prime(n):
    if math.factorial(n - 1) % n == -1 % n:
        return True
    else:
        return False


def large_prime():
    n = int(input("What's the largest prime you want to know? "))

    prim = 5
    a = [2, 3]

    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        while len(a) < n:
            if is_prime(prim) == True:
                a.append(prim)
            prim += 2

    return a[-1]


def main():
    print(large_prime())


if __name__ == "__main__":
    main()
