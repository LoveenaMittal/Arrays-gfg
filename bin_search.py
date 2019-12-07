# -------> recursive solution <-----------

# flag = 0
# since binary search an be applied on ona sorted array
# so we should be given the array in sorted order
# else need to sort it

def bin_search(arr, l, r, e):

    #base case check
    if r >= l:
        # calculating middle index
        mid = l + (r - l) // 2

        # if element is present at the middle itself
        if arr[mid] == e:
            return mid
        
        # if element is smaller than mid, then it
        # can be in left subarray

        elif arr[mid] > e:
            return bin_search(arr, l, mid-1, e)

        #else the element must be present in the right subarray

        else:
            return bin_search(arr, mid+1, r, e)

    else:
        #element is not present in the array
        return -1


arr = [-1,1,2,3,4,33,40]
e = 3
value = bin_search(arr, 0, len(arr)-1, e)
if  value != -1:
    print("element found at index ", value)
else:
    print("not found")