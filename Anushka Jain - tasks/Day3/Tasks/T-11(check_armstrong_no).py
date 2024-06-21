import math
num = int(input("Enter no: "))
n = num
order = len(str(num))
s = 0

while(num > 0):
    di = num % 10
    s += (math.pow(di,order))
    num //= 10

if(s == n):
    print(n,"is an Armstrong no")
else:
    print(n,"is NOT an Armstrong no")
    
