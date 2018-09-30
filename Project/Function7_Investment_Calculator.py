#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 17:12:35 2018

@author: root
"""

### START FUNCTION 7

def investment(PMT, n, i):

    # YOUR CODE HERE
    
    investment_balance = 0
    interest_rate = 1 + i
    
    for year in range(n):
        year = year + 1
        if (year % 2) == 0:
            PMT *= 2
        investment_balance =  PMT + investment_balance * interest_rate
    
    return round(investment_balance, 2)

### END FUNCTION 7
print(investment(15000, 30, 0.1045))   
#investment(15000, 30, 0.1045) == 1954935238.47

print(investment(10000, 40, 0.1045))
#investment(10000, 40, 0.1045) == 41728281751.16

