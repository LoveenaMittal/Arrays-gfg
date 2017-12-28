# All possible combinations of an array

#arr = input().split()
arr = [int(item) for item in raw_input().split()]
size = len(arr)
sub_arr = []
for i in range(size):
    for count in range(i,size):
        sub_arr.append(arr[i:count+1])

print(sub_arr)




		
	
