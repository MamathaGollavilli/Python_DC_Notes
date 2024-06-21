f = open("num.txt")
lines = f.readlines()
print(lines)
sum = 0
for num in lines:
    sum += int(num)
print(sum)
f.close()
