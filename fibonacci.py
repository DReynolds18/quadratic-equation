# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 18:16:04 2022

@author: dreynolds18

Fibonacci numbers is a sequence of numbers starting with 1, 1, and the next number in the sequence is the sum of the 
previous two. So the sequence looks like 1,2,3,5,8,...

F[n] = F[n-1} + F[N-2]

1. Write a function 'make_Fibonacci' that returns the first N Fibonacci numbers. Put the function in a module named 
fibonacci  (that's just a file named fibonacci.py).  
In the module, put a test block, so that if the file were run as a program,
the first 20 Fibonacci numbers print to the screen. 

2.  Johannes Kepler (yes, that Johannes Kepler) claimed that the ratio of consecutive Fibonacci numbers converges to the
'golden ratioLinks to an external site..'   

Golden Ratio:      F[N+1]/F[N] -> (read, 'gets close to  as N increases' )  (1+sqrt(5))/2

Extend your module by defining a function 'converging_ratios' that takes an array or list F that contains Fibonacci 
numbers as input and tests to see if Kepler's claim seems correct.
Put a call to the function in the test block and run the function.

3.'Rate of convergence' is a mathematical concept that shows up in math and engineering.
if e[N] is the difference between the ratio F[N+1]/F[N} then e[N} = C*e[N}**q, C is some constant, then q is the rate of
convergence   The computation for q is

q = np.log(e[N+1]/e{N]) / np.log(e[N]/e[N-1)

Extend your module by including a function 'computre_rates' that  takes a sequence F, and computes the corresponding 
values for q and prints the last 5 values. You do not need any value for C,
The convergence rates should get close to 1 and N gets large.
"""
import numpy as np

def make_Fibonacci(n):
    """
    

    Parameters
    ----------
    n : TYPE integer
        DESCRIPTION. the length of the Fibonacci sequence returned

    Returns
    -------
    F: a list that contains the first n fibanocci number

    """
    
    F=[1,1]
    if n ==1:
        F=[1]
        #print(F)
        return F
    
    for i in range(2,n):
        F.append(F[i-1] + F[i-2])
    return F

def converging_ratios(F):
    golden_ratio = (1+np.sqrt(5))/2
    n = len(F)
    print(f"length of F is {n}")
    error = []
    for i in range(n-1):
        error.append(F[i+1]/F[i] - golden_ratio)
    return error

def computre_rates(error):
    n = len(error)
    error = [abs(x) for x in error]
    q = []
    for i in range(n-1):
        q.append(np.log(error[i+1]/error[i]) / np.log(error[i]/error[i-1]))
    return q
 
    
if __name__ =='__main__':
    print(make_Fibonacci(20))
    print(converging_ratios((make_Fibonacci(20))))
    print(computre_rates(converging_ratios((make_Fibonacci(20)))))
    
    import matplotlib.pyplot as plt
    e = (converging_ratios((make_Fibonacci(20))))
    plt.plot(e)
    
    q = (computre_rates(converging_ratios((make_Fibonacci(20)))))
    plt.plot(q)