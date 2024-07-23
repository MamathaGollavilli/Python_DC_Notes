f1 = open("byte.txt", "r")
f2 = open("byte1.txt", "w")

lst = f1.readlines()

new_lst = []
for line in lst:
    new_lst.append(line.strip())
print(new_lst)

grouped_lines = []
current_group = []

for line in new_lst:
    current_group.append(line)
    if len(current_group) == 4:
        grouped_lines.append(current_group[::-1])
        current_group = []

if current_group != []:
    grouped_lines.append(current_group[::-1])

print(grouped_lines)

for groups in grouped_lines:
    for i in groups:
        f2.write(i)
    f2.write('\n')

f1.close()
f2.close()

f1 = open("byte1.txt", "r")
lst = f1.readlines()
new_lst = []
for line in lst:
    new_lst.append(line.strip())
print(new_lst)
f1.close()
