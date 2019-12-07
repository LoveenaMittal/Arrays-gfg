
def rev(num):
    temp = 0
    while (num >= 1):
        rem = num % 10 
        temp = temp*10+ rem
        num = num // 10
    return temp

def pall(num):
    if num == rev(num):
        print("Pallindrome")
    else:
        print("Not pallindrome")

num = int(input())
pall(num)
