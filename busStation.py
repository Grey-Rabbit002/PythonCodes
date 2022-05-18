#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
def solve(a):
    # Write your code here
    fact=[]
    for i in range(len(a)):
        sum+=i
    mini=min(a)
    for i in range(1,sum+1):
        if(sum%i==0):
            fact.append(i)
    fact.remove(mini)
    
    csum=[]#store the cumulatige sum
    for i in range(1,len(a)):
        csum[i]=csum[i]+csum[i-1]
    
a=[1,2,1,1,1,2,1,3]
 