"""
Program to segregate 0's and 1's in an array
"""

from collections import Counter

def swap(arr,i,j):
	"""
	Function to swap the array element
	"""
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def segregate(arr):
	"""
	Function where we are looping until i < j
	low keeps track of 0's and high keeps track of 1's
	"""
	size = len(arr)
	low, high = 0, size-1
	while(low<high):
		if arr[low] == 0:
			low+=1
		elif arr[low] == 1:
			swap(arr,low,high)
			high-=1

###############################################################

def segregate_v2(arr):
	"""
    The function uses a collection Counter where we are 
    taking 0 and 1 as keys and then printing them that mnay times
	"""
	c = Counter(arr)
	# print(c)
	return [0]*c[0] + [1]*c[1]




array = [int(item) for item in input().split()]
# segregate(array)
# print(array)
print(segregate_v2(array))