
def prime_no(num):
    for i in range(2,num//2):
        if num % i == 0:
            return -1
    return 1

num = int(input())
res = prime_no(num)
if res != -1:
    print("num is prime")
else:
    print("num is not prime")