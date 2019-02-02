# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 01:00:53 2019

@author: wanng

SelectionSort

O(n^2)
find the smallest #, and pop it, then find the smallest in the rest
"""

def FindSmallest(array):
	small = array[0]
	small_index = 0
	for i in range(1, len(array)):
		if array[i] < small:
			small = array[i]
			small_index = i
	return small_index

def SelectionSort(array):
	ordered = []
	for i in range(len(array)):
		small = FindSmallest(array)
		ordered.append(array.pop(small))
	return ordered

test = [11, 2, 5, 7, 10, 1, 0]
print(len(test))
print(SelectionSort(test))