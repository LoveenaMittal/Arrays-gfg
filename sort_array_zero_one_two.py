"""
 This problem is also called Dutch National Flag problem
 Here we need to sort 0's 1's and 2's 
"""
from collections import Counter

def swap_elements(arr,i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def Deutch_flag(arr):
	"""
    we are maintianing 3 indexes low, mid and high
    low remains at the start and mid iterates through each swap_elements
    high remains at the end
    Once we get 0, then mid posn is swapped with low and both mid and low are increemented
    if we get 1 at mid's place, we simply increement mid
    if we get 2 then we swap mid posn with high posn and decreement high posn
	"""
	low, mid = 0, 0
	high = len(arr)-1
	while mid <= high:
		if arr[mid] == 0:
			swap_elements(arr,mid,low)
			mid+=1
			low+=1
		elif arr[mid] == 2:
			swap_elements(arr,mid,high)
			high-=1
		elif arr[mid] == 1:
			mid+=1

###############################################################


def Deutch_flag_v2(arr):
	"""
    second version of this can be done if we count the no. of
    0's 1's and 2's and then print them that many times
	"""
	c = Counter(arr)
	# c will have value Counter({0: 4, 1: 4, 2: 2})
	"""
    for key in c:
    ...:     print key
    this prints the key of counter i.e 0,1,2
	"""
	# new_arr = []
	
	# for i in range(c[0]):
	# 	new_arr.append(0)
	# for i in range(c[1]):
	# 	new_arr.append(1)
	# for i in range(c[2]):
	# 	new_arr.append(2)

	return [0]*c[0] + [1]*c[1] + [2]*c[2]
	# new_arr = list(c.elements())
	#return new_arr



array = [int(item) for item in input().split()]
# Deutch_flag(array)
print(Deutch_flag_v2(array))
