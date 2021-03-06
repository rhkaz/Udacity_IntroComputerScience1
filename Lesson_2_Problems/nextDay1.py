#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:22:32 2016

@author: RashidKazmi
"""

###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """Warning: this version incorrectly 
    assumes all months have 30 days """
    if (day < 30):
        return year, month, day + 1
    if (year < 12):
        return year, month + 1, 1
    else:
        return year + 1, 1, 1
        
print (nextDay(1999, 12, 30))    