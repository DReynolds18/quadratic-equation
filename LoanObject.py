# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:06:57 2022

@author: dreynolds18
"""

class loan(object):
    def __init__ (self, name):  # initialize with a name, thie permits
                                # easier manamgement of multiple instances
        """
        loan is a class object to implement computations of 
        loan parameters
        
        name: documents the name associated with the instance of loan 

        Returns
        -------
        None.

        """
        #initialization
        self._name = name
        self._Pv = 0
        self._intAPR = 0
        self._Pmt = 0
        self._nMonths=0
        
        
    def getName(self):
        print(f"\nname on this instance: {self._name}")
    
    def getChoice(self):
        print("\nwhat would you like to compute?")
        print("options: Pmt, Pv, intAPR, nMonths")
        
        choice = 0
        
        while choice  not in ("Pmt", "Pv", "intAPR", "nMonths"):
            choice = input("enter choice ")
            
        if choice == "Pmt":
            self.computePmt()
        elif choice == 'Pv':
            self.computePv()
        elif choice == 'intAPR':
            self.compute_intAPR()
        else:
            self.compute_nMonths()


    def compute_intAPR(self):
        ''' Solve for interest rate, APR  '''
        self._Pv = float(input('Enter PV '))
        self._Pmt = float(input('Enter Pmt '))
        self._nMonths = int(input('Enter number of months '))
        
        # The solution will be r where using Pmt, n, and Pv works
        ## bisection algorithm finds the two sides of the equation are equal
        ## that is, the difference is 0
        ## side 1: Pmt*(1-(1+r)**(-n))
        ## side 2:  Pv*r
        
        #example of an in-line (lambda) function
        fIntRate = lambda r: self._Pmt*(1-(1+r)**(-self._nMonths)) - self._Pv*r
        
        # low and high possible interest rates, APR
        # the actual rate is between 
        
        _rlow =0
        _rhigh = 50 
        
        _rl = _rlow/1200
        _rh = _rhigh/1200
        _count = 0
        
        while(_count < 20): # in case there is no solution
            _rTry = (_rl+_rh)/2
            if abs(fIntRate(_rTry)) < 0.001: break
            
            if fIntRate(_rTry) > 0: _rl = _rTry
            else: _rh = _rTry
            
            _count += 1
            
        if(_count >=20):
            print("no solution: try again")
            print(f"interest rate APR is > {_rTry*1200:.2f}%") # convert back to APR
            rTry = None
        
        print(f"Interest rate = {_rTry*1200}")
        return _rTry*1200

    def computePmt(self):
        # Pmt =  r/1200*PV/(1-(1+(r/1200))**(-n)) 
        # assumes you entered interest rate as APR
        self._Pv = float(input('Enter PV '))
        self._intAPR = float(input('Enter intrest rate '))
        self._nMonths = int(input('Enter number of months '))
        
        _r = self._intAPR / 1200
        
        self._Pmt = _r*self._Pv/(1-(1+_r)**(-self._nMonths))
        
        print(f"Monthly Payment = {self._Pmt}")
        return self._Pmt
    
    def compute_nMonths(self):
        import numpy as np
        #formula for _nMonths:
        # -np.log(1-(_r*self._Pv/self._Pmt)/np.log((1+_r))
        self._Pv = float(input('Enter PV '))
        self._intAPR = float(input('Enter intrest rate '))
        self._Pmt = float(input('Enter Pmt '))
        
        _r = self._intAPR / 1200
        
        self._nMonths = -np.log(1-_r*self._Pv/self._Pmt)/np.log((1+_r))
        
        print(f"{self._nMonths} months to pay off loan")
        return self._nMonths

    
    def computePv(self):
        #formula for PV:
        # self._Pmt/_r *(1-(1+_r)**(-self._nMonths))
        
        self._intAPR = float(input('Enter intrest rate '))
        self._Pmt = float(input('Enter Pmt '))
        self._nMonths = int(input('Enter number of months '))
        
        _r = self._intAPR / 1200
        
        self._Pv = self._Pmt/_r *(1-(1+_r)**(-self._nMonths))
        
        print(f'Pv = {self._Pv:.2f}')
        return self._Pv


#####################################################################     
  
if __name__ == '__main__':
    
    testloan = loan('example1')
    testloan.getName()
    
    testloan.getChoice()