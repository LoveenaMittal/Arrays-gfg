"""
This program finds all the leaders in an array
An element is leader if it is greater than all the elements to 
its right side. The rightmost element is always a leader. 
>>
>>
>>
The strategy would be to start from the last element and then 
proceed backwards (as last element is always a leader)
"""

def leader(arr):
	"""
	Here we are maintaining a tracker "max_till_now"
	that tracks the max element till now from right side
	if the array element is maxium than this variable, it
	is considered to be max of all the elements to it's right
	"""
	size = len(arr)
	leaders_array = []
	max_till_now = arr[size-1]
	i = size-2
	leaders_array.append(arr[size-1])
	while i>=0:
		if arr[i] > max_till_now:
			max_till_now = arr[i]
			leaders_array.append(arr[i])
		i-=1
	print(leaders_array[size-1::-1])

array = [int(item) for item in input().split()]
leader(array)





