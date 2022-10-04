# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:35:46 2022

@author: Dylan Reynolds

A prime number is a number whose only divisors are 1 and itself.  For example 1, 2, 3 5, 7, 11, 13 .. are prime numbers, but 9 (divisor of 3),  51 (divisor of 3) .. are not prime.

Write a python program to print out all the prime numbers < 1000
"""

def is_prime(n):
    if n > 0:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

for thousand in range(1,1001):
    if (is_prime(thousand)):
        print(thousand)