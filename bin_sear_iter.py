# ---------- iterative solution ------------

def bin_search(arr, l, r, e):
    #print("l = %d r = %d",l,r)

    #base condition
    while l <= r:
        print("l = % r = %",l,r)

        # finding the middle index
        mid = l + (r - l) // 2
        #print(mid)

        # checking if element present at the middle index
        if arr[mid] == e:
            return mid
        
        elif arr[mid] > e:
            # if element is smaller than the middle
            # element then ignore right half
            r = mid - 1
            print("r --> ", r)

        else:
            # if element is greater than middle elemet
            # ignore first half
            l =  mid + 1
            print("l--> ",l)
        
        #if we reach here (loop has ended)
        # means elemet was not present
    return -1

arr = [2,3,4,10,20]
e = 0

result = bin_search(arr, 0, len(arr)-1, e)

if result != -1:
    print ("element found at index ", result)
else:
    print("elemnt not found")