"""
The program is to tell at which position the equilibrium first occurs in the array. 
Equilibrium position in an array is a position such that the sum of elements below 
it is equal to the sum of elements after it.
"""

def equi(arr):

	"""
	This solution is done in O(n2) times

	"""
	size = len(arr)
	for i in range(size):
		if sum(arr[:i]) == sum(arr[i+1:]):
			#checking if left sum of element is equal to right sum or not
			# if yes, return the index+1
			return (i+1)
			# Note: If we want to print all equilibrium indexes, we can 
			#       write a print statement instead of the return statement
	if i==size-1:
		# finally if i becomes equal to the last index
		# and no return has occured, means that there is no equilibrium
		return (-1)

################################################################################


def equilibrium(arr):
	"""
	This function takes O(n)
	"""

	size = len(arr)

	# finding the sum of whole array
	total_sum = sum(arr)
	
	left_sum = 0
	
	for i,item in enumerate(arr):

		# we start with index i
		# now the sum should be "total sum - array element"
		# here total_sum keeps track of the right sum of array

		total_sum -= item

		if left_sum == total_sum:
			return (i+1)
		# Note: If we want to print all equilibrium indexes, we can 
			#       write a print statement instead of the return statement	
		
		# here we are adding the element to find the left_sum
		left_sum += item
	return (-1)


array = [int(item) for item in input().split()]
# print(equi(array))
print(equilibrium(array))