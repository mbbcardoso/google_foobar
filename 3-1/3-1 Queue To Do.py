#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://www.geeksforgeeks.org/calculate-xor-1-n/
# Function to calculate xor  
def computeXOR(n): 
  
    # Modulus operator are expensive  
    # on most of the computers. n & 3  
    # will be equivalent to n % 4. 
  
    # if n is multiple of 4  
    if n % 4 == 0 : 
        return n 
  
    # If n % 4 gives remainder 1 
    if n % 4 == 1 : 
        return 1
  
    # If n%4 gives remainder 2  
    if n % 4 == 2 : 
        return n + 1
  
    # If n%4 gives remainder 3 
    return 0

def solution(start, length):
    # process each row at a time
    first = start
    step = length - 1
    checksum = 0
    for row in range(length):
        first = start + length * row
        last = first + step
        checksum ^= computeXOR(first-1) ^ computeXOR(last)
        step -= 1 
    return checksum

