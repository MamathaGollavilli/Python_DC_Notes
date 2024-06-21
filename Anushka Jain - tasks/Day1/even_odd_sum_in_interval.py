start = int(input("Enter starting interval: "))
end = int(input("Enter ending interval: "))
even = odd = 0
for i in range(start, end+1):
    if(i%2 == 0):
        even += i
    else:
        odd += i
print("Odd sum: ",odd)
print("Even sum: ",even)
