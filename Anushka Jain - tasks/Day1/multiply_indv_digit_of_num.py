num = int(input("Enter a num: "))
mul = 1
while(num > 0):
    digit = num % 10
    num //= 10
    if(num>0):
        print(digit,"*", end=" ")
    else:
        print(digit,"=", end=" ")
    mul *= digit
    
print(mul)
