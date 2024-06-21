with open ("num.txt") as f:
    lines = f.readlines()
for num in lines:
    if(int(num) % 2 == 0):
        print(int(num))
    
