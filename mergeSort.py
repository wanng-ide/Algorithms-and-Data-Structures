# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:32:07 2019

@author: wanng

Average, Worst: O(n*(log n))

divide and conquer
Sort left and right list and merge.
"""

def merge(left, right):
	temp = [ ]
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			temp.append(left[i])
			i += 1
		else:
			temp.append(right[j])
			j += 1
	temp += left[i:]
	temp += right[j:]
	return temp

def mergeSort(array):
	if len(array) < 2:
		return array
	mid = int(len(array) / 2)
	left = mergeSort(array[:mid])
	right = mergeSort(array[mid:])
	return merge(left, right)

test = [5, 6, 1, 3, 10]

print(mergeSort(test))