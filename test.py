# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 14:00:04 2019

@author: wanng

This file is for some small tests
"""
def mysum(arr = None):
	if arr == [ ]:
		return 0
	else:
		return arr[0] + mysum(arr[1:])

def findLen(arr = None):
	if arr == [ ]:
		return 0
	else:
		return 1 + findLen(arr[1:])
	
def findBig(arr):
	if len(arr) == 2:
		return arr[0] if arr[0] > arr[1] else arr[1]
	sub_big = findBig(arr[1:])
	return arr[0] if arr[0] > sub_big else sub_big

testarr = [5, 6, 1, 3, 10]

print(mysum(testarr))
print(findLen(testarr))
print(findBig(testarr))
