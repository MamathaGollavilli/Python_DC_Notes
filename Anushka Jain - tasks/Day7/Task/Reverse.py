f = open("byte.txt")
lines = f.read().splitlines()
out = []
for i in range(0, len(lines),4):
    group = lines[i:i+4]
    reversed_group = ''.join(reversed(group))
    out.append(reversed_group)

for line in out:
    print(line)
    
