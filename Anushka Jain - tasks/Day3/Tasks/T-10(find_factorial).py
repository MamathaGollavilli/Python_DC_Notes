n = int(input("Enter a no to find it's factorial: "))
num = n
f = 1
if(n < 0):
    print("Invalid no to find factorial")
elif(n == 0 or n == 1):
    print("Factorial of", n, "is 1")
else:
    while(n > 1):
        f *= n
        n -= 1
    print("Factorial of", num, "is", f)    
