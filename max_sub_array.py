sub_array=[]
def possible_combination(arr):
    """funcation to find all possible combinations of
       elements of array"""
    size=len(arr)
    for i in range(size):
        for count in range (i,size):
            sub_array.append(arr[i:count+1])

def sub_array_sum(sub_arr):
    """funaction to find sum of individual elements of a list of 
       subarrays and then finally prints the maximum subarray sum"""
    max_sum=-9999
    max_sub_array=[]
    for item  in sub_arr:
        if sum(item)>max_sum:
            max_sum=sum(item)
            max_sub_array=item
        #max_sub_array=item
    print(max_sum)
    print(max_sub_array)




























def kadanes_algo(arr):
    """
    calculates the maximum_sum_subarray
    """
    start, end, ct = 0, 0, 0

    if not arr:
        print("empty array")
        return
    max_ending_here=-999
    max_so_far=-999
    for i in range(len(arr)):
        #max_ending_here = max_ending_here + arr[i]

        
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            start = i
        else:
            max_ending_here = max_ending_here + arr[i]


        
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            # start = ct
            end = i
        

        # if max_ending_here < max_ending_here + arr[i]:
        #     max_ending_here = max_ending_here + arr[i]
        # elif max_ending_here + arr[i] < arr[i]:
        #     max_ending_here = arr[i]
        #     start = i

        # if max_so_far < max_ending_here:
        #     max_so_far = max_ending_here
        #     end = i



    print (max_so_far)
    print ("start {} --  end {}".format(start, end))
    print(arr[start:end+1])


# Python program to print largest contiguous array sum
 
from sys import maxsize
 
# Function to find the maximum contiguous subarray
# and print its starting and end index
def maxSubArraySum(a,size):
 
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0,size):
 
        max_ending_here += a[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
 
    print ("Maximum contiguous sum is %d"%(max_so_far))
    print ("Starting Index %d"%(start))
    print ("Ending Index %d"%(end))


















def kadanes_algo_v2(arr):
	max_end_here=max_so_far=arr[0]
	for x in arr[1:]:
		max_end_here = max(x,max_end_here+x)
		max_so_far = max(max_so_far,max_end_here)
	print(max_so_far)

array=[int(x) for x in input().split()]
print(array)
kadanes_algo(array)
#possible_combination(array)
#print(sub_array)
#sub_array_sum(sub_array)

