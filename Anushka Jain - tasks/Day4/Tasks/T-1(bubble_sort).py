#bubble sort
li = [5, 4, 3, 2, 1]
n = len(li)
for i in range(1, n):
    no_of_comp = 0
    for j in range (0, n - i):
        if(li[j] > li[j+1]):
            li[j], li[j+1] = li[j+1], li[j]
            no_of_comp += 1
    if(not no_of_comp):
        break;
print(li)
            
