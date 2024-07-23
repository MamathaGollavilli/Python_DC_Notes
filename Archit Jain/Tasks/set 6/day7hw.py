####################################################################################################
# You are required to read the contents of a text file named `byte.txt`, process the lines, and write the output to a new file named `byte1.txt`. Specifically, you need to read all lines from `byte.txt`, remove any newline characters, and group the lines into chunks of four. Each group of four lines should then be reversed in order. Write these reversed groups to `byte1.txt`, with each group forming a single line in the output file. If the total number of lines is not a multiple of four, the last group should contain the remaining lines in reversed order. For instance, given the input file `byte.txt` with the lines `21`, `1f`, `20`, `34`, `36`, `74`, `90`, `98`, `78`, `45`, `23`, `b4`, and `09`, the output file `byte1.txt` should contain the lines `34201f21`, `98907436`, `b4234578`, and `09`.
####################################################################################################

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

####################################################################################################
# Write a python program to find the third largest number from a given list of numbers, use python 'set' data type.
####################################################################################################

f1 = open("nums.txt","r")
lst = f1.readlines()

new_lst = []

for i in lst:
    element = i.strip()
    if element.isdigit():
        new_lst.append(int(element))
print(new_lst)

new_set = set(new_lst)
print(new_set)

new_lst_no_repetition = list(new_set)
new_lst_no_repetition.sort()
print(new_lst_no_repetition)

print("The third largest number is: ",new_lst_no_repetition[2])

####################################################################################################
# DLL: Dynamic link library
# GCC: GNU Compiler Collection
####################################################################################################