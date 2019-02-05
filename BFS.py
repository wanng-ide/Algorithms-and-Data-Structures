# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 23:28:13 2019

@author: wanng

Breadth-First Search
在书中是用于找出段数最少的路径
Method: Queue

This example is from book "grokking algorithms".

"""

from collections import deque 

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
	return name[-1] == 'm'

def search(name):
	search_queue = deque()
	search_queue += graph[name]
	
	while search_queue:
		person = search_queue.popleft()
		if person_is_seller(person):
			print(person + " is a mango seller!")
			return True
		else:
			search_queue += graph[person]
	return False

search("you")
