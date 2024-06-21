with open ("num.txt") as f:
    lines = f.readlines()
print(lines)
max_no = int(lines[0])
min_no = int(lines[0])
for num in lines:
    if(int(num) > max_no):
        max_no = int(num)
    if(int(num) < min_no):
        min_no = int(num)
print("Maximum no:", max_no)
print("Minimum no:", min_no)
