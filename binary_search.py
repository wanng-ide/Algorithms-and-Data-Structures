# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 01:07:22 2019

@author: wanng

Binary search 二分查找
Only for a ordered list.
O(log n)
"""

def binary_search(list, target):
	low = 0
	high = len(list) - 1
	
	while low <= high:
		mid = int((low + high) / 2)
		guess = list[mid]
		if guess == target:
			return mid
		if guess < target:
			low = mid + 1
		else:
			high = mid - 1
	return None

test = [1, 2, 10, 55, 100, 101, 102]

print(binary_search(test, 55))
print(binary_search(test, 56))