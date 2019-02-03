# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:04:56 2019

@author: wanng

Average: O(n*(log n))
Worst: O(n^2)

divide and conquer
The smallest ordered list is "one element list" or "none element list".
Recursive condition is: find the smaller group and the bigger group for pivot element.
"""

def quickSort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		smaller = [ ]
		bigger = [ ]
		for i in array[1:]:
			if i <= pivot:
				smaller.append(i)
			else:
				bigger.append(i)
		return quickSort(smaller) + [pivot] + quickSort(bigger)

test = [5, 6, 1, 3, 10]

print(quickSort(test))