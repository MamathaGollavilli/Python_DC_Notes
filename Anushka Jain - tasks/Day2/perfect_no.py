num = int(input("Enter a no: "))
if(num <= 1):
    print(num, "is NOT a perfect no")
else:
    sum = 0;
    for i in range(1, int(num*0.5)+1):
        if(num % i == 0):
            sum += i;
    if(sum == num):
        print(num, "is a perfect no")
    else:
        print(num, "is NOT a perfect no")
            
