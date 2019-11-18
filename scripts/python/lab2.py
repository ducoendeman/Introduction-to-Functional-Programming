#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:25:16 2019

@author: duco

------------------------------------------------------------------------------------------------------------------------------
-- Lab 2: Validating Credit Card Numbers
------------------------------------------------------------------------------------------------------------------------------
"""

def toDigits(n):
    
    """
    toDigits :: Integer -> [Integer]
    
    type n = int
    rtype = list (of ints)
    """
    
    return [int(digit) for digit in str(n)]

def toDigitsRev(n):
    
    """
    toDigitRev:: Integer -> [Integer]
    
    type n = int
    retype = list (of ints)
    """    
        
    return list(reversed(toDigits(n)))

def doubleSecond(xs):

    """
    doubleSecond :: [Integer] -> [Integer]
    
    type xs = list (of integers)
    rtype = list (of integers)
    """
    
    return [xs[i] if i%2 == 0 else 2*xs[i] for i in range(len(xs))]

def sumDigits(xs):
    
    """
    sumDigits :: [Integer] -> Integer
    type xs = list (of integers)
    rtype = integer
    """
    
    return sum([int(digit) for number in xs for digit in str(number)])
    
def isValid(n):
     
     """
     isValid :: Integer -> Bool
     type n = int
     rtype = Bool
     """
     
     return n % 10 == 0
    
    
    
    
def creditcardValid(n):
    
    """
    type n = int
    rtype = Bool
    """
    
    return isValid(sumDigits(doubleSecond((toDigitsRev(n)))))
    
    
    