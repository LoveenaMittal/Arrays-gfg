def req_sub_array(arr,size,sum_req):
	sum_ending_here = 0
	start_index=0
	end_index=0
	# tracker=0
	for i in range(size):
		sum_ending_here+=arr[i]
		
		
		# if sum_ending_here != sum_req:
		while sum_ending_here>sum_req:
			sum_ending_here-=arr[start_index]
			#print("sum_ending_here = ", sum_ending_here)
			start_index+=1
			#print("start_index= ",start_index)
			if sum_ending_here == sum_req:
				end_index=i
				break
		if sum_ending_here == sum_req:
			end_index=i
			
			# print(arr[start_index:end_index+1])
			print("{} {}".format(start_index+1,end_index+1))		
			return


		# else:
		# 	end_index=i
	
	if i==size:
	    print(-1)
			






 

test_cases = int(input())
for i in range(test_cases):
	size,sum_req = input().split()
	size = int(size)
	sum_req = int(sum_req)
	arr = [int(item) for item in input().split()]
	req_sub_array(arr,size,sum_req)