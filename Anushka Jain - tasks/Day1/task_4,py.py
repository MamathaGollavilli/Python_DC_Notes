n = int(input("Enter a number: "))
sum = 0
for i in range(1,4):
    num = i * f"{n}" #3 * "5" == "555"
    if(i == 3):
        print(num, "=", end=" ")
    else:
        print(num, "+", end=" ")
    sum += int(num) 
print(sum)
