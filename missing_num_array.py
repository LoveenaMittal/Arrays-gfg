test_cases = int(input())


for i in range(test_cases):
	size=int(input())
	arr=[int(item) for item in input().split()]


	"""
	Solution in O(n)
	
	# here we are adding all the elements of the array and then subtracting it from sum of 
	# 'N' natural nos

	"""

	total_sum = size*(size+1)/2
	sum=0
	for item in arr:
		sum+=item
	print(total_sum-sum)



############################################################
	
	"""
	Solution in O(n) using a dictionary
	

	# here we are converting out input array to a dict
	d={}
	for num in arr:
		d[num]="number"
	print(d)

	test = [x for x in range(1,size+1)]

	for item in test:
		try:
			temp=d[item]
		except:
			print("num not present-- {}".format(item))
	"""

###############################################################

"""
SOLUTION IN O(nlogn)

	arr.sort()
	index=0
	for num in range(1,size+1):
		# print("num={} --- arr{}={}".format(num,index,arr[index]))
		if (index!=size-1):
			if (arr[index]!=num):
				print(num)
				break
			else:
				index+=1
		else:
			print(num)
			break
"""



