start = int(input("Enter starting interval: "))
end = int(input("Enter ending interval: "))
for i in range(start, end+1):
    if(i%3 == 0 and i%6 == 0):
        print(i)
