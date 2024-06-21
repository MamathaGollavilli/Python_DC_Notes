f1 = open("num1.txt")
f2 = open("num2.txt")
f3 = open("merged.txt", "w")
lines1 = f1.readlines()
lines2 = f2.readlines()
print(lines1)
print(lines2)
if(len(lines1)<len(lines2)):
    i = 0
    while(i<len(lines1)):
        f3.write(lines1[i])
        f3.write(lines2[i])
        i += 1
    while(i<len(lines2)):
        f3.write(lines2[i])
        i += 1
else:
    i = 0
    while(i<len(lines2)):
        f3.write(lines1[i])
        f3.write(lines2[i])
        i += 1
    while(i<len(lines1)):
        f3.write(lines1[i])
        i += 1
f1.close()
f2.close()
f3.close()
f4 = open("merged.txt")
print(f4.read())
f4.close()
