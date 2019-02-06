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

# 一个贪婪算法的例子：贪婪算法近似集合覆盖问题

# 要覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# 广播台清单
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set() # 存储最终选择的广播台

while states_needed:  # 只要没有全部覆盖完
  best_station = None 
  states_covered = set()  # 存储已经覆盖的州
  for station, states in stations.items(): # items()存储键值(广播台和相应的覆盖州)
    covered = states_needed & states  # 集合的交集，判断还未覆盖的州与此广播台的交集个数   
    if len(covered) > len(states_covered): # 如果当前广播台州交集的个数大于当前要覆盖的州 
      best_station = station  # 就替换为最优的广播台
      states_covered = covered  # 替换已经覆盖的州

  states_needed -= states_covered # 从要覆盖的州中减去已经覆盖过的(集合相减)
  print('states_needed:',states_needed)
  final_stations.add(best_station) # 添加最优的广播台

print(final_stations)
