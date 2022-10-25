# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:17:26 2022

@author: dreynolds18

Objective:
Write a function roots that computes the roots of a quadratic equation. Check for complex roots and print an
error message saying that the roots are complex.
"""
import math

def roots(a,b,c):
    
    quadraticComplex = b**2 - 4 * a * c
    
    if (a == 0 or b == 0 or c == 0):
        print("A, B, or C cannot equal 0")

    else:
        if (quadraticComplex < 0):
            print('Roots are complex')
        else:    
            addX = (-(b) + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
            subX = (-(b) - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
            print(f'The Roots are {addX} and {subX}')
    
    
#####################################################################     
  
if __name__ == '__main__':
    roots(2,9,-5)
    
    roots(1,0,3)
    
    roots(1,-2,5)
    
    roots(1,-10,25)