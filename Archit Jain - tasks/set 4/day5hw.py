# Read a file containing no's
# 1) Find sum of all the no's in that file
# 2) Find min and max no
# 3) Find all the even no's from that file

f=open("numbers.txt","r")
lst=f.readlines()
print(lst)

new_lst = []

for i in lst:
    if i.strip().isdigit():
        new_lst.append(int(i.strip()))
print(new_lst)

length = len(new_lst)
sum=0
# sum
for i in range (length):
    sum = sum + new_lst[i]
print("Sum of all the numbers in the file is: ",sum)

# min and max
print("Maximum number in the file is: ",max(new_lst))
print("Minimum number in the file is: ",min(new_lst))

# even numbers
for i in range (length):
    if new_lst[i]%2==0:
        print(new_lst[i],end=" ")

f.close()