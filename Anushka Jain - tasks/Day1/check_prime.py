import math
num = int(input("Enter a number: "))
flag = False
if(num<=1):
    print(num, "is NOT a prime no")
    flag = True
    
i = 2
while(not(flag) and i <= math.sqrt(num)): 
    if(num % i == 0):
        print(num, "is NOT a prime no")
        flag = True
        break
    i += 1
if(not(flag)):
    print(num, "is a prime no")
